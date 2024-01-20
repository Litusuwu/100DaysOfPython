def encrypt(text, shift, operation):
    strin = ""
    for i in text:
        if i not in alphabet: 
            strin += i
            continue
            
        if(alphabet.index(i) + shift >= len(alphabet)):
            strin += alphabet[alphabet.index(i)+shift - len(alphabet)]
        else:
            strin += alphabet[alphabet.index(i)+shift]
    print(f"Here's the {operation}d result: {strin}")

def decrypt(text, shift, operation):
    strin = ""
    for i in text:
        if i not in alphabet: 
            strin += i
            continue
            
        strin += alphabet[alphabet.index(i)-shift]
    print(f"Here's the {operation}d result: {strin}")

def caesar(start_text, shift_amount, operation):
    if operation == "decode":
        decrypt(start_text, shift_amount, operation)
    elif operation == "encode":
        encrypt(start_text, shift_amount, operation)
    else:
        print("Incorrect direction.")
   


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


caesar(text, shift, direction)
