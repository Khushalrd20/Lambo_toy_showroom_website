from PIL import Image 
def main():
 try: 
#Relative Path 
  img = Image.open("685721.png") 
#Angle given 
  img = img.rotate(180) 
#Saved in the same relative location 
  img.save("rotated_picture.jpg")
  width, height = img.size 
  area = (0, 0, width/2, height/2) 
  img = img.crop(area) 
#Saved in the same relative location 
  img.save("cropped_picture.jpg") 
# Relative Path 
  width, height = img.size 
  img = img.resize((width/2, height/2)) 
# Saved in the same relative location 
  img.save("resized_picture.jpg") 
 except IOError: 
  pass 
if __name__ == "__main__": 
 main()