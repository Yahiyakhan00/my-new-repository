import cv2 # type: ignore
import numpy as np # type: ignore

def pixel_encrypt(image_path, key):
    print(f"Encrypting {image_path} with key {key}...")  # Debugging line
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if image is None:
        raise ValueError("Invalid image path or image not found.")
    
    key_array = np.full_like(image, key, dtype=np.uint8)
    encrypted = cv2.bitwise_xor(image, key_array)
    
    cv2.imwrite('encrypted_image.png', encrypted)
    print("Encryption complete. Saved as 'encrypted_image.png'")
    return 'Image encrypted and saved as encrypted_image.png'

def pixel_decrypt(image_path, key):
    return pixel_encrypt(image_path, key)
