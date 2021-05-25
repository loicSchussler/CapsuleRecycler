import PIL.Image
import pickle
import glob
import os


def main():
    def getColorDistance(current,match):
        redDiff = 0
        greenDiff = 0
        blueDiff = 0

        refDiff = current[0] - match[0]
        greenDiff = current[1] - match[1]
        blueDiff = current[2] - match[2]

        return redDiff * redDiff + greenDiff * greenDiff + blueDiff * blueDiff


    def segmentation():
        red = 0
        green = 0
        blue = 0
        for line in range(heightImg):
            for column in range(widthImg):
                rgb = rgb_im.getpixel((line,column))
                colorDiff = getColorDistance(rgb,neutralColor)
                if colorDiff < colorThreshold:
                    red += rgb[0]
                    green += rgb[1]
                    blue += rgb[2]
                    rgb_im.putpixel((line,column),(0,0,0))
        return (red//sizeImg,green//sizeImg,blue//sizeImg)
    
    
    infos = pickle.load( open( "save.p", "rb" ) )

    index = 0
    for filename in glob.glob(os.path.join(infos["folderPath"], '*.jpg')):
        im = PIL.Image.open(filename)
        (heightImg,widthImg) = im.size
        sizeImg = heightImg * widthImg
        rgb_im = im.convert('RGB')
        colorThreshold = 20

        copieImg = []
        parse = []
        for i in range(heightImg):
            add = []
            addparse = []
            for j in range(widthImg):
                add.append(rgb_im.getpixel((i,j)))
                addparse.append(False)
            copieImg.append(add)
            parse.append(addparse)

        neutralColor = rgb_im.getpixel((0,0))

        colorOfTheCaps = segmentation()
        infos[str(index)]["color"] = str(colorOfTheCaps[0])+" "+str(colorOfTheCaps[1]+" "+str(colorOfTheCaps[2])


        #rgb_im.save("testcapsModified.jpg")
        rgb_im.close()
        
        index += 1

    print("finish")

