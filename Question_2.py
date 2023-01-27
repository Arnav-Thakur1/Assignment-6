def check_pallindrome():
    String_1=input("Enter the string you want to check for pallindrome\n")
    revversed_string="".join(reversed(String_1))                                         
    if String_1==revversed_string:                                                      
        print("Yes\n")
    else:
        print("No\n")

while True:
    check_pallindrome()