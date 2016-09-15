from PIL import Image
im=Image.open('iam1p.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((50,50))
im.save('thumb.jpg','JPEG')