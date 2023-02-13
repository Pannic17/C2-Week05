# Image Hash Readme

This script implements an image hashing and encryption algorithm using the Marr-Hildreth and Block Mean Hashing algorithms from the OpenCV library. The script reads an image, generates a hash using the Marr-Hildreth algorithm, and then uses this hash to hide a message within the image. The Block Mean Hash algorithm is then used to adjust the pixel values to create a "glitch" effect. The main purpose of the script is to perform the following operations:

- Hash an image using the MarrHildrethHash and BlockMeanHash functions.
- Convert the hash values to hexadecimal and binary representations.
- Convert the hash values to RGB values for use in image manipulation.
- Replace pixels in an image with ASCII characters based on the hash values.
- Glitch an image by adjusting the y-coordinate of pixels based on the hash values.

## How to use the script

The `hash_hide` function takes a path to an image as an argument and performs the following operations:

- Resizes the image to 256x256 pixels.
- Hashes the image using MarrHildrethHash.
- Converts the hash values to a hexadecimal representation.
- Replaces pixels in the image with ASCII characters based on the hash values.
- Displays the modified image using the OpenCV `imshow` function.

The `hash_glitch` function takes a path to an image as an argument and performs the following operations:

- Resizes the image to 256x256 pixels.
- Hashes the image using MarrHildrethHash and BlockMeanHash.
- Converts the hash values to a hexadecimal representation.
- Converts the hash values to RGB values.
- Adjusts the y-coordinate of pixels in the image based on the hash values.
- Displays the modified image using the OpenCV `imshow` function.

## Requirements

The following libraries are required to run the script:

- OpenCV (cv2)
- Numpy

## Code Organization

The code is organized as follows:

- Import statements for the required libraries.
- The `print_hi` function is a simple function for testing purposes.
- The `decimal2hex` function takes a list of decimal values and converts them to a hexadecimal representation.
- The `resize` function takes an image and resizes it to the specified width and height (default 256x256).
- The `convert_hash2rgb` function takes a list of decimal values and converts them to RGB values.
- The `convert_char2rgb` function takes an ASCII character and converts it to an RGB value.
- The `replace_pixel_hide` function takes an image, a string of ASCII characters, and a list of decimal values and replaces pixels in the image with ASCII characters based on the hash values.
- The `decimal2qua` function takes a list of decimal values and converts them to a 4-digit base representation.
- The `decimal2bin` function takes a list of decimal values and converts them to a binary representation.
- The `adjust_y_position` function takes an ASCII character, a 4-digit base representation, and a binary representation and returns a y-coordinate offset for use in image manipulation.
- The `get_ascii` function takes an ASCII character and returns its decimal value.
- The `hash_hide` function takes a path to an image and performs the operations described above to hide ASCII characters in the image.
