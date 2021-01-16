from PIL import Image, ImageEnhance
from PIL import ImageFilter
from PIL.ImageFilter import (
    ModeFilter
    )
image = Image.open('city.jpeg')

print(image.format)
print(image.mode)
print(image.size)

image.show()

enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(0.25).save(
    "ImageEnhance_Brightness_100.jpg")

def song_to_image(photo, song_extract):
    # put the filtering stuff here, return an edited image
    # the song_extract is an array in this order
    # danceability, tempo, energy, valence, mode

    if (song_extract[4] == 0):
        pic = photo.filter(MinFilter(size=9))
        pic.save("ImageFilter_MinFilter_9.jpg")
    if (song_extract[4] == 1):
        pic = photo.filter(MaxFilter(size=9))
        pic.save("ImageFilter_MaxFilter_9.jpg")

song_to_image(image, [0.262, 145.353, 0.458, 4, 0])
