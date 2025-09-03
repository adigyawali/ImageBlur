"""
From an Image, do gaussian blur manually and output result
"""

from PIL import Image
import numpy as np


imageFile = "../images/OriginalImageTokyo.jpg"


def createKernel(sigma, size):
    
    # Ensures Size is odd to have a center
    if size % 2 == 0:
        raise ValueError("Kernel size must be odd")

    # Convert it into grid coordinates where the middle pixel is the origin
    offset = size//2

    # Create the Kernel
    kernel = np.zeros((size, size))

    #Iterate through each element in the kernel; ensure its a normal distrubution using normal formula
    for x in range(-offset, offset + 1):
        for y in range(-offset, offset + 1):
            # Do +offset to convert into array indices
            # Only use the normal part of the euqation, no need for the constant
            kernel[x+offset, y+offset] = np.exp(-(x**2 + y**2) / (2 * (sigma**2)))

    # Normalize the Kernel
    kernel = kernel / np.sum(kernel)

    return kernel


def convolution(kernel, imgArr):
    # Create a copy of the array so original isn't modified
    blurredArr = np.zeros(imgArr.shape)
    k = kernel.shape[0]

    # Range of the grid around the origin
    offset = k // 2 

    # Rows
    for y in range(imgArr.shape[0]):

        # Columns
        for x in range(imgArr.shape[1]):
            
            # Each color(c) in the grid
            for c in range(3):

                # Total for that pixel
                total = 0

                # Iterage over the kernel (in grid coord)
                for kernelposX in range(-offset, offset+1):
                    
                    for kernelposY in range(-offset, offset+1):
                        
                        # Current Coord of the pixel around the kernel size
                        px = x + kernelposX
                        py = y  + kernelposY

                        # Do the calculation if the pixel is actually in the image
                        if (0 <= px < imgArr.shape[1] and 0 <= py < imgArr.shape[0]):
                            total += imgArr[py, px, c] * kernel[kernelposY+offset, kernelposX+offset]

                blurredArr[y, x, c] = total

    return blurredArr


def main():
    # Size of Kernel
    size = 7

    # Sigma for the weight each pixel should have
    sigma = 3

    # Open the image and convert it to array
    img = Image.open(imageFile)
    imgArr = np.array(img)

    # Create the kernel
    kernel = createKernel(sigma, size)
    
    # Call the Convolution Function
    blurredImgArr = convolution(kernel, imgArr)

    # Shapes of the two images, Should be the same as the original
    print(f"Image Shape: {imgArr.shape}\n Blurred Image Shape: {blurredImgArr.shape}")

    # Convert the array back to an image and save the output
    blurredImgArr = np.clip(blurredImgArr, 0, 255)
    blurredImg = Image.fromarray(blurredImgArr.astype(np.uint8))
    blurredImg.save("../images/blurredImg.jpg")


if __name__ == "__main__":
    main()