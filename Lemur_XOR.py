import numpy as np
from PIL import Image, ImageChops
img1=Image.open('1.png', mode='r').convert("1")
img2=Image.open('2.png', mode='r').convert("1")
result=ImageChops.logical_xor(img1,img2)
result.save("result.png")
result.show()
