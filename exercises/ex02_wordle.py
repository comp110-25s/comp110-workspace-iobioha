"""This program recreates Wordle!"""

__author__ = "730671071"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    max_turns = 6
    turn_number = 1
    user_won = False

    # Start the game:

    while turn_number <= max_turns and not user_won:
        print(f"=== Turn {turn_number}/{max_turns} ===")

        user_guess = input_guess(len(secret))
        emoji_result = emojified(user_guess, secret)

        if user_guess == secret:
            print(emoji_result)
            print(f"You won in {turn_number}/{max_turns} turns!")
            user_won = True
        else:
            print(emoji_result)
            turn_number = turn_number + 1

    if user_guess != secret:
        user_won = False

    print(f"{max_turns}/{max_turns} - Sorry, try again tomorrow!")


# Check if any character in the user's guess is in the secret word
def contains_char(str_lookup: str, correct_letter: str) -> bool:
    """Determine if any of the letters are correct in the guessed word"""
    assert len(correct_letter) == 1, f"len('{correct_letter}') is not 1"
    idx: int = 0
    while idx < len(str_lookup):
        if str_lookup[idx] == correct_letter:
            return True
        idx = idx + 1
    return False


# Displays accuracy of the user's guess using green, yellow, and white boxes
def emojified(guess: str, secret_word: str) -> str:
    """Determine which characters in a string match those in the secret word"""

    assert len(guess) == len(secret_word), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    secret_idx: int = 0

    while secret_idx < len(guess):
        if guess[secret_idx] == secret_word[secret_idx]:
            result = result + GREEN_BOX

        # Outputs a yellow box if a correct character from input is at the wrong index
        elif contains_char(secret_word, guess[secret_idx]):
            result = result + YELLOW_BOX

        else:
            result = result + WHITE_BOX

        secret_idx = secret_idx + 1

    return result


# Prompts user to guess the secret word
def input_guess(expected_length: int) -> str:
    """Prompts user to enter a string until string is correct length."""
    guess = input(f"Enter a {expected_length} character word:")

    if len(guess) != expected_length:
        return input(f"That wasn't {expected_length} chars! Try again:")
    else:
        return guess


# Determines secret word
if __name__ == "__main__":
    main(secret="codes")
