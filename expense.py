from PyInquirer import prompt
import csv
from csv import DictWriter

headersCSV = ['amount','label','spender','involvedUsers']

involvedUserListChoice=[]
usersList = []



def addSpenderToInvolved(spender):
    index = 0
    while involvedUserListChoice[index][1] != spender:
        index += 1
    involvedUserListChoice[index].append({"checked": True})

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"rawlist",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": usersList,
    },
    {
        "type":"checkbox",
        "message":"Select users involved",
        "name":"involvedUsers",
        "choices":involvedUserListChoice,
    },
    
]

# answers = prompt(expense_questions)



def get_user(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    for row in csvreader:
        usersList.append(row[0])
    file.close()

def builUserInvoledListChoices():
    for elm in usersList:
        involvedUserListChoice.append({"name": elm})

def new_expense(*args):
    expensefilename = 'data/expense.csv'
    usersfilename = 'data/users.csv'
    get_user(usersfilename)
    builUserInvoledListChoices()
    infos = prompt(expense_questions)
    with open(expensefilename, 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(infos)            

            f_object.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


