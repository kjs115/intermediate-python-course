def main():
  import random
  dice_roll=int(input('How many dice would you like to roll? '))
  dice_size=int(input('How many sides are the dice? '))
  no_of_player=int(input('Player 1 or 2 ?'))
  if(no_of_player>2 or no_of_player<1):
    print("Fatal Error!")
    return
  for i in range(1,no_of_player+1):
     dice_sum=0
     print(f"**** For player {i} ****\n")
     for _ in range(dice_roll):
          roll=random.randint(1,dice_size)
          dice_sum+=roll
          if(roll==1):
             print(f'You rolled a {roll}! Critical fail.')
          elif(roll==dice_size):
             print(f'You rolled a {roll}! Critical Success!')
          else:
            print(f'You rolled a {roll}.')
     print(f'You have rolled a total of {dice_sum}.\n')

if __name__== "__main__":
  main()