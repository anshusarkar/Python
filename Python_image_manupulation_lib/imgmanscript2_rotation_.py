from PIL import Image as I

im = I.open("example.jpeg")

rotated_im = im.rotate(90)

rotated_im.save("rotated_image.jpeg")