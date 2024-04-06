from PIL import Image as i

im = i.open("example.jpeg")

im.rotate(180).resize((1080,1920)).save("rotated_&_resized_.jpeg")