from PyInquirer import prompt
from csv import DictWriter

headersCSV = ['Name']      

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name",
    },
]

def add_user():
    infos = prompt(user_questions)
    with open('data/users.csv', 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(infos)            

            f_object.close()
    # This function should create a new user, asking for its name
    print("User added !")
    return True