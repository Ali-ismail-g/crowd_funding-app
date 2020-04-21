import re

valid_inputs = {}
def signup():
    print("*********Registeration*********")
    first_name = input("please enter your first name: ")
    if first_name.isalpha():
        valid_inputs["first_name"] = first_name  
    else:
        print("rewrite your name")
        first_name = input("please enter your first name: ")
    
    last_name = input("please enter your last name: ")
    if first_name.isalpha():
        valid_inputs["last_name"] = last_name
    else:
        print("rewrite your name")
        last_name = input("please enter your last name: ")
    
    password = input("please enter your password at least 4 chars: ")
    if len(password) < 4: 
        print('length should be at least 4')
        password = input("please enter your password at least 4 chars: ")
    else:
        valid_inputs["password"] = password
    
    confirm_password = input("please confirm your password: ")
    if password == confirm_password:
        valid_inputs["confirm_password"] = confirm_password
    else:
        print("password wasn't confirmed")
        confirm_password = input("please confirm your password: ")  
    
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    email = input("please enter your email: ")
    if re.search(regex,email):
        valid_inputs["email"] = email 
    else:
        print("not valid email")
        email = input("please enter your email: ")
    
    mob_reg = "(01)[0-9]{9}"
    mobile_phone = input("please enter your mobile_phone: ")
    if re.search(mob_reg,mobile_phone):
        print("mobile phone valid")
        valid_inputs["mobile_phone"] = mobile_phone
    else:
        print("mob phone not valid")
        mobile_phone = input("please enter your mobile_phone: ")
    
    if valid_inputs:
        with open('register.txt','a') as f:
            f.write(str(valid_inputs)+"\n")
            print("Welcome to Crowd-Funding App")   
    else:
        print("there must be an error with the file")
    
    
def login():
    email = input("please enter your email: ")
    password = input("please enter your password: ")
    with open('register.txt', 'r') as r:
        for line in r:
            if line.find(email) and line.find(password):
                print("Hello")              
            else:
                # print(email,password)
                print("I am sorry but you are not a member")
                signup()
    
    

