from math import log10, sqrt
import cv2
import numpy as np

# Import per SSIM
import skimage


def PSNR(original, compressed):  # Peak signal-to-noise ratio
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):  # MSE a 0 indica che non c'è rumore
        return 100  # Quindi la qualità è 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def MSE(original, compressed):  # Mean Squared Error
    mse = np.square(np.subtract(original, compressed)).mean()
    return mse


def SSIM(original, compressed): # Structural similarity index
    # Conversione dell'immagine in scala di grigi
    originalGray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    compressedGray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)

    ssim = skimage.metrics.structural_similarity(originalGray, compressedGray,
                                                  gaussian_weights=True, sigma=1.5,
                                                  use_sample_covariance=False, data_range=255)
    if ssim == 1.0:
        print("I frame forniti sono uguali")
    return ssim


def main():
    original = cv2.imread("Resources/FramesControlLocale/frame72.jpg")  # Immagine non compressa
    compressed = cv2.imread("Resources/5MBControlStadia/frame7.jpg", 1)  # Immagine compressa

    valuePSNR = PSNR(original, compressed)
    valueMSE = MSE(original, compressed)
    valueSSIM = SSIM(original, compressed)

    print("PSNR: ", valuePSNR)
    print("MSE: ", valueMSE)
    print("SSIM: ", valueSSIM)
                                                                TEMPO CHE INTERCORRE TRA OGNI FRAME 16.6ms

if __name__ == "__main__":
    main()
