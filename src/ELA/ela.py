from PIL import Image, ImageChops, ImageEnhance

original = Image.open("image.jpeg")
recompressed = original.copy()
recompressed.save("temp.jpeg", quality=90)

temp = Image.open("temp.jpeg")
ela = ImageChops.difference(original, temp)

enhancer = ImageEnhance.Brightness(ela)
ela = enhancer.enhance(30)

ela.show()
