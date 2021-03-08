import random


rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps_list = (rock, paper, scissors)

player_move = input("Make your move!")
print("Your move:\n")
comp_move = random.choice(rps_list)
if player_move == "rock":
    print(rock)
elif player_move == "paper":
    print(paper)
elif player_move == "scissors":
    print(scissors)

print("Comp move:\n" + comp_move)


if player_move == "paper" and comp_move == paper:
    print("Draw!")
elif player_move == "scissors" and comp_move == scissors:
    print("Draw!")
elif player_move == "rock" and comp_move == rock:
    print("Draw!")
elif player_move == "rock" and comp_move == paper:
    print("Comp won!")
elif player_move == "rock" and comp_move == scissors:
    print("You won!")
elif player_move == "paper" and comp_move == rock:
    print("You won!")
elif player_move == "scissors" and comp_move == rock:
    print("Comp won!")




