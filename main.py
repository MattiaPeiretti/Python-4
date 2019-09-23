#Mattia Peiretti, Sep 2019, stardate: -303334.24, https://mattiapeiretti.com

import os
import json

CHECK_WORDLIST = 'v'
ADD_TO_WORDLIST = 'a'
DELETE_FROM_WORDLIST = 'd'
SELECT_WORDLIST = 's'
NEW_WORDLIST = 'n'
ESCAPE = 'q'

WORDLISTS_FILE_DIR = 'wordlists/'


MENU_WIDTH = 60

current_dict = ''
main_dict = {}


#write_json({'src':'sedede'}, 'test')
def write_json(data, filename, filepath=WORDLISTS_FILE_DIR):
    with open(filepath + filename + '.json', 'w', encoding='utf8') as outfile:
        json_str = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(str(json_str))
        

def get_dict_lang(dict_name=main_dict):
    pos = dict_name.find('2')
    if pos = -1:
        return False

def check_file(filename, filepath=WORDLISTS_FILE_DIR):
    if os.path.exists(filepath + filename):
        return True
    else:
        return False

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_menu_line(letter ,text, menu_width):
    space = ' ' * int(menu_width / 10)
    line = '║' + ('{:' + str((menu_width - 2)) + '}').format(space + letter + ' - ' + text) + '║\n'
    return line

def generate_main_menu():
    cls()
    blank_line =  '║' + ' '*(MENU_WIDTH-2) + '║\n'
    menu = '╔' + '═'*(MENU_WIDTH - 2) + '╗\n'
    menu += blank_line
    menu += generate_menu_line(CHECK_WORDLIST, 'View the selected wordlist', MENU_WIDTH)
    menu += generate_menu_line(ADD_TO_WORDLIST, 'Add item to wordlist', MENU_WIDTH)
    menu += generate_menu_line(DELETE_FROM_WORDLIST, 'Delete item from wordlist', MENU_WIDTH)
    menu += generate_menu_line(SELECT_WORDLIST, 'Select wordlist', MENU_WIDTH)
    menu += generate_menu_line(NEW_WORDLIST, 'Create new wordlist', MENU_WIDTH)
    menu += generate_menu_line(ESCAPE, 'Quit the program', MENU_WIDTH)
    menu += blank_line
    menu += '╚' + '═'*(MENU_WIDTH - 2) + '╝\n'
    return menu


def check_wordlist():
    pass

def add_to_wordlist():
    pass

def new_wordlist():
    lang_a = input('Insert first language: ')
    lang_b = input('Insert second language: ')
    if lang_a == '' or lang_b == '':
        print('You cannot insert empty languages name!!')
        return
    file_name = lang_a + '2' + lang_b
    ret = check_file(file_name + '.json')
    if ret:
        inp = input('The file already exists, do you want to overwrite it? [Y/N]')
        if inp.lower() == 'n':
            return
    current_dict = file_name
    
    




def main():
    print(generate_main_menu())
    inp = input("Select option: ")
    if inp == CHECK_WORDLIST:
        check_wordlist()
    elif inp == ADD_TO_WORDLIST:
        add_to_wordlist()
    elif inp == DELETE_FROM_WORDLIST:
        pass
    elif inp == SELECT_WORDLIST:
        pass
    elif inp == NEW_WORDLIST:
        new_wordlist()
    elif inp == ESCAPE:
        pass
    else:
        cls()
        print('Option not recognised!')


if __name__ == '__main__':
    main()