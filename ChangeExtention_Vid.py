from moviepy.editor import *
import os

def convert_to_mp4(input_files, output_dir):
    for input_file in input_files:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Get the filename (without extension) for the output file
        output_filename = input_file.split('/')[-1].split('.')[0]
        
        # Set the output file path
        output_file = f"{output_dir}/{output_filename}.mp4"
        
        # Convert to MP4 format
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Example usage
input_files = ['v1.MOV', 'v2.MOV', 'v3.MOV', 'v4.MOV', 'v5.MOV', 'v6.MOV','v7.MOV' , 'v8.MOV', 'v9.MOV', 'v10.MOV']
output_dir = 'converted_videos'  # Change this to the desired output directory

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

convert_to_mp4(input_files, output_dir)
