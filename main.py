import pytesseract
from PIL import Image

# Load an image from file
img = Image.open("sample.png")

# Perform OCR
text = pytesseract.image_to_string(img)

print(text)