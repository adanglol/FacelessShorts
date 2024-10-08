
from transformers import pipeline
import pyttsx3
from moviepy.editor import *
from moviepy.video.fx.resize import resize
from moviepy.config import change_settings
import os
from dotenv import load_dotenv
import numpy as np

from PIL import Image

load_dotenv()

# Set the path to the ImageMagick binary
imageMagickPath = os.getenv("IMAGEMAGICK_BINARY")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.6)  # Volume 0-1

change_settings({"IMAGEMAGICK_BINARY": imageMagickPath})

# Load the text-to-text generation pipeline with Flan-T5 on GPU
generator = pipeline("text2text-generation", model="google/flan-t5-large", device=0)

prompt = (
    "Create a chilling and suspenseful story of about 200 words about a girl named Lily who confronts her fears in an abandoned house."
    "Begin with Lily exploring the dark and decaying house on a dare, feeling a mix of excitement and trepidation."
    "Describe the eerie atmosphere as she hears strange creaks and whispers echoing through the empty halls."
    "Illustrate Lily's growing anxiety as she discovers unsettling clues, such as faded photographs and a locked door that seems to call her name."
    "Express the tension as shadows flicker and a cold wind sweeps through, heightening her fear and making her question whether she is truly alone."
    "Conclude with a terrifying encounter that reveals the house's dark history, leaving Lily to escape with her heart racing, haunted by what she has experienced and forever changed by the encounter."
)


# Generate the story
story = generator(
    prompt,
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
image_path = "October.png"  # Replace with your image path
audio_clip = AudioFileClip(audio_file_path)


image = Image.open(image_path).resize((1080, 1920), Image.LANCZOS)
image_array = np.array(image)
background_clip = ImageClip(image_array).set_duration(audio_clip.duration)  # Set duration to match audio

# Create the title text clip
title_text = "Scary Stories"  # Replace with your actual story title
title_clip = TextClip(title_text, fontsize=100, color='black', bg_color='white', size=(900, 0), method='caption', font='Courier-Bold')
title_clip = title_clip.set_position('center').set_duration(audio_clip.duration)  # Position in center and match duration with audio

# Combine the background and title clip
final_clip = CompositeVideoClip([background_clip, title_clip], size=(1080, 1920))

# Set the audio for the final video
final_clip = final_clip.set_audio(audio_clip)

# Write the final video file
video_file_path = "story_video_with_title.mp4"
final_clip.write_videofile(video_file_path, fps=24)



