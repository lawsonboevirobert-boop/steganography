from PIL import Image


pex = Image.open("pex.jpg")

print(pex)
pex.save("new_pex.png")

