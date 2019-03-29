import pickle
from PIL import Image
with open("fin.dict","rb") as f:
    mydict=pickle.load(f)

#Old Image
img0=Image.open("input.png").convert('1')

#New Image
img = Image.new( '1', (img0.size[0]*2,img0.size[1]*2),0) # create a new black image
pixels0 = img0.load() # create the pixel map
pixels = img.load()


for i in range(img0.size[1]-1): 
    for j in range(img0.size[0]-1):
        value=mydict[int(pixels0[i,j]/255*8+pixels0[i,j]/255*4+pixels0[i,j]/255*2+pixels0[i,j]/255)]
        myindex=0
        for pix in value:
            p=int(pix)
            # print([(i-1)*2+myindex%4,(j-1)*2+myindex//4])
            pixels[(i)*2+myindex%4,(j)*2+myindex//4]=max(p*255,pixels[(i)*2+myindex%4,(j)*2+myindex//4])
            # print(p*255)
            myindex+=1
        

img.show()
img.save("new.png")