#_*_ coding: utf-8 _*_
import pytesseract
from PIL import Image

image = Image.open("E:/imooc1.png")
text = pytesseract.image_to_string(image)
print(text)