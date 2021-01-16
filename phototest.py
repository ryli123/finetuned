from PIL import Image, ImageEnhance
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
