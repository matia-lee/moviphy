import os
from moviepy import VideoFileClip

input_folder = "files/"
output_folder = "fragments/"
os.makedirs(output_folder, exist_ok=True)

def split_video_into_fragments(input_video_file, fragment_duration):
    fragment_num = 1

    clip = VideoFileClip(input_video_file)
    duration = int(clip.duration)

    fragment_start = 0
    
    while fragment_start < duration:
        fragment_end = min(fragment_start + fragment_duration, duration)
        output_file = os.path.join(output_folder, f"fragment_{fragment_num}.mp4")
        new = clip.subclipped(fragment_start, fragment_end)
        new.write_videofile(output_file, audio_codec="aac")

        print(f"Processed fragment {fragment_num}")

        fragment_start += fragment_duration
        fragment_num += 1

    clip.close()

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_video_file = os.path.join(input_folder, filename)
        split_video_into_fragments(input_video_file, 10)