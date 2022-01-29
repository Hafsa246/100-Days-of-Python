# from art import logo
# print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# shift %= 25      #if the shift number is out range of alphabet

# def encrypt(text, shift):
#     cipher_text = ""
#     for i in text:
#         pos = alphabet.index(i)
#         new_pos = pos + shift
#         new_letter = alphabet[new_pos]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(text, shift):
#     cipher_text = ""
#     for i in text:
#         pos = alphabet.index(i)
#         new_pos = pos - shift
#         new_letter = alphabet[new_pos]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")

def caesar(direction, text, shift):
    cipher_text = ""
    if(direction == "decode"):
        shift *= -1
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += char
    print(f"The {direction}d text is {cipher_text}")


go = True
while go:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 25 
    caesar(direction, text, shift)

    want = input("Type 'yes' if you want to go again. otherwise type 'no'. \n")
    if want == "no":
        go = False
        print("GoodBye")
