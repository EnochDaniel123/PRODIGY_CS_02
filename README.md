# PRODIGY_CS_02
Pixel Manipulation for Image Encryption
# 1. Introduction
In an era where digital images are frequently shared and stored online, protecting them from unauthorized access is essential. This project presents a basic image encryption and decryption tool using pixel manipulation techniques. By altering the pixel values mathematically, we can securely transform an image into an encrypted version, and then retrieve the original using a reverse operation.
# 2. Objective
- Develop a Python-based program that performs pixel-level encryption.
- Apply simple yet effective pixel manipulation operations.
- Enable both encryption and decryption of images using the same technique.
# 3. Tools & Technologies Used
Tool/Library	Purpose
Python	Programming language
Pillow (PIL)	For image loading and manipulation
Visual Studio Code	Code editor used for development
# 4. Methodology
This project performs image encryption by mathematically manipulating pixel values. The RGB values of each pixel are processed using the following approach:

🔐 Encryption Logic:
For each pixel (R, G, B):
Apply the operation: (255 - G, 255 - B, 255 - R)
This reverses the values and swaps the channels, making the image unrecognizable.

🔓 Decryption Logic:
Apply the same function again, because it’s reversible.
# 5. Implementation
Here is the simplified code used for the project:

from PIL import Image

def encrypt_pixel(r, g, b):
    return (255 - g, 255 - b, 255 - r)

def decrypt_pixel(r, g, b):
    return encrypt_pixel(r, g, b)  # Same function used twice

def process_image(input_path, output_path, mode='encrypt'):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if mode == 'encrypt':
                pixels[x, y] = encrypt_pixel(r, g, b)
            elif mode == 'decrypt':
                pixels[x, y] = decrypt_pixel(r, g, b)

    img.save(output_path)
    print(f"{mode.capitalize()}ed image saved to: {output_path}")

# 6. Output
- The encrypted image looks completely altered and cannot be understood visually.
- Decrypting it restores the original image.
- Encrypted and decrypted images are saved separately.
# 7. Results
Action	Output File
Encryption	encrypted.jpg
Decryption	decrypted.jpg
# 8. Conclusion
This project demonstrates a basic yet effective method of image encryption using pixel manipulation. It introduces the concept of image-level security and can serve as a foundation for more advanced encryption techniques in the future.
# 9. Future Enhancements
- Add password-based encryption logic.
- Use more advanced encryption algorithms (e.g., AES).
- Implement a GUI for ease of use.
# 10. Acknowledgement
I would like to thank Prodigy InfoTech for the opportunity to apply practical programming skills through this internship project. This assignment has strengthened my understanding of image processing and encryption fundamen

