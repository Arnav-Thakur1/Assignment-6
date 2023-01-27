class Check_validity:
    def check(String_1):
        l_1= ["()","{}","[]"] 

        for brs in l_1:
            while brs in String_1:
                String_1=String_1.replace(brs,"")
        if String_1=="":
            return True
        else:
            return False    
        

String_1 = input("Enter the paranthesses string\n")

print(String_1,"is", end=" ")
if Check_validity.check(String_1):
    print("valid")
else:
    print("invalid")