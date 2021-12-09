from math import log10, sqrt
import cv2
import numpy as np


def PSNR(original, compressed): #Peak signal-to-noise ratio
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE a 0 indica che non c'è rumore
        return 100 # Quindi la qualità è 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def MSE(original, compressed): #Mean Squared Error
    mse = np.square(np.subtract(original, compressed)).mean()
    return mse

def main():
    original = cv2.imread("original_image.png") # Immagine non compressa
    compressed = cv2.imread("compressed_image.png", 1) # Immagine compressa
    value = PSNR(original, compressed)
    print(f"PSNR: {value} dB")


if __name__ == "__main__":
    main()