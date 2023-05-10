import requests
import os
from art import art, logo

headers = {
  'X-Api-Key': '<YOUR_API_KEY>'
}

response = requests.get("https://api.api-ninjas.com/v1/randomword", headers=headers)
response.raise_for_status()

word = response.json()['word']
number_of_guesses = 7
guessed_letters = []
game_is_on = True

def print_word():
  print("Word: ",end=" ")
  for letter in word:
    if letter in guessed_letters:
      print(letter, end="")
    else:
      print("_", end="")
  print("\n")

def is_game_over():
  if number_of_guesses == 0:
    return True
  
  for letter in word:
    if letter not in guessed_letters:
      return False
    
  return True


while game_is_on:
  os.system('cls')
  print(logo)
  print(art[7-number_of_guesses])
  print("\n")
  print(f"Guesses left: {number_of_guesses}")
  
  print_word()
  user_input = input("Guess: ")

  if user_input in guessed_letters:
    continue
  else:
    guessed_letters.append(user_input)

  if user_input not in word:
    number_of_guesses -= 1

  game_is_on = not is_game_over()

if number_of_guesses>0:
  print('Congratulations! You win!')
print(f'The word is: {word}')
