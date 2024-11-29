import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "encode" or encode_or_decode == "e":
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter
        print(f"Here is the encoded result: {cipher_text}")
    elif encode_or_decode == "decode" or encode_or_decode == "d":
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter
        print(f"Here is the decoded result: {cipher_text}")
    else:
        print("Please start again with a proper direction")


while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Check if the user wants to continue
    want_to_continue = input("\nDo you want to continue? Type 'yes' or 'no': ").lower()
    if want_to_continue != "yes" or want_to_continue != "y":
        print("Goodbye!")
        break


