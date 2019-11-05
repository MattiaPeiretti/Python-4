#Mattia Peiretti, Sep 2019, stardate: -303334.24, https://mattiapeiretti.com

import os
import json
import random
from random import randint


CHECK_WORDLIST = 'v'
ADD_TO_WORDLIST = 'a'
DELETE_WORDLIST = 'd'
SELECT_WORDLIST = 's'
NEW_WORDLIST = 'n'
ESCAPE = 'q'

WORDLISTS_FILE_DIR = 'wordlists/'

MENU_WIDTH = 60

### DICTIONARIES STUFF :)

#write_json({'src':'sedede'}, 'test')
def write_json(data, filename, filepath=WORDLISTS_FILE_DIR):
    with open(filepath + filename + '.json', 'w', encoding='utf8') as outfile:
        json_str = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(str(json_str))

def load_file(filename, dir = WORDLISTS_FILE_DIR):
    with open(dir+filename) as data_file:
        data_loaded = json.load(data_file)
        return data_loaded
        
def write_dictionary_file(dict_data, dict_name, dir=WORDLISTS_FILE_DIR):
    with open(dir + dict_name + '.json', 'w', encoding='utf8') as data_file:
        json_data = json.dumps(dict_data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        data_file.write(str(json_data))

def list_wordlists_files(dir=WORDLISTS_FILE_DIR):
    files = []
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            files.append(filename)
    if not files:
        return
    return files

def print_wordlists_list_names(list_):
    print('\n')
    for x in range(len(list_)):
        print(list_[x][0:len(list_[x])-5])
    print('\n')
        
def get_dict_lang(dict_name):
    pos = dict_name.find('2')
    lang_a = dict_name[0:pos]
    lang_b = dict_name[(pos + 1):len(dict_name)]
    return (lang_a, lang_b) 
    

### MENU STUFF 

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_menu_line(text, menu_width):
    space = ' ' * int(menu_width / 10)
    line = '║' + ('{:' + str((menu_width - 2)) + '}').format(space + text) + '║\n'
    return line

def generate_main_menu(current_dictionary):
    if current_dictionary == '':
        current_dictionary = 'No wordlist selected!' 
    cls()
    blank_line =  '║' + ' '*(MENU_WIDTH-2) + '║\n'
    menu = '╔' + '═'*(MENU_WIDTH - 2) + '╗\n'
    menu += blank_line
    menu += generate_menu_line(CHECK_WORDLIST + ' - ' + 'View the selected wordlist', MENU_WIDTH)
    menu += generate_menu_line(ADD_TO_WORDLIST + ' - ' + 'Add item to wordlist', MENU_WIDTH)
    menu += generate_menu_line(DELETE_WORDLIST + ' - ' + 'Delete wordlist', MENU_WIDTH)
    menu += generate_menu_line(SELECT_WORDLIST + ' - ' + 'Select wordlist', MENU_WIDTH)
    menu += generate_menu_line(NEW_WORDLIST + ' - ' + 'Create new wordlist', MENU_WIDTH)
    menu += generate_menu_line(ESCAPE + ' - ' + 'Save and quit the program', MENU_WIDTH)
    menu += blank_line
    menu += generate_menu_line('Selected Wordlist: ' + current_dictionary, MENU_WIDTH)
    menu += blank_line
    menu += '╚' + '═'*(MENU_WIDTH - 2) + '╝\n'
    return menu

### MAIN FUNCTIONS


def check_wordlist(current_dict, main_dict):
    while True:
        current_word = random.choice(list(main_dict.keys()))

        print(current_word)

        _, lang_b = get_dict_lang(current_dict)
        inp = input('Enter the transaltion to ' + lang_b + ': ')

        if inp.lower() == main_dict[current_word]:
            print('im proud of ya son')
            input()
        elif inp == ESCAPE:
            break

def add_to_wordlist(current_dict, main_dict):
    if current_dict:
        lang_a, lang_b = get_dict_lang(current_dict)
        word_a = input('Insert word in {}:'.format(lang_a))
        word_b = input('Insert word in {}:'.format(lang_b))
        main_dict[word_a.lower()] = word_b.lower()
        return True
    return -1

def select_wordlist(current_dict, main_dict):
    if not current_dict == "":
        write_dictionary_file(main_dict, current_dict)

    files = list_wordlists_files()

    print_wordlists_list_names(files)

    inp = input('Enter name: ')
    if inp:
        if inp+'.json' in files:
            print('Found!')
            current_dict = inp
            main_dict = load_file(inp+'.json')
    return current_dict, main_dict

def delete_wordlists():
    files = list_wordlists_files()

    print_wordlists_list_names(files)
    confirmation_num = randint(100, 999)

    file_name = input('Enter name: ')
    if file_name:
        if file_name.lower()+'.json' in files:
            print('\nTo confirm, type the following number and press ENTER.\n\n           {}\n\nq. To cancel\n'.format(confirmation_num))
            inp = input('Confirm: ')
            if int(inp) == confirmation_num:
                os.remove(WORDLISTS_FILE_DIR + file_name+'.json')
                
            elif inp == 'q':
                return

            else:
                print('Option not recognized!\nThe list has NOT been deleted.')
                input('Press ENTER to continue...')
    else:
        print('\nList not found!\n')
        input('Press ENTER to continue...')

def new_wordlist():
    lang_a = input('Insert first language: ')
    lang_b = input('Insert second language: ')
    if lang_a == '' or lang_b == '':
        print('You cannot insert empty languages name!!')
        return
    file_name = lang_a.lower() + '2' + lang_b.lower()
    if os.path.exists(file_name + '.json'):
        inp = input('The file already exists, do you want to overwrite it? [Y/N]')
        if inp.lower() == 'n':
            return
    return file_name


def main():

    current_dict = ''
    main_dict = {}

    while True:
        print(generate_main_menu(current_dict))

        inp = input("Select option: ")

        if inp == CHECK_WORDLIST:
            check_wordlist(current_dict, main_dict)

        elif inp == ADD_TO_WORDLIST:
            ret = add_to_wordlist(current_dict, main_dict)
            if not ret:
                print('No wordlist selected, the item has not been written.')

        elif inp == DELETE_WORDLIST:
            delete_wordlists()
        
        elif inp == SELECT_WORDLIST:
            current_dict, main_dict = select_wordlist(current_dict, main_dict)

        elif inp == NEW_WORDLIST:
            current_dict = new_wordlist()

        elif inp == ESCAPE:
            if not current_dict == "":
                write_dictionary_file(main_dict, current_dict)
            break

        else:
            cls()
            print('Option not recognised!')


if __name__ == '__main__':
    main()