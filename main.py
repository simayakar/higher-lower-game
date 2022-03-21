from game_data import data
from art import logo
from art import vs
import random

def get_random_account():
  return random.choice(data)

def get_format_version(data):
  name = data['name']
  desc = data['description']
  country = data['country']
  return f"{name}, a {desc}, from {country}"



def compare(count_1, count_2, flag):
  if count_1 >= count_2:
    return count_1, flag
    
  else:
    flag = 1
    return count_2, flag
    

def game():
  print(logo)
  game_continue = True
  first_data = get_random_account()
  first_text = get_format_version(first_data)
  score = 0
  flag = 0
  
  while game_continue:
      print(f"Compare A: {first_text}")
      print(vs)
      second_data = get_random_account()
      second_text = get_format_version(second_data)
      #if two data are the same choose another 
      if first_data == second_data:
        second_data = get_random_account()
        second_text = get_format_version(second_data)
    
      print(f"Compare B: {second_text}")
      answer = input("Who has more followers? Type 'A' or 'B': ")
      if answer == 'A':
        answer = first_data['follower_count']
      elif answer == 'B':
        answer = second_data['follower_count']
      
      result = compare(first_data['follower_count'], second_data['follower_count'], flag)[0]
      data_flag = compare(first_data['follower_count'], second_data['follower_count'], flag)[1]
      #print(data_flag)
      if result == answer:
        score += 1
        print(f"You're right! Current score: {score}.")
        if data_flag == 1:
          first_data = second_data
          first_text = get_format_version(first_data)
      else:
        print(f"Sorry, wrong answer. Your score is: {score}.")
        game_continue = False
      
game()
