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

#write_json({'src':'sedede'}, 'test')
def write_json(data, filename, filepath=WORDLISTS_FILE_DIR):
    with open(filepath + filename + '.json', 'w', encoding='utf8') as outfile:
        json_str = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(str(json_str))

def load_file(filename, dir = WORDLISTS_FILE_DIR):
    with open(dir+filename) as data_file:
        data_loaded = json.load(data_file)


        
def get_dict_lang(dict_name):
    pos = dict_name.find('2')
    lang_a = dict_name[0:pos]
    lang_b = dict_name[(pos + 1):len(dict_name)]
    return (lang_a, lang_b) 

def check_file(filename, filepath=WORDLISTS_FILE_DIR):
    if os.path.exists(filepath + filename):
        return True
    else:
        return False

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
    menu += generate_menu_line(DELETE_FROM_WORDLIST + ' - ' + 'Delete item from wordlist', MENU_WIDTH)
    menu += generate_menu_line(SELECT_WORDLIST + ' - ' + 'Select wordlist', MENU_WIDTH)
    menu += generate_menu_line(NEW_WORDLIST + ' - ' + 'Create new wordlist', MENU_WIDTH)
    menu += generate_menu_line(ESCAPE + ' - ' + 'Save and quit the program', MENU_WIDTH)
    menu += blank_line
    menu += generate_menu_line('Slected Wordlist: ' + current_dictionary, MENU_WIDTH)
    menu += blank_line
    menu += '╚' + '═'*(MENU_WIDTH - 2) + '╝\n'
    return menu

def read_wordlists_files(dir=WORDLISTS_FILE_DIR):
    files = []
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            files.append(filename)
    if not files:
        return
    return files

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
    return file_name
    
    




def main():

    current_dict = ''
    main_dict = {}

    while True:
        # print(main_dict)
        # input()
        print(generate_main_menu(current_dict))
        inp = input("Select option: ")
        if inp == CHECK_WORDLIST:
            check_wordlist()
        elif inp == ADD_TO_WORDLIST:
            if current_dict:
                lang_a, lang_b = get_dict_lang(current_dict)
                word_a = input('Insert word in {}:'.format(lang_a))
                word_b = input('Insert word in {}:'.format(lang_b))
                main_dict[word_a] = word_b

        elif inp == DELETE_FROM_WORDLIST:
            pass
        elif inp == SELECT_WORDLIST:
            files = read_wordlists_files()
            for x in range(len(files)):
                print(files[x])
            inp = input('Enter name: ')
            if inp:

            
        elif inp == NEW_WORDLIST:
            current_dict = new_wordlist()
        elif inp == ESCAPE:
            break
        else:
            cls()
            print('Option not recognised!')


if __name__ == '__main__':
    main()