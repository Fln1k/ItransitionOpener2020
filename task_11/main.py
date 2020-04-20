from PIL import Image

image = Image.open("photo.png")
img = image.load()
width = image.size[0]
height = image.size[1]
f = open("guru99.txt", "w+")
for x in range(width):
    for y in range(height):
        print(img[x, y])
        f.write(f"{img[x, y]} ".replace("(", "").replace(")", "").replace(",", " "))
