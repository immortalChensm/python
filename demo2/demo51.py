
from PIL import Image

im = Image.open("code.png")

print(dir(Image))
print(im.size,im.mode)

im.thumbnail((100,15))
im.save("temp.png")