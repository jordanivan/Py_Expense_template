from PyInquirer import prompt
import csv
from csv import DictWriter

headersCSV = ['amount','label','spender']      

usersList = []
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
        "choices": usersList
    },

]

def get_user(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    for row in csvreader:
        usersList.append(row[0])
    print(usersList)
    file.close()

def new_expense(*args):
    expensefilename = 'data/expense.csv'
    usersfilename = 'data/users.csv'
    get_user(usersfilename)
    infos = prompt(expense_questions)
    with open(expensefilename, 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(infos)            

            f_object.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


