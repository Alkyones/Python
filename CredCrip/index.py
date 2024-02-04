from PIL import Image
import numpy as np

def encrypt_text(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text_to_image(image_path, text, key):
    image = Image.open(image_path).convert("RGB")
    encrypted_text = encrypt_text(text, key)
    binary_text = ''.join(format(ord(char), '08b') for char in encrypted_text)
    pixels = list(image.getdata())
    new_pixels = []
    binary_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if binary_index < len(binary_text):
                new_pixel[i] = int(bin(pixel[i])[2:9] + binary_text[binary_index], 2)
                binary_index += 1
        new_pixels.append(tuple(new_pixel))
    new_image = Image.new("RGB", image.size)
    new_image.putdata(new_pixels)
    encrypted_image_path = "change"
    new_image.save(encrypted_image_path)
    print("Encryption successful. Encrypted image saved as", encrypted_image_path)
    return encrypted_image_path


def decrypt_text_from_image(encrypted_image_path, key):
    image = Image.open(encrypted_image_path).convert("RGB")
    pixels = np.array(image)
    flat_pixels = pixels.reshape(-1, 3)
    binary_text = ''.join([format((pixel & 1), 'b') for pixel in flat_pixels.flatten()])
    decrypted_text = ""
    for i in range(0, len(binary_text), 8):
        decrypted_text += chr(int(binary_text[i:i+8], 2))
    decrypted_text = encrypt_text(decrypted_text, -key)
    return decrypted_text

# Example usage
image_path = "change it"
text_to_encrypt = "This is a secret message!"
encryption_key = 3

encrypted_image_path = encrypt_text_to_image(image_path, text_to_encrypt, encryption_key)
print("Encrypted Image Path:", encrypted_image_path)

decrypted_text = decrypt_text_from_image(encrypted_image_path, encryption_key)
print("Decrypted Text:", decrypted_text)
