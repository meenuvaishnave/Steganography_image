Image Steganography Using Python

This project demonstrates a simple method to hide and extract secret messages within an image using steganography. The technique used is called Least Significant Bit (LSB) encoding, which allows you to embed binary data (your secret message) into the image pixels without noticeable changes.

Features
	•	Encoding: Hide a secret message inside an image.
	•	Decoding: Retrieve the hidden message from the image.
	•	Command-Line Interface: Simple script-based interaction.

Technologies Used
	•	Python 3
	•	OpenCV (cv2): For reading, processing, and saving images.
	•	NumPy: For array manipulations (handling pixel data).
	•	Pillow (PIL): For additional image handling (if needed).

How It Works
	1.	Encoding Process:
	•	Reading the Image: The script reads an input image from a given file path.
	•	Message Preparation: The secret message is appended with a delimiter "#####" to mark its end, then each character is converted into its 8-bit binary representation.
	•	Embedding the Message: The binary data is embedded into the image by modifying the least significant bit (LSB) of each pixel’s color channels (Red, Green, Blue). This tiny change does not affect the overall appearance of the image.
	•	Saving the Image: The modified image, now containing the hidden message, is saved as a new file.
	2.	Decoding Process:
	•	Reading the Stego-Image: The script opens the image with the hidden message.
	•	Extracting the Message: It reads the last bit from each pixel’s color channel, reconstructing the binary data.
	•	Converting to Text: The binary data is split into 8-bit chunks and converted back into text characters. The process stops when the delimiter is encountered.

Installation and Usage

Prerequisites
	•	Python 3.x installed on your system.
	•	Required Python libraries:

pip install opencv-python numpy pillow



How to Run the Code
	1.	Clone the Repository:

git clone https://github.com/yourusername/Steganography_image.git


	2.	Navigate to the Project Directory:

cd Steganography_image


	3.	Prepare Your Image:
	•	Place your input image in the project folder.
	•	Rename it to input_image.png (or update the code with your file name).
	4.	Run the Script:
	•	Open steganography.py and modify the hidden_message variable if desired.
	•	Execute the script:

python steganography.py


	5.	Output:
	•	The script creates an image called stego_image.png that contains the hidden message.
	•	It also decodes the message from the image and prints it to the console.

License

This project is open source and available under the MIT License.

Acknowledgements
	•	Thanks to the developers and communities behind OpenCV, NumPy, and Pillow for providing such powerful libraries.
	•	Inspiration from various online steganography tutorials and projects.
