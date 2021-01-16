from PIL import Image, ImageFilter, ImageEnhance
import sys

color = 10
contrast = 1.2
brightness = 10
sharpness = 10
blur = True
contour = True
smooth = True
detail = True
edge_enhance = True


try:
    img = Image.open("Image.png")

except IOError:
    print("Unable to load image")
    sys.exit(1)

img.show()
img = ImageEnhance.Contrast(img).enhance(contrast)
img = ImageEnhance.Brightness(img).enhance(brightness)
img = ImageEnhance.Color(img).enhance(color)
img = ImageEnhance.Sharpness(img).enhance(sharpness)

if blur:
    img = img.filter(ImageFilter.BLUR)

if contour:
    img = img.filter(ImageFilter.CONTOUR)

if smooth:
    img = img.filter(ImageFilter.SMOOTH)

if detail:
    img = img.filter(ImageFilter.DETAIL)

if edge_enhance:
    img = img.filter(ImageFilter.EDGE_ENHANCE)


img.save("filtered.png")
img.show()

