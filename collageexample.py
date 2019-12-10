from collagemaker import makecollage
import os

filename = 'example.png'
imagepaths = os.listdir('Images')
imagepaths = ['Images/'+i for i in imagepaths if '.png' in i or '.jpg' in i]
blockheight = 128
blockwidth = 128
makecollage(imagepaths,filename,blockheight,blockwidth)