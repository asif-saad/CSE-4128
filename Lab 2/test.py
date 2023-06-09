import cv2
import numpy as np

def bilateral_filter(img, d, sigma_color, sigma_space):
    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a Gaussian kernel for spatial filtering
    kernel_space = cv2.getGaussianKernel(d, sigma_space)
    kernel_space = kernel_space * kernel_space.T

    # Initialize the filtered image
    filtered_img = np.zeros_like(img_gray)

    # Iterate over each pixel in the image
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]):
            # Define the local region around the pixel
            i_min = max(0, i - d//2)
            i_max = min(img_gray.shape[0] - 1, i + d//2)
            j_min = max(0, j - d//2)
            j_max = min(img_gray.shape[1] - 1, j + d//2)

            # Extract the local region and compute the Gaussian weights
            local_region = img_gray[i_min:i_max+1, j_min:j_max+1]
            kernel_color = np.exp(-np.square(local_region - img_gray[i,j]) / (2 * np.square(sigma_color)))
            weights = kernel_color * kernel_space[(i_min-i+ d//2):(i_max-i+ d//2+1), (j_min-j+ d//2):(j_max-j+ d//2+1)]

            # Normalize the weights and compute the filtered value
            weights /= np.sum(weights)
            filtered_img[i,j] = np.sum(weights * local_region)

    return filtered_img