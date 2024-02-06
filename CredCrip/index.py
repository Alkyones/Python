from PIL import Image
import numpy as np
import sys, os
def getParams():
    method = ''
    key = 0
    while method != 'encrypt' and method != 'decrypt':
        method = input("Enter the method (encrypt/decrypt):")

    while key < 1 or key > 25:
        key = int(input("Enter the key (1-25):"))
    return method, key

def getImagePath(imagesInFolder):
    imagesInFolder = os.listdir(path="./Images")
    imageKeys = {}
    if len(imagesInFolder) != 0:
        imagesInFolder = [(i+1, image) for i, image in enumerate(imagesInFolder)]
        for i, image in imagesInFolder:
            imageKeys[i] = image
    return imageKeys


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
    new_image.save(image_path)
    print("Encryption successful. Encrypted image saved as", image_path)
    return image_path


def decrypt_text_from_image(encrypted_image_path, key):
    image = Image.open(encrypted_image_path).convert("RGB")
    pixels = np.array(image)
    flat_pixels = pixels.reshape(-1, 3)
    binary_text = ''.join([format((pixel & 1), 'b') for pixel in flat_pixels.flatten()])
    decrypted_text = ""
    for i in range(0, len(binary_text), 8):
        decrypted_text += chr(int(binary_text[i:i+8], 2))
    decrypted_text = encrypt_text(decrypted_text, -key)
    
    with open("./data/output.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    print("Decryption successful. Decrypted text saved as output.txt")
    return True    







if __name__ == "__main__":
    method, key = getParams()
    imageKeys = getImagePath(os.listdir(path="./Images"))
    if(len(imageKeys) == 0):
        print("No images found in the Images folder.")
        sys.exit()
    else:
        print("Images found in the Images folder:")
        for i, image in imageKeys.items():
            print(i, image)

    image_path_key = 0
    while image_path_key not in imageKeys.keys():
        image_path_key = int(input(f"Enter the image number ({len(imageKeys)}):"))
    image_path = "./Images/" + imageKeys[image_path_key]

    with open("./data/data.txt", "r") as f:
        secret_message = f.read()
    
    
    if method == "encrypt":
        encrypted_image_path = encrypt_text_to_image(image_path, secret_message, key)
    elif method == "decrypt":
        decrypted_text = decrypt_text_from_image(image_path, key)
