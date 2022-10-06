# Import libraries
from PIL import Image
import pytesseract
import glob
import os

pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"

def magic(image, lang):
            print(image)
            text = pytesseract.image_to_string(image,lang=lang)
            return(text)

def get_text(lang):
    all_text = []
    images = glob.glob('photos/*.jpg')

    for im in images:
        image = Image.open(im)
        image.save(im[:-3] + 'png')
        image = Image.open(im[:-3] + 'png')
        all_text.append(magic(image, lang))
    
    images = glob.glob('photos/*')
    for f in images:
        os.remove(f)

    return ' '.join(all_text)
    
        
    