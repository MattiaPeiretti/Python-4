#Mattia Peiretti, Sep 2019, stardate: -303334.24, https://mattiapeiretti.com

CHECK_WORDLIST = 'v'
ADD_TO_WORDLIST = 'a'
DELETE_FROM_WORDLIST = 'd'
SELECT_WORDLIST = 's'
NEW_WORDLIST = 'n'
ESCAPE = 'q'


MENU_WIDTH = 60

def generate_main_menu():
    menu = ''
    lines = {
        'line1' : 'View the selected wordlist',
        'line2' : 'Add item to wordlist',
        'line3' : 'Delete item from wordlist',
        'line4' : 'Select wordlist',
        'line5' : 'Create new wordlist',
        'line6' : 'Quit the program'
    }
    blank_line =  '║' + ' '*(MENU_WIDTH-2) + '║\n'
    menu += '╔' + '═'*(MENU_WIDTH - 2) + '╗\n'
    menu += blank_line
    menu += '║' + ('{:' + str((MENU_WIDTH - 2)) + '}').format(CHECK_WORDLIST + ' - ' + lines['line1'] + ' ' * (((MENU_WIDTH - 2)/4)*3)- len()) + '║\n'
    menu += '║' + ('{:' + str((MENU_WIDTH - 2)) + '}').format(ADD_TO_WORDLIST + ' - ' + 'Add item to wordlist') + '║\n'
    menu += '║' + ('{:^' + str((MENU_WIDTH - 2)) + '}').format(DELETE_FROM_WORDLIST + ' - ' + 'Delete item from wordlist') + '║\n'
    menu += '║' + ('{:^' + str((MENU_WIDTH - 2)) + '}').format(SELECT_WORDLIST + ' - ' + 'Select wordlist') + '║\n'
    menu += '║' + ('{:^' + str((MENU_WIDTH - 2)) + '}').format(NEW_WORDLIST + ' - ' + 'Create new wordlist') + '║\n'
    menu += '║' + ('{:^' + str((MENU_WIDTH - 2)) + '}').format(ESCAPE + ' - ' + 'Quit the program') + '║\n'
    menu += blank_line
    menu += '╔' + '═'*(MENU_WIDTH - 2) + '╗\n'

    return menu

def main():
    print(generate_main_menu())
    input()

if __name__ == '__main__':
    main()