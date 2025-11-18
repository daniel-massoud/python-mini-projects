#Simple rock, paper, scissors game
import random as ra

def getChoices():
  playerChoice = input("Enter a choice (rock, paper, scissors): ")
  computerChoice = ra.choice(["rock", "paper", "scissors"])
  choices = {"player": playerChoice, "computer": computerChoice}
  return choices

def checkWin(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player==computer:
    return "it's a tie !!"
  elif player=="rock" and computer=="scissors":
    return "you win !!"
  elif player=="paper" and computer=="rock":
    return "you win !!"
  elif player=="scissors" and computer=="paper":
    return "you win !!"
  else:
    return "you lose !"

choices = getChoices()
result = checkWin(choices.get("player"), choices.get("computer"))
print(result)
