import PIL.Image
import pickle
import glob
import os

def differenceBetweenRGBComponents(color):
    return (abs(color[0] - color[1]) + abs(color[0] - color[2]) + abs(color[1] - color[2]))//3
        

def main():

    def isWhite(color):
        return differenceBetweenRGBComponents(color) > colorTreshold
    
    def segmentation():
        red = 0
        green = 0
        blue = 0
        mean_divisor = 0
        for line in range(heightImg):
            for column in range(widthImg):
                rgb = rgb_im.getpixel((line,column))
                colorDiff = differenceBetweenRGBComponents(rgb)
                if colorDiff > colorThreshold:
                    mean_divisor += 1
                    red += rgb[0]
                    green += rgb[1]
                    blue += rgb[2]

        return (red//mean_divisor,green//mean_divisor,blue//mean_divisor)


    def saveInfos():
        f  = open("Build_strategyCS/Build_strategyCS/capsInfos.txt","w")
        f.write(infos["folderPath"]+"\n")

        for key,value in infos.items():
            if key != "folderPath":
                f.write(key+" "+value["numberOfCaps"]+" "+value["color"]+"\n")
        f.close()
                
                
            
        

    
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

        infos[str(index)]["color"] = str(colorOfTheCaps[0])+" "+str(colorOfTheCaps[1])+" "+str(colorOfTheCaps[2])


        #rgb_im.save("testcapsModified.jpg")
        rgb_im.close()

        
        index += 1


    saveInfos()
    print("finish")


    
    

