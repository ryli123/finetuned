from PIL import Image, ImageEnhance
image = Image.open('city.jpeg')

print(image.format)
print(image.mode)
print(image.size)

image.show()

enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(0.25).save(
    "ImageEnhance_Brightness_100.jpg")