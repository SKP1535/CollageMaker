import cv2
from imutils import build_montages
from PIL import Image
import numpy


def makecollage(imagepaths,filename,blockheight,blockwidth):


    images = []
    #Reading all images
    for imgpath in imagepaths:
        image = cv2.imread(imgpath)
        if image is None:
            imimage = Image.open(imgpath).convert('RGB')
            image = cv2.cvtColor(numpy.array(imimage), cv2.COLOR_RGB2BGR)
        
        images.append(image)
    # if len(images) < 10:
    #     col = len(images)
    #     r = 1

    #Calculating number of rows and columns required to generate collage
    num = 1
    col = len(images)
    while 1:
        var = len(images)/num
        if var >= num :
            col = num
            num = num + 1
        elif var < num:
            break
    row = col
    sqr = col**2
    sub = len(images)-sqr
    div = sub/col
    check = div - int(div)
    if check > 0:
        div = div + 1
    div = int(div)
    row = row + div

    #Generating collage
    montages = build_montages(images,(blockheight,blockwidth),(col,row))

    #Saving Collage
    cv2.imwrite(filename,montages[0])

