def check_panagram():
    String_1=input("Enter the string you want to check for panagram\n")
    is_it_panagram=True
    String_1=String_1.lower()
    String_1=String_1.upper()
    for i in range(65,91):
        if chr(i) not in String_1:
            is_it_panagram=False

    if is_it_panagram==True:
        print("The entered string is a panagram\n")
    else:
        print("The entered string is not a panagram\n")

while True:
    check_panagram()
