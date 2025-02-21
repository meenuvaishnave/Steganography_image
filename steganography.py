import cv2
import numpy as np
from PIL import Image

# Function to encode a message into an image
def encode_message(image_path, secret_message, output_image):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image file or path.")

    # Add a delimiter to mark the end of the message
    message = secret_message + "#####"  
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    data_index = 0
    rows, cols, _ = img.shape

    for row in range(rows):
        for col in range(cols):
            pixel = img[row, col]
            for channel in range(3):  
                if data_index < len(binary_message):
                    pixel[channel] = (pixel[channel] & 254) | int(binary_message[data_index])
                    data_index += 1
                else:
                    break

    cv2.imwrite(output_image, img)
    print(f"Steganographic image saved as {output_image}")

# Function to decode the message from an image
def decode_message(stego_image):
    img = cv2.imread(stego_image)
    if img is None:
        raise ValueError("Invalid stego-image file or path.")

    binary_message = ""
    rows, cols, _ = img.shape

    for row in range(rows):
        for col in range(cols):
            pixel = img[row, col]
            for channel in range(3):  
                binary_message += str(pixel[channel] & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == "#":
            break
        message += char

    print("Decoded message:", message)


# Example usage
input_image = "input_image.png"  # Ensure this image exists
output_stego_image = "stego_image.png"
hidden_message = "Hello, this is a secret!"

# Encode the message
encode_message(input_image, hidden_message, output_stego_image)

# Decode the message
decode_message(output_stego_image)