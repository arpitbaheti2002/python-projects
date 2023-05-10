# Hangman Game
This is a classic Hangman game built using **Python**. The game fetches random words from the [Random Word API](https://api-ninjas.com/api/randomword) and provides the player with 7 guesses to correctly guess the word.

### Getting Started
To play the game, simply click the "Run" button on the [Hangman](https://replit.com/@ArpitBaheti1/Hangman?v=1) to run the code.

To download in local machine:<br>
1. Clone this repository to your local machine:
2. Sign up on [API Ninjas](https://api-ninjas.com/) to get an API key.
3. Visit your profile on API Ninjas to obtain your API key.
4. Open the Hangman.py file in a text editor and replace `<Your_API_KEY>` with your actual API key.
5. Save the file.

### Running the Game
1. Navigate to the Beginner/Hangman directory in your terminal or command prompt:<br>
`cd python-projects/Beginner/Hangman`
2. Run the Hangman.py file in your Python environment:<br>
`python Hangman.py`

### Gameplay
When the game is launched, a random word is fetched from the API. The player's task is to guess the word by entering a letter at a time. The player has a total of 7 incorrect guesses before the game ends.

For each incorrect guess, a different ASCII art representation of a hangman is displayed, illustrating the progress of the game.

If the player guesses the word correctly within the 7 guesses, they win. Otherwise, they lose the game.

### Contributing
Contributions to this project are welcome! If you have any suggestions for improvements or new features, feel free to create a pull request.