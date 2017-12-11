

password= "assignment"

def word(value):
    if(value == password):
        print("Password match")
    else:
        print("Wrong password")


value=input("Enter the password: ")
word(value)
