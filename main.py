import pickle
from PIL import Image
with open("fin.dict","rb") as f:
    mydict=pickle.load(f)

#Old Image
img0=Image.open("input.png").convert('1')

#New Image
img = Image.new( '1', (img0.size[0]*2,img0.size[1]*2)) # create a new black image
pixels0 = img0.load() # create the pixel map
pixels = img.load()


for i in range(img0.size[1]): 
    for j in range(img0.size[0]):
        value=mydict[int(pixels0[i,j]/255*8+pixels0[i,j]/255*4+pixels0[i,j]/255*2+pixels0[i,j]/255)]
        for pix in value:
            p=int(pix)
            pixels[j+(i*2)%4,i+(i*2)//4]=p*255
            # print(p*255)
        

img.show()
img.save("new.png")