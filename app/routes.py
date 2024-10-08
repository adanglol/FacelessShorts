#  Edit captions with video - captions go along withh voiceover
#  make sure voice dont sound like robot 
#  Add music to the background  ?
#  make text clip look good 
#  make sure content isnt wack 
#  make sure video is good
#  eventually upload to yt or tik tok ?? 



# TITLE 
# CONTENT PROMPT 
# UI
# IMAGE PROMPTING
# FINE TUNE VOICE
# FINE TUNE MODEL




from flask import Blueprint, render_template, request, jsonify, send_file

from .voiceover import generate_content
# import pyttsx3
# import os   
# from transformers import pipeline
# import moviepy.editor as mpy
# from moviepy.config import change_settings

main = Blueprint('main', __name__)  # Create a Blueprint object

# Set the path to the ImageMagick binary - needed for moviepy
# change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})  #Should be relative to where your ImageMagick is installed
# voice_over_path = r"C:\Users\adrag\OneDrive\Desktop\Projects\FacelessShorts\Generated\Audios"
# video_path = r"C:\Users\adrag\OneDrive\Desktop\Projects\FacelessShorts\Generated\Videos"


# Initialize voice engine - pyttsx3 and set properties
# engine = pyttsx3.init()
# engine.setProperty('rate', 200) 
# engine.setProperty('volume', 0.9)
# engine.setProperty('voice', engine.getProperty('voices')[1].id)  


   


@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/generate', methods=['POST'])
# def generate():
#     # Get Title of the story
#     title = request.form.get('title')
#     # Get user prompt
#     user_prompt = request.form.get('user_prompt')
#     # Get image prompt
#     image_prompt = request.form.get('image_prompt')

#     # Call the generate_content function to create the video and return it
#     video_io = generate_content(title, image_prompt, user_prompt)

#     # Return video as downloadable file via Flask
#     return send_file(video_io, as_attachment=True, download_name="generated_video.mp4", mimetype='video/mp4')
    
    


@main.route('/generate', methods=['POST'])
def generate():
    # Get Title of the story
    title = request.form.get('title')
    # Get user prompt
    user_prompt = request.form.get('user_prompt')
    # Get image prompt
    image_prompt = request.form.get('image_prompt')


    print(title)
    print(user_prompt)
    print(image_prompt)
      # Convert image_prompt to string, ensuring it is not None
    title = str(title) if title is not None else ""
    image_prompt = str(image_prompt) if image_prompt is not None else ""
    user_prompt = str(user_prompt) if user_prompt is not None else ""
     # # Call the generate_content function to create the video and return the file path
    video_file_path = generate_content(title, image_prompt, user_prompt)
    print(video_file_path)
    return jsonify({"Success": "Success"})
        
   

    # # Return video as downloadable file via Flask
    # return jsonify({"Success": video_file_path})
