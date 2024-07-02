"""
Sample png output:
What do you do in the mornings? page.tsx:86
- Do you like to get up early in the morning?
- Is breakfast important?

Topic: Describe a person who likes to buy goods with low  page.tsx:93
prices. You should say:
- who this person is
what this person likes to buy
where this person likes to buy things
and explain why this person likes cheap goods
"""
import pytesseract
from PIL import Image

# Load an image from file
img = Image.open("sample.png")

# Perform OCR
text = pytesseract.image_to_string(img)

print(text)
