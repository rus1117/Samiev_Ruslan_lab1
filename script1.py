def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        elif 'A' <= char <= 'Z':
            start = ord('A')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        elif 'а' <= char <= 'я':
            start = ord('а')
            result.append(chr((ord(char) - start + shift) % 32 + start))
        elif 'А' <= char <= 'Я':
            start = ord('А')
            result.append(chr((ord(char) - start + shift) % 32 + start))
        elif char in 'ёЁ':
            base = 'е' if char == 'ё' else 'Е'
            start = ord(base)
            result.append(chr((ord(base) - start + shift) % 32 + start))
        else:
            result.append(char)
    return "".join(result)

text = input("Введите текст: ")
shift = int(input("Введите величину сдвига: "))

encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, shift, decrypt=True)

print(f"Зашифрованный текст: {encrypted}")
print(f"Расшифрованный текст: {decrypted}")
