from PIL import *


def findAllLeftCorners():
    s = ""
    nb = 0
    for line in range(heightImg):
        for column in range(widthImg):
            if (not(parse[line][column]) and isDifferentColor(rgb_im.getpixel((line,column)))):
                squareCoords = findSquareCoords(line,column)
                color = findMedianeColorOfASquare(squareCoords[0],squareCoords[1],squareCoords[2],squareCoords[3])
                nb += 1
                colorASquare(squareCoords[0],squareCoords[1],squareCoords[2],squareCoords[3],color)
                s += str(color[0])+" "+str(color[1])+" "+str(color[2])+" "+str(nb)+"\n"
    return s





def findSquareCoords(leftCornerX,leftCornerY):
    x = leftCornerX
    y = leftCornerY
    RGB = rgb_im.getpixel((x,y))

    while (RGB != (0,0,0) and x < heightImg):
        RGB = rgb_im.getpixel((x,y))
        x += 1

    botLeftCorner = (x,y)
    x = leftCornerX
    y = leftCornerY

    RGB = rgb_im.getpixel((x,y))
    while (RGB != (0,0,0) and y < widthImg):
        RGB = rgb_im.getpixel((x,y))
        y += 1
    
    rightCorner = (x,y)
    botRightCorner = (botLeftCorner[0],rightCorner[1])

    return ((leftCornerX,leftCornerY),rightCorner,botLeftCorner,botRightCorner)
    

def findMedianeColorOfASquare(leftCorner,rightCorner,botLeftCorner,botRightCorner):
    r,g,b = 0,0,0
    
    size = 0

    for line in range(leftCorner[0],botLeftCorner[0]):
        for column in range(leftCorner[1],rightCorner[1]):
            size += 1
            RGB = rgb_im.getpixel((line,column))
            r += RGB[0]
            g += RGB[1]
            b += RGB[2]
    
    return (r//size,g//size,b//size)

def colorASquare(leftCorner,rightCorner,botLeftCorner,botRightCorner,color):
     for line in range(leftCorner[0],botLeftCorner[0]):
        for column in range(leftCorner[1],rightCorner[1]):
            parse[line][column] = True
            rgb_im.putpixel((line,column),color)


def isDifferentColor(RGB):
    mean_comp = (RGB[0]+RGB[1]+RGB[2])/2
    mean_ref = (neutralColor[0]+neutralColor[1]+neutralColor[2])/2
    
    diff = mean_comp - mean_ref

    return abs(diff) > 30


def isWhiteLine(line):
    global rgb_im

    
    for column in range(widthImg):
        #RGB = rgb_im.getpixel((line,column))
        RGB = copieImg[line][column]
        notWhite  = isDifferentColor(RGB)
        if notWhite:
            return False
    return True
    
def isWhiteColumn(column):
    global rgb_im

    for line in range(heightImg):
        #RGB = rgb_im.getpixel((line,column))
        RGB = copieImg[line][column]
        notWhite = isDifferentColor(RGB)
        if notWhite:
            return False
    return True


def segmentation():
    global rgb_im
    RGB = (0,0,0)

    for line in range(heightImg):
            #RGB = rgb_im.getpixel((line,0))
            RGB = copieImg[line][0]
            if (not(isDifferentColor(RGB))):
                traitementLigne(line)

    for column in range(widthImg):
            #RGB = rgb_im.getpixel((0,column))
            RGB = copieImg[0][column]
            if (not(isDifferentColor(RGB))):
                traitementColonne(column)
        
            

def traitementLigne(line):
    global rgb_im
    
    #RGB = rgb_im.getpixel((line,0))
    RGB = copieImg[line][0]


    if isWhiteLine(line):
        for column in range(widthImg):
            rgb_im.putpixel((line,column),(0,0,0))
        

def traitementColonne(column):
    global rgb_im
    
    #RGB = rgb_im.getpixel((0,column))
    RGB = copieImg[0][column]
    
    if isWhiteColumn(column):  
        for line in range(heightImg):
            rgb_im.putpixel((line,column),(0,0,0))


im = PIL.Image.open("capsule.jpg")
(heightImg,widthImg) = im.size
rgb_im = im.convert('RGB')
RGB = (0,0,0)

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

segmentation()

s = findAllLeftCorners()


#capsules = []
#newCapsColor = (0,0,0)
#wasLastCapsuleDifferentColor = False

rgb_im.save("testcapsModified.jpg")
rgb_im.close()

f = open("capsMap.txt","w")
f.write(s)
f.close()
