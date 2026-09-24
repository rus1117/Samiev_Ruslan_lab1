text = input("Введите текст для шифрования: ")
shift = int(input("Введите величину сдвига: "))

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

encrypted_text = "".join(result)
print(f"Зашифрованный текст: {encrypted_text}")