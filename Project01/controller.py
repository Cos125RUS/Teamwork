import view as v
import modul as m

def start():
    options = [find_member,position,salary,add_member,del_member,update,export_json,export_csv,exit_of_program]
    return options[v.show_menu() - 1]()


def find_member():
    return v.info(m.find_personal(v.find_peaple()))


def position():

    return 0

def salary():

    return 0



def add_member():
    res = m.new_personal(v.add_new_personal())
    return v.info(res)

def del_member():

    return 0

def update():

    return 0

def export_json():
    # передавать словарь
    return 0

def export_csv():

    return 0

def exit_of_program():

    return 0