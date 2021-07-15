alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(msg,shift,action):
    """ Turn a msg into a cipher text"""
    end_msg=""
    if action == "decode":
        shift *= -1
    for letter in msg:
        if letter in alphabet:
            i=alphabet.index(letter) 
            new_i=i+shift
            end_msg += alphabet[new_i]
        else:
            end_msg += letter
    print(f"The {action}d message is: {end_msg}")

while True:
    action=input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    msg=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))
    shift=shift%26
    ceaser(msg,shift,action)
    result=input("continue?")
    if result=="no":
        print("Goodbye")
        break
