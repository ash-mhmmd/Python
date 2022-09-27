from cipherlogo import logo

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(message, shift_amount, mode):
    end_text = ""
    if mode == "decode":
        shift_amount *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + (shift_amount)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {mode}d message is: {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(message=text, shift_amount=shift, mode=direction)

    next_step = input("Run again? Type 'yes' or 'no'.\n")
    if next_step == "no":
        should_continue = False
        print("Goodbye.")
