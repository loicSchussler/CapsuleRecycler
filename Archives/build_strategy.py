from PIL.Image import *
import random
import math
import cProfile
import re


def main():
    def distanceBetweenColors(RGB1,RGB2):
        rmean = (RGB1[0] + RGB2[0])//2
        r = RGB1[0] + RGB2[0]
        g = RGB1[1] + RGB2[1]
        b = RGB1[2] + RGB2[2]
        return sqrt((((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8))

    def minimalDistanceColor(RGB,lePalette):
        mini = 99999999
        stock = 0
        for i in range(lePalette):
            dist = distanceBetweenColors(RGB,Palette[i])
            if dist < mini:
                mini = dist
                stock = i
        return Palette[stock]


    def approximPicture():

        for line in range(heightImg):
            for column in range(widthImg):
                RGB = rgb_im.getpixel((line,column))
                color = minimalDistanceColor(RGB,lePalette)
                rgb_im.putpixel((line,column),color)


    im = open("modelPics.jpg")
    (heightImg,widthImg) = im.size
    rgb_im = im.convert('RGB')

    sqrt = math.sqrt
    r,g,b = 0,0,0
    Palette = []
    for i in range(50):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        Palette.append((r,g,b))
    lePalette = 50

    approximPicture()

    rgb_im.save("modelPicsModified.jpg")



cProfile.run('main()')

