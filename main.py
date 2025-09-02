"""
From an Image, do gaussian blur manually and output result
"""

from PIL import Image
import numpy as np


imageFile = "tokyoimg.jpg"

def main():
    img = Image.open(imageFile)
    arr = np.array(img)

    #Check the image shape

    print(f"Image Shape: {arr.shape}")



if __name__ == "__main__":
    main()