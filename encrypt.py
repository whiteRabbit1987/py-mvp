import random, string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars: {chars}\nkey: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
chiper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    chiper_text += key[index]

print(f"\n*********************************"
      f"\nOriginal message: {plain_text}"
      f"\nEncrypted message: {chiper_text}"
      f"\n*********************************")


#DECRYPT
chiper_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"\n*********************************"
      f"\nEncrypted message: {chiper_text}"
      f"\nOriginal message: {plain_text}"
      f"\n*********************************")