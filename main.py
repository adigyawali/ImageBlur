"""
From an Image, do gaussian blur manually and output result
"""

from PIL import Image
import numpy as np


imageFile = "tokyoimg.jpg"


def createKernel(sigma, size):
    # Determine the kernel Size
    kernelSize = size//2 # Ensures Size is odd to have a center

    # Create the Kernel
    kernel = np.zeros(kernelSize, kernelSize)

    #Iterate through each element in the kernel; ensure its a normal distrubution using normal formula
    # Do -kernelSize to kernelSize + 1 to convert it into grid coordinates where the middle pixel is the origin
        # - Required for Gaussain Formula
    for x in range(-kernelSize, kernelSize + 1):
        for y in range(-kernelSize, kernelSize + 1):
            # Do +kernelSize to convert into array indices
            # Only use the normal part of the euqation, no need for the constant
            kernel[x+kernelSize, y+kernelSize] = np.exp(-(x**2 + y**2) / (2 * (sigma**2)))

    # Normalize the Kernel
    kernel = kernel / np.sum(kernel)

    return kernel


def convolution(kernel, imgArr):
    # Create a copy of the array so original isn't modified
    blurredArr = np.zeros(imgArr.shape)
    kernelShape = kernel.shape

    # Rows
    for x in range(imgArr.shape[0]):

        # Columns
        for y in range(imgArr.shape[1]):
            
            # Each color(c) in the grid
            for c in range(3):

                # Total for that pixel
                total = 0

                # Iterage over the kernel (in grid coord)



def main():
    # Size of Kernel
    size = 3

    # Sigma for the weight each pixel should have
    sigma = 1

    # Open the image and convert it to array
    img = Image.open(imageFile)
    imgArr = np.array(img)

    # Create the kernel
    kernel = createKernel(sigma, size)
    
    # Call the Convolution Function
    blurredImgArr = convolution(kernel, imgArr)

    # Shapes of the two images
    print(f"Image Shape: {imgArr.shape}\n Blurred Image Shape: {blurredImgArr.shape}")

    # Should be the same as the original
    blurredImg = Image.fromarray(blurredImgArr)
    blurredImg.save("output.jpg")

if __name__ == "__main__":
    main()