from PIL import Image, ImageChops
import imagehash

img1 = imagehash.average_hash(Image.open("6.png"))
img2 = imagehash.average_hash(Image.open("7.png"))
cutoff = 5 

if img1 - img2 < cutoff:
    print("Weapons is similar")
else:
    print("Weapons is not similar")