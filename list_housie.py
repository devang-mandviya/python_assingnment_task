import random

main_list = []

while len(main_list)<12:
    ticket = random.randint(1,100)
    if ticket not in main_list:
        main_list.append(ticket)

player_1 = main_list[:6] # first 6 elements from the list 
player_2 = main_list[6:] # last 6 elements 

random.shuffle(main_list)
print(main_list)
print(player_1)
print(player_2)

ticket_list = main_list

print(" LET'S START THE GAME ")

status = True 
while status:
    input()
    lucky_ticket =random.choice(ticket_list)
    
    print("LUCKY NUMBER : ",lucky_ticket)
    if lucky_ticket in player_1:
        print("PLAYER 1 WIN ")
        player_1.remove(lucky_ticket)
    elif lucky_ticket in player_2:
        print("PLAYER 2 WIN ")
        player_2.remove(lucky_ticket)
    print("player  1   = ",player_1)
    print("player  2   = ",player_2)
    ticket_list.remove(lucky_ticket)
    if len(player_1)==0:
        status = False
        print("----------- PLAYER 1 WON THE GAME")
    elif len(player_2)==0:
        status = False
        print("----------- PLAYER 2 WON THE GAME")


