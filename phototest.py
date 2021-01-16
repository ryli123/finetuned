from PIL import Image, ImageEnhance
from PIL import ImageFilter
from PIL.ImageFilter import (
    RankFilter, MedianFilter, MinFilter, MaxFilter
    )
image = Image.open('city.jpeg')

print(image.format)
print(image.mode)
print(image.size)

#image.show()

enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(0.25).save(
    "ImageEnhance_Brightness_100.jpg")

def song_to_image(photo, song_extract):
    # put the filtering stuff here, return an edited image
    # the song_extract is an array in this order
    # danceability, tempo, energy, valence, mode

    # STEP 1: saturation
    saturation = song_extract[3]*10*0.6 + song_extract[0]*10*0.4 
    print(saturation)
    photo = ImageEnhance.Color(photo).enhance(saturation)

    # STEP 2: contrast
    contrast = song_extract[2]*5
    photo = ImageEnhance.Contrast(photo).enhance(contrast)

    if (song_extract[4] == 0):
        pic = photo.filter(MinFilter(size=9))
        pic.save("ImageFilter_MinFilter_9.jpg")
    if (song_extract[4] == 1):
        pic = photo.filter(MaxFilter(size=9))
        pic.save("ImageFilter_MaxFilter_9.jpg")

song_to_image(image, [0.262, 145.353, 0.458, 4, 0])
