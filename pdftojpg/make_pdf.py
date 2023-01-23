from PIL import Image

def rotate_img(img):
    im = Image.open(img)
    width = im.size[0] 
    height = im.size[1]
    if width > height:
        im_rotate = im.rotate(90, expand=True)
        im_rotate.save(img)
        im.close()


rotate_img('test.jpg')
