import random
from win_comb_gen import win_comb 
# create a 1-d 3*3 board
board = [' '] * 9
# beauitfy and print board
def printboard():
   for i in range(len(board)):
      if i % 3 == 0:
         print("\n", "-" * 17)  # Horizontal line
      if board[i] == ' ':
            print(f"|  {i + 1}  ", end="")
      else:
            print(f"|  {board[i]}  ", end="")
      if (i + 1) % 3 == 0:
            print("|")  # Vertical line
   print(" -" * 9)  # Horizontal line
   print("\n")
    
# capture player move
def player_move():
    while True:
      player_input = int(input('(- -) PLAYER ENTER THE POSITION:'))
      if 1 <= player_input <= 9 and board[player_input - 1] == ' ':
         board[player_input - 1] = 'x'
         break
      else:
         print('INVALID INPUT')

# check if player win or computer win
# pass there respective sign as parameter
def check_win(player):
   winning_combinations = [
      [0, 1, 2],# top Rows
      [3, 4, 5],# middle 
      [6, 7, 8],# bottom
      [0, 3, 6],# left columns
      [1, 4, 7],# middle
      [2, 5, 8],# right 
      [0, 4, 8],# left-right Digonals
      [2, 4, 6] # right-left 
   ]

   for combination in winning_combinations:
      if all(board[i] == player for i in combination):
         return True
   return False
# check for winner using check_win()
def check_winner():
   if check_win('x'):
      return 0
   elif check_win('o'):
      return 1
   elif ' ' not in board:
      return -1
   else:
      return None

# chance of winning combination and return winning list
# pass the respective sign as parameter
def any_win_combo(player):
   winning_combinations = [
      [0, 1, 2],#Rows
      [3, 4, 5], 
      [6, 7, 8], 
      [0, 3, 6],#columns
      [1, 4, 7], 
      [2, 5, 8],
      [0, 4, 8],#Digonals
      [2, 4, 6]     
   ]
   

   for combination in winning_combinations:
      count_win_chance = sum(1 if board[val] == player else -1 if board[val] != ' ' else 0 for val in combination)
      #count_win_chance = sum(1 for val in combination if board[val] == player)
      if count_win_chance == 2:
         return combination
   return None

# compture move logic
def computer_move():
   # if any combination 
   comb_op = any_win_combo('x')  # is player filled two winning combinations
   comb_co = any_win_combo('o')  # is computer filled two winning combinations
   #print(comb_op)
   #print(comb_co)
   # centre(4) > corner(0,2,6,8) > edge(1,3,5,7)
   cent=[4]
   corner=[0,2,6,8]
   edge=[1,3,5,7]
   random.shuffle(corner)
   random.shuffle(edge)
   cent_cor_edg=cent+corner+edge
   # stop player win
   if comb_op:
      for i in comb_op:
         if board[i] == ' ':
            board[i] = 'o'
            return 
   # now computer try to win
   elif comb_co:
      for i in comb_co:
         if board[i] == ' ':
            board[i] = 'o'
            return 
   # put value at center or corner or edge
   else:
      for val in cent_cor_edg:
         if board[val] == ' ':
            board[val] = 'o'
            return 
         
         
         
printboard()     
while True:
   player_move() # start with player
   flag = check_winner() # check for win 
   if flag == 0:
      print("You won...!")
      break
   elif flag == 1:
      print("Computer won...!")
      break
   elif flag== -1:
      print("Game Draw...")
      break
   printboard() # print board
   
   print('[- -] COMPUTER ENTERD THE POSITION:')
   computer_move() # now computer chance
   # after move check for win
   flag = check_winner() # check for win 
   if flag == 0:
      print("You won...!")
      break
   elif flag == 1:
      print("Computer won...!")
      break
   elif flag==-1:
      print("Game draw..")
      break
   printboard() # print board
      
printboard()

