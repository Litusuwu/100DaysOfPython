import random 
import art
import game_data
import os

def select(number):
    while True:
        value2 = random.randint(0, len(game_data.data)-1)
        if value2!= number :
            break
    return value2

def compare(v1, v2):
    if game_data.data[v1]['follower_count'] > game_data.data[v2]['follower_count'] :
        return "A"
    else :
        return "B"

def procedure():
    os.system('clear')
    score = 0
    value2 = -1
    print(art.logo)
    while True:
        
        if score == 0 :
            value1 = random.randint(0, len(game_data.data)-1)
        else:
            value1 = value2 
        
        print(f"Compare A: {game_data.data[value1]['name']}, a {game_data.data[value1]['description']},  from {game_data.data[value1]['country']}.")
        print(art.vs)
        value2 = select(value1)
        print(f"Against B: {game_data.data[value2]['name']}, a {game_data.data[value2]['description']},  from {game_data.data[value2]['country']}.")
        flag = compare(value1, value2) #True : wins A - wins B : False
        answer = input("Who has more followers= Type 'A' or 'B' : ")
        if flag == answer:
            os.system('clear')
            score += 1
            print(art.logo)
            print(f"You're right! Current score : {score}")     
        else:
            os.system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score : {score}")
            break

procedure()