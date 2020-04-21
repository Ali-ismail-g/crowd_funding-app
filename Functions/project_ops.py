import datetime
project_details = {}
def create_project():
    print("*****you can create a project fund raise campaign*****\n")
    title = input("please enter the title of the project: ")
    project_details["title"] = title
    
    details = input("please enter a details about the project: ")
    project_details["details"] = details
    
    total_target = input("please enter the target of the campaign: ")
    project_details["total_target"] = total_target
    
    start_date = input("please enter the start date of the project(dd/mm/yy): ")
    day,month,year = start_date.split('/')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
        project_details["start_date"] = start_date
    except ValueError :
        isValidDate = False

    end_date = input("please enter the end date of the project(dd/mm/yy): ")
    day,month,year = end_date.split('/')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
        project_details["end_date"] = end_date
    except ValueError :
        isValidDate = False
    
    if project_details:
        with open('project.txt','a') as f:
            f.write(str(project_details)+"\n")
            print("Welcome to Crowd-Funding App")   
    else:
        print("there must be an error with the file")



def show_project():
    with open('project.txt', 'r') as r:
        for line in r:
            project = eval(line)
            for key,value in project.items():
                print(key+":"+value)
            # print(eval(line))
            # print(type(eval(line)))

def edit_project():
    title_index = int(input("please enter the number of line you want to edit: "))
    with open('project.txt', 'r') as r:
        lines = r.readlines()
        print(lines)
        with open("project.txt", "w") as r:
            for i in lines:
                if i == title_index:
                    lines.pop(i)
                    r.write(lines)
                create_project()
                print("project has been updated")
    # with open("project.txt", "w") as r:
    #     for line in lines:
    #         if line.strip("\n") != title_edit:
    #             print(line)
    #             r.write(line)

                # print("done")
            #         with open('project.txt','a') as f:
            #             f.write(str(project_details)+"\n")
            #         create_project()

def delete_project():
    deleted_index = int(input("please enter the number of line you want to delete: "))
    with open('project.txt', 'r') as r:
        lines = r.readlines()
        print(lines)
        with open("project.txt", "w") as r:
            for i in lines:
                if i == deleted_index:
                    lines.pop(i)
                    r.write(lines)
                print("project has been deleted")