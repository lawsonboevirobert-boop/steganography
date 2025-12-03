from PIL import Image


pex = Image.open("pex.jpg")

print(pex)
pex.save("new_pex.png")


largeurs = pex.size[0]
hauteurs =pex.size[1]

def img_position(x,y,image):
    pixel = image.getpixel((x,y))
    return print(pixel)

img_position(1,4,pex)
    

        