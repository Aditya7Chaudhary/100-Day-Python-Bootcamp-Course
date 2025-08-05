command = input("Do you want to decode or encode it : ")
msg = input(f"Enter the msg you want to {command} : ")
shift = int(input("Enter the shift : "))

def decoder_encoder(msg,command,shift):
    ans = ""
    if command=="encode":
        for i in msg:
            ans = ans + chr(ord(i)+shift)
    elif command=="decode":
        for i in msg:
            ans = ans + chr(ord(i)-shift)

    print(f"The final message is {ans}")
    choice = input("Are you fine with this? (Y/N) : ")
    if choice in ("Y","y"):
        return
    elif choice == ("N","n"):
        command = input("Do you want to decode or encode it : ")
        shift = int(input("Enter the shift : "))
        decoder_encoder(msg,command,shift)


decoder_encoder(msg,command,shift)

