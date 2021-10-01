import random

nameDict = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

nameList = ["rock", "paper", "scissors"]

outcomes = [
    ["It's draw", "You loose", "You win"],
    ["You win", "It's draw", "You loose"],
    ["You loose", "You win", "It's draw"]
]

print("Choose: rock, paper or scissors:")
choice = input()

computerChoice = random.randint(0,2)

print("Computer chose", nameList[computerChoice])
print(outcomes[nameDict[choice]][computerChoice])