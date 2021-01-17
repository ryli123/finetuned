from PIL import Image, ImageEnhance, ImageOps
from PIL import ImageFilter, ImageChops
from PIL.ImageFilter import (
    RankFilter, MedianFilter, MinFilter, MaxFilter
    )

#image = Image.open("city.jpeg")
#image.show()

#enhancer = ImageEnhance.Brightness(image)
#enhancer.enhance(0.25).save(
#    "ImageEnhance_Brightness_100.jpg")

def song_to_image(image, song_extract, sentiment): #pass sentiment in too 
    #sentiment passed in as tuple of (pos, neutral, neg) that sum up to 1 
    photo = Image.open(image)

    print(photo.format)
    print(photo.mode)
    print(photo.size)

    pos = sentiment[0]
    neut = sentiment[1]
    neg = sentiment[2]

    # FOR SENTIMENT ANALYSIS 


    # put the filtering stuff here, return an edited image
    # the song_extract is an array in this order
    # danceability, tempo, energy, valence, mode, loudness, instrumentalness

    # STEP 1: saturation
    sat_ratio1 = 0.75
    sat_ratio2 = 0.75
    sat_ratio3 = 0.5
    
    saturation = song_extract[3]*sat_ratio1 + song_extract[0]*sat_ratio2 - song_extract[6]*sat_ratio3
    print(saturation)
    photo = ImageEnhance.Color(photo).enhance(saturation)

    # STEP 2: contrast
    con_ratio1 = 1.2
    con_ratio2 = 0.8
    
    contrast = song_extract[2]*con_ratio1 + -song_extract[5]/60*con_ratio2
    print(contrast)
    photo = ImageEnhance.Contrast(photo).enhance(contrast)

    #STEP 3: brightness
    bri_ratio1 = 1
    bri_ratio2 = 1/200
    
    brightness = song_extract[2]*bri_ratio1 + song_extract[1]*bri_ratio2
    photo = ImageEnhance.Brightness(photo).enhance(brightness)

    #STEP 4: sharpness
    sha_ratio1 = 1
    sha_ratio2 = 1
    sha_ratio3 = 2
    
    sharpness = song_extract[0]*sha_ratio1 + song_extract[4]*sha_ratio2 + -song_extract[5]/60*sha_ratio3
    photo = ImageEnhance.Sharpness(photo).enhance(sharpness)

    #invert colors idk if we can use this

    #photo = ImageChops.invert(photo)

    #convert to greyscale maybe for sad songs?
    
    if (song_extract[1]/100 + song_extract[2] + song_extract[3] < 1.5 and song_extract[4] == 0):
        photo = ImageOps.grayscale(photo)

    
    '''
    if (song_extract[4] == 0):
        pic = photo.filter(MaxFilter(size=9))
        pic.save("ImageFilter_MinFilter_9.jpg")
    if (song_extract[4] == 1):
        pic = photo.filter(MaxFilter(size=9))
        pic.save("ImageFilter_MaxFilter_9.jpg")

    this feels kinda over kill
    '''
    '''
    if (song_extract[4] == 0):
        pic = photo.filter(ImageFilter.SMOOTH)
        pic.save("ImageFilter_MinFilter_9.jpg")
    if (song_extract[4] == 1):
        pic = photo.filter(ImageFilter.SMOOTH) #<--- idk
        pic.save("ImageFilter_MaxFilter_9.jpg")

    '''
    #photo.show()
    path="static/edits/" + image[15:].rsplit('.', 1)[0] + "_edited.jpg"
    photo.save(path)
    return path

#song_to_image('city.jpeg', [0.728, 65.043, 0.859, 0.535, 0, -5.237, 0], [0.2, 0.4, 0.4])
