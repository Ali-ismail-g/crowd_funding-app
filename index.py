
from Functions import register,project_ops 


print("**Welcome to Crowd-Funding App**")
print("************************************************\n")
print("**If you are a new member please signup and if you are not please Login**")

user = input("please select one of the options login or signup: ")

if user == "login":
    register.login()
    print("**Welcome to Crowd-Funding App**")
    project = input("what do you want to do create , show , delete , edit: ")
    if project == "create":
        project_ops.create_project()
    elif project == "show":
        project_ops.show_project()
    elif project == "edit":
        project_ops.edit_project()
    elif project == "delete":
        project_ops.delete_project()    
    
elif user == "signup":
    register.signup()
    print("**Welcome to Crowd-Funding App**")
    project = input("what do you want to do create , show , delete , edit: ")
    if project == "create":
        project_ops.create_project()
    elif project == "show":
        project_ops.show_project()
    elif project == "edit":
        project_ops.edit_project()
    elif project == "delete":
        project_ops.delete_project()