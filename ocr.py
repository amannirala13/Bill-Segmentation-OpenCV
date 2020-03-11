# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 02:41:52 2020

@author: amann
"""

from PIL import Image
import pytesseract
text = pytesseract.image_to_boxes(Image.open('C:/Users/amann/Desktop/test.jpg'),lang='eng')