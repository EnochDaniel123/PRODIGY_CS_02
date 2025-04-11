from PIL import Image

# Encrypt pixel by inverting and swapping RGB values
def encrypt_pixel(r, g, b):
    return (255 - g, 255 - b, 255 - r)

# Decrypt pixel (same logic to reverse)
def decrypt_pixel(r, g, b):
    return encrypt_pixel(r, g, b)

# Function to process image
def process_image(input_path, output_path, mode='encrypt'):
    try:
        # Open image and convert to RGB
        img = Image.open(input_path).convert('RGB')
        pixels = img.load()
        width, height = img.size

        # Loop through all pixels
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                if mode == 'encrypt':
                    pixels[x, y] = encrypt_pixel(r, g, b)
                elif mode == 'decrypt':
                    pixels[x, y] = decrypt_pixel(r, g, b)

        img.save(output_path)
        print(f"\n✅ {mode.capitalize()}ed image saved as: {output_path}")

    except FileNotFoundError:
        print("❌ Error: Input image not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# CLI interface
def main():
    print("🖼️ Pixel Manipulation - Image Encryption Tool")
    print("--------------------------------------------")
    
    mode_input = input("Choose mode - Encrypt (e) / Decrypt (d): ").strip().lower()
    
    if mode_input not in ['e', 'd']:
        print("❌ Invalid option. Please enter 'e' or 'd'.")
        return
    
    input_file = input("Enter input image filename (e.g., input.jpg): ").strip()
    output_file = input("Enter output image filename (e.g., encrypted.png): ").strip()
    
    if mode_input == 'e':
        process_image(input_file, output_file, 'encrypt')
    else:
        process_image(input_file, output_file, 'decrypt')

# Run the program
if __name__ == "__main__":
    main()
