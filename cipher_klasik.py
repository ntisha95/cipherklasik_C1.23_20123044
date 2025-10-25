# Program Caesar Cipher
# Fitur: Enkripsi, Dekripsi, dan Simpan hasil ke file .txt
# Dibuat untuk Tugas Mini - Cipher Klasik

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            if mode == 'encrypt':
                result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            elif mode == 'decrypt':
                result += chr((ord(char) - ord(base) - shift) % 26 + ord(base))
        else:
            result += char
    return result

def main():
    print("=== Program Cipher Klasik (Caesar Cipher) ===")
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan nilai shift (misal 3): "))

    encrypted = caesar_cipher(text, shift, 'encrypt')
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')

    print("\nHasil Enkripsi:", encrypted)
    print("Hasil Dekripsi:", decrypted)

    # Simpan ke file .txt
    with open("hasil_cipher.txt", "w") as file:
        file.write("=== Hasil Caesar Cipher ===\n")
        file.write(f"Teks asli     : {text}\n")
        file.write(f"Hasil enkripsi: {encrypted}\n")
        file.write(f"Hasil dekripsi: {decrypted}\n")

    print("\nHasil telah disimpan di file 'hasil_cipher.txt'.")

if __name__ == "__main__":
    main()
