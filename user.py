from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name",
    },
]

def add_user():
    infos = prompt(user_questions)
    # This function should create a new user, asking for its name
    print(infos)
    print("User added !")
    return True