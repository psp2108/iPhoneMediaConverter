import os
from wand.image import Image
from moviepy.editor import *
import shutil

def convert_heic_to_jpeg(input_file, output_file):
    with Image(filename=input_file) as image:
        # Convert the image to JPEG
        image.format = 'jpeg'

        # Save the image as JPEG
        image.save(filename=output_file)


def video_to_mp4(input, output):
    try:
        video = VideoFileClip(input)
        if video.rotation in [90, 270]:
            video = video.resize(video.size[::-1])
            video.rotation = 0
        video.write_videofile(output, codec='libx264')
        video.close()

    except Exception as e:
        print(f"Failed to convert {input}: {str(e)}")

# source = "D:\\Pictures\\Tamini Ghat + Kundalika Valley 15072023\\Tamini Ghat"
# destination = "converted"

source = input("Enter path of source folder: ")
destination = input("Enter path of destination folder (where you want ur converted files to be): ")

files = os.listdir(source)

if not os.path.exists(destination):
    os.makedirs(destination)

heic = []
mov = []
other = []

for i in files:
    i = i.lower()
    if i[-5:] == ".heic":
        heic.append(i)
    elif i[-4:] == ".mov":
        mov.append(i)
    else:
        other.append(i)

heicCount = len(heic)
movCount = len(mov)
otherCount = len(other)

print(f"Total Photos: {heicCount}, Videos:{movCount}, Other:{otherCount}")

print("Converting Photos...")
for i in range(heicCount):
    eachPhoto = heic[i]
    print(f'{i+1}/{heicCount} -- {eachPhoto}')

    convert_heic_to_jpeg(os.path.join(source, eachPhoto), os.path.join(destination, eachPhoto.lower().replace('.heic', '.jpeg')))

print("Converting Videos...")
for i in range(movCount):
    eachVideo = mov[i]
    print(f'{i+1}/{movCount} -- {eachVideo}')

    video_to_mp4(os.path.join(source, eachVideo), output=os.path.join(destination, eachVideo.lower().replace('.mov', '.mp4')))

print("Copying other files...")
for i in range(otherCount):
    eachFile = other[i]

    shutil.copy2(os.path.join(source, eachFile), os.path.join(destination, eachFile))