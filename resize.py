import os
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
import random

src= "D:\\data\\images\\genre-painting"


#Set your own PATH 
dst = "D:\\data\\genre-painting"

i=1

for filename in os.listdir(src):

    path = os.path.join(src, filename)
    
    out = os.path.join(dst, filename+".png")
    
    image = Image.open(path)
    image.resize((64, 64)).convert('RGB').save(out)
    
    try:
        image.load()
    except IOError:
        pass
    
    