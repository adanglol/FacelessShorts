# import pyttsx3
# from transformers import pipeline
# from moviepy.editor import *
# from moviepy.config import change_settings
# import io
# from dotenv import load_dotenv
# import torch
# from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
# import tempfile

from transformers import pipeline
import pyttsx3
from moviepy.editor import *
from moviepy.video.fx.resize import resize
from moviepy.config import change_settings
import os
from dotenv import load_dotenv
import numpy as np
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# Load environment variables
load_dotenv()

imageMagickPath = os.getenv("IMAGEMAGICK_BINARY")

change_settings({"IMAGEMAGICK_BINARY": imageMagickPath})
    
# Initialize models and pyttsx3 engine as before
generator = pipeline("text2text-generation", model="google/flan-t5-large", device=0)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.6)

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")




def generate_content(title, image_prompt, user_prompt):
    print("Generating content...")

    # Generate the image
    image = pipe(image_prompt).images[0]
    image.save("Bg.png")
    
    # Generate the story
    story = generator(
        user_prompt,
        max_length=500,
        min_length=250,
        num_return_sequences=1,
        temperature=0.9,
        top_k=50,
        top_p=0.9,
        do_sample=True
    )

    # Get Generated Story
    generated_text = story[0]['generated_text']

    # Text-to-speech - Save generated story to audio file
    audio_file_path = "story.wav"
    engine.save_to_file(generated_text, audio_file_path)
    engine.runAndWait()

    # Load the audio file and image
    image_path = "Bg.png"  # Replace with your image path
    audio_clip = AudioFileClip(audio_file_path)


    image = Image.open(image_path).resize((1080, 1920), Image.LANCZOS)
    image_array = np.array(image)
    background_clip = ImageClip(image_array).set_duration(audio_clip.duration)  # Set duration to match audio

    # Create the title text clip
    title_clip = TextClip(title, fontsize=100, color='black', bg_color='white', size=(900, 0), method='caption', font='Courier-Bold')
    title_clip = title_clip.set_position('center').set_duration(audio_clip.duration)  # Position in center and match duration with audio

    # Combine the background and title clip
    final_clip = CompositeVideoClip([background_clip, title_clip], size=(1080, 1920))

    # Set the audio for the final video
    final_clip = final_clip.set_audio(audio_clip)

    # Write the final video file
    video_file_path = "story_video_with_title.mp4"
    final_clip.write_videofile(video_file_path, fps=24)
    
