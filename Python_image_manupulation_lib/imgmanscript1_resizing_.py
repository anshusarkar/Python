from PIL import Image 

im = Image.open("/home/zero/Python/Python_image_manupulation_lib/example.jpeg")

resized_image = im.resize((1920, 1080))

resized_image.save("/home/zero/Python/Python_image_manupulation_lib/resized_image.jpeg")