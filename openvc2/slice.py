from PIL import Image 
Image1 = Image.open('C:\\Logs\carroseel.png') 
croppedIm = Image1.crop((130, 120, 200, 200)) 
croppedIm.show() 