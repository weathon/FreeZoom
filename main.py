import pickle
from PIL import Image
mydict=pickle.load(open("fin.dict","rb"))

# pixels = img.load() # create the pixel map

#Old Image
img0=Image.open("input.png", mode='r').convert('1')

#New Image
img = Image.new( '1', (img0.size[0]*2,img0.size[1]*2)) # create a new black image
pixels0 = img0.load() # create the pixel map
pixels = img.load()


for i in range(img.size[0]): 
    for j in range(img.size[1]):
        

img.show()
img.save("new.png")