def calculator(l):
    i = 1
    while i < len(l):
        while "/" in l:
            a = int(l.pop(l.index("/")-1))/int(l.pop(l.index("/")+1))
            l[l.index("/")] = a
        while "*" in l:
            a = int(l.pop(l.index("*")-1))*int(l.pop(l.index("*")+1))
            l[l.index("*")] = a
        while "+" in l:
            a = int(l.pop(l.index("+")-1))+int(l.pop(l.index("+")+1))
            l[l.index("+")] = a
        while "-" in l:
            a = int(l.pop(l.index("-")-1))-int(l.pop(l.index("-")+1))
            l[l.index("-")] = a

        print(f"The answer is : {l[0]}")
        ch = input("Do you want to continue with the calculation (Y/N)? : ")

        if ch in ["Y","y"]:
            s = input(f"Enter the calculation you want to make (Kindly enter space between characters) :\n{l[0]}")
            l1 = s.split(" ")
            l1.insert(0,str(l[0]))
            l1.pop(1)
            calculator(l1)
        else:
            return


s = input("Enter the calculation you want to make (Kindly enter space between characters) :\n")
l = s.split(" ")

calculator(l)