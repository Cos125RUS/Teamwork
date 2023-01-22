import csv
def find_personal(key):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                name, surname, position, salary = i.split(';')
                return f'{name} {surname}\n{position}\n{salary}'
            else:
                return 'Not found'

def new_personal(card):
    name, surname, position, salary = card
    with open('members.cvs', 'a') as data:
        member = f'{name};{surname};{position};{salary}\n'
        data.write(member)
    return 'New member was create'




def export_csv(dict_data):
    with open('data_json.csv', 'w') as csvfile:
        fieldnames = ['name', 'surname', 'position', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(dict_data)

