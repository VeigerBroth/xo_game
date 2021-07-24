import os
from random import randint
from time import sleep
        
def checker():
    ### check if X has winning combination
    if field[0]==x and field[1]==x and field[2]==x or field[3]==x and field[4]==x and field[5]==x or field[6]==x and field[7]==x and field[8]==x or field[0]==x and field[3]==x and field[6]==x or field[1]==x and field[4]==x and field[7]==x or field[2]==x and field[5]==x and field[8]==x or field[0]==x and field[4]==x and field[8]==x or field[2]==x and field[4]==x and field[6]==x:
        print('Win X')
        fields()
        quit()
        return 1
	### check if O has winning combination
    elif field[0]==o and field[1]==o and field[2]==o or field[3]==o and field[4]==o and field[5]==o or field[6]==o and field[7]==o and field[8]==o or field[0]==o and field[3]==o and field[6]==o or field[1]==o and field[4]==o and field[7]==o or field[2]==o and field[5]==o and field[8]==o or field[0]==o and field[4]==o and field[8]==o or field[2]==o and field[4]==o and field[6]==o:
        print('Win O')
        fields()
        quit()
        return 1
    elif i==8:
        print('Draw! To play - run game again!')
        fields()
        quit()
    
def fields():
    print(field[0]+'|'+field[1]+'|'+field[2])
    print('-'*5)
    print(field[3]+'|'+field[4]+'|'+field[5])
    print('-'*5)
    print(field[6]+'|'+field[7]+'|'+field[8])

def mes_chosen_char():
    print("Char X or O was chosen.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def rand_start_player():
    rand = randint(0, 1)
    return rand

def pc_move(field):
    rand = randint(0, 8)
    if field[rand] == str(rand+1):
        field[rand] = o
    else:
        pc_move(field)
        
x="x"
o="o"

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

rand = rand_start_player()
clear_terminal()
while True:
    start_question = input('Play with PC - 1; Play with another player - 2; Close game - 3: ')

    try:
        con_st_q = int(start_question)
    except:
        con_st_q = -1

    if con_st_q == 2:
        i=-1
        while i<9:
            i = i+1
            fields()
            if rand%2==0:
                print('X move')
            else:
                print('O move')
    
            w = input("Choose field number: ")
            
            try:
                q = int(w)
            except:
                q = -1
            if q > 0 and q < 10:
                if q==1 or q==2 or q==3 or q==4 or q==5 or q==6 or q==7 or q==8 or q==9:
                    if field[q-1] == str(q):
                        if rand%2==0:
                            rand = rand+1
                            field[q-1]=x
                            if checker() == 1:
                                break
                        else:
                            rand = rand-1
                            field[q-1]=o
                            if checker() == 1:
                                break
                    else:
                        mes_chosen_char()
                        i = i-1
                else:
                    i = i-1
                    print("Value incorrect - choose only numbers from 1 to 9!")

    elif con_st_q == 1:
        i = -1
        while i < 10:
            if rand == 1:
                i = i+1
                if i == 0:
                    print('First move its PC!')
                    sleep(1)
                else:
                    print('PC move!')
                    sleep(1)
                rand = rand-1
                pc_move(field)
                if checker() == 1:
                    break
                
            else:
                i = i+1
                fields()
                print('Now its player move!')
                sleep(1)
                move = input('Choose your move: ')
        
                try:
                    q = int(move)
                
                except:
                    q = -1
                if q > 0 and q < 10:
                    if q==1 or q==2 or q==3 or q==4 or q==5 or q==6 or q==7 or q==8 or q==9:
                        if field[q-1] == str(q):
                            rand = rand+1
                            field[q-1] = x
                            if checker() == 1:
                                break
                        else:
                            mes_chosen_char()
                            i = i-1
                            
                else:
                    print('Value incorrect - choose only numbers from 1 to 9!')
                    i = i-1
            
        quit()
        
    elif con_st_q == 3:
        quit()

    else:
        print("Value incorrect - choose only numbers from 1 do 3!")
