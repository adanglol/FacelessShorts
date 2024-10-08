import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "Spooky forest background with full moon and fog. Its for halloween shorts"
image = pipe(prompt).images[0]
    
image.save("October.png")



# from dotenv import load_dotenv
# import os
# load_dotenv()


# var = os.getenv("IMAGEMAGICK_BINARY")
# print(var)