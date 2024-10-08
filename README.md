# FacelessShorts

Faceless Shorts is a web application that generates short stories based on a given prompt. The application uses a pre-trained T-5 model and diffusion 2 for images to generate the stories. The user can input a prompt and the model will generate a short story based on the prompt.  The application is built using Flask and Huggingface Transformers.

## Models 
diffusion 2 - image generation
flan/t5-large - text generation

## Frameworks
Flask 
Huggingface Transformers
Moviepy
ImageMagick


## Installation
1. Clone the repository
2. Create a virtual environment
3. Install the required packages using the requirements.txt file
4. Create a `.env` file in the root directory and add the following variables:
```ImageMagick = "path to ImageMagick" ```
this is for using the ImageMagick library for moviepy library - need have ImageMagick installed on your system
4. In root directory, run the command `python run.py`
5. Open the browser and go to `http://localhost:5000/`


## Usage
1. Enter a prompt in the text box
2. wait for the story to be generated

Its supposed be a fun project, so the stories generated are not always coherent. Also it is intended to be used fo generating short stories to post on social media or for fun.