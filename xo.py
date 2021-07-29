import os
from random import randint
from time import sleep
        
def checker():
    ### check if X has winning combination
    if (
        field[0]==x and field[1]==x and field[2]==x 
     or field[3]==x and field[4]==x and field[5]==x 
     or field[6]==x and field[7]==x and field[8]==x 
     or field[0]==x and field[3]==x and field[6]==x 
     or field[1]==x and field[4]==x and field[7]==x 
     or field[2]==x and field[5]==x and field[8]==x 
     or field[0]==x and field[4]==x and field[8]==x 
     or field[2]==x and field[4]==x and field[6]==x
        ):
            
        print('Win X')
        fields()
        quit()
        return 1
        
    ### check if O has winning combination
    elif (
          field[0]==o and field[1]==o and field[2]==o 
       or field[3]==o and field[4]==o and field[5]==o 
       or field[6]==o and field[7]==o and field[8]==o 
       or field[0]==o and field[3]==o and field[6]==o 
       or field[1]==o and field[4]==o and field[7]==o 
       or field[2]==o and field[5]==o and field[8]==o 
       or field[0]==o and field[4]==o and field[8]==o 
       or field[2]==o and field[4]==o and field[6]==o
          ):
              
        print('Win O')
        fields()
        quit()
        return 1
        
    elif i==9:
        print('Draw! To play - run game again!')
        fields()
        quit()
    
def fields():
    print(field[0]+'|'+field[1]+'|'+field[2])
    print('-'*5)
    print(field[3]+'|'+field[4]+'|'+field[5])
    print('-'*5)
    print(field[6]+'|'+field[7]+'|'+field[8])

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pc_move(field):
    rand = randint(0, 8)
    if field[rand] == str(rand+1):
        field[rand] = o
    else:
        pc_move(field)
        
def enter_value(input_message, error_message, input_type_convertion, 
                first_condition_value=None, second_condition_value=None):
                    
    while True:
        try:
            if input_type_convertion == int:
                enter_value = int(input(input_message))
                if enter_value <= first_condition_value \
                and enter_value != second_condition_value:
                    break
                else:
                    print(error_message)
        except:
            print(error_message)
            
    return enter_value
        
x="x"
o="o"

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

i=0

rand_first_move = randint(0, 1)

clear_terminal()
while True:
    start_question = enter_value('Play with PC - 1; '+
    'Play with another player - 2; Close game - 3: ',
    'Value incorrect - choose only numbers from 1 to 3!', int, 3, 0)
    
    if start_question==1 or start_question==2:
        while i<9:
            if (start_question==1 and rand_first_move==1):
                i+=1
                print('PC move!')
                sleep(1)
                rand_first_move-=1
                pc_move(field)
                if checker() == 1:
                    break
                        
            elif (rand_first_move==0 and start_question==1) or start_question==2:
                i+=1
                fields()
                if rand_first_move%2==0:
                    print('X move')
                else:
                    print('O move')

                move = enter_value('Choose your move: ',
                'Value incorrect - choose only numbers from 1 to 9!', int, 9, 0)

                if field[move-1] == str(move):
                    if (start_question==2 and rand_first_move==1):
                        rand_first_move-=1
                        field[move-1] = o
                        if checker() == 1:
                            break
                    else:
                        rand_first_move+=1
                        field[move-1] = x
                        if checker() == 1:
                            break
                else:
                    print('Char X or O was chosen!')
                    i-=1
                
                     
    elif start_question==3:
        quit()
