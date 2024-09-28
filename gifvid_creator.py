from glob import glob
from os import path
from PIL import Image
import cv2


def create_gif(images, duration=500):
    """Uses the PIL library to create a gif from a list of images """
    gif = []
    for imagefile in imagefiles:
        image = Image.open(imagefile)
        gif.append(image)
    gif[0].save('project.gif',
                save_all=True,
                optimize=False,
                append_images=gif[1:],
                duration=duration,
                loop=0
                )


def create_video(images, fps=1):
    """Uses openCV to create a video """
    example_img = cv2.imread(images[0])
    height, width, _ = example_img.shape
    out = cv2.VideoWriter('project.mp4',
                          cv2.VideoWriter_fourcc(*'mp4v'),
                          fps,
                          (width, height))
    for imagefile in imagefiles:
        img = cv2.imread(imagefile)
        out.write(img)
    out.release()


if __name__ == '__main__':
    # folder with the images
    imagefolder = "example_images"
    image_extension = ".png"
    imagefiles = sorted(glob(path.join(imagefolder, '*' + image_extension)))
    create_gif(imagefiles, duration=500)
    create_video(imagefiles, fps=1)
