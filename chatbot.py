"""A small rule-based mood chatbot called Sunny."""

import random
import time


def typing_effect(text, delay=0.02):
    """Print one character at a time to make the chat feel natural."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def lonely():
    typing_effect("I am sorry you are feeling lonely. Here is a virtual hug.")
    typing_effect("Try taking one slow breath with me: inhale, hold, and exhale.")
    typing_effect("Reaching out to someone you trust can also make the day feel lighter.")


def sad():
    typing_effect("It is okay to have a difficult day. You do not have to hide it.")
    answer = input("Would you like a positive reminder? (y/n): ").strip().lower()
    if answer == "y":
        affirmation()
    else:
        typing_effect("That is okay. I am still here to listen.")


def anxious():
    typing_effect("Let us pause for a short breathing exercise.")
    typing_effect("Breathe in for four seconds, hold for four, and breathe out slowly.")
    typing_effect("Focus on what is around you right now, one thing at a time.")


def happy():
    typing_effect("That is good to hear!")
    typing_effect("Try to remember what made today feel good so you can return to it later.")


def talk():
    message = input("You: ").strip()
    if message:
        typing_effect("Thank you for sharing that with me.")
        typing_effect("Your thoughts and feelings matter.")
    else:
        typing_effect("No pressure. Take your time.")


def affirmation():
    messages = [
        "You are enough as you are.",
        "Your feelings are valid.",
        "Small progress is still progress.",
        "You are doing better than you think.",
        "It is okay to ask for help.",
    ]
    typing_effect(random.choice(messages))


def surprise():
    actions = [lonely, anxious, happy, affirmation]
    random.choice(actions)()


def mood_menu():
    actions = {
        "1": lonely,
        "2": sad,
        "3": anxious,
        "4": happy,
        "5": talk,
        "6": surprise,
    }

    while True:
        print("\nHow are you feeling?")
        print("1. Lonely")
        print("2. Sad")
        print("3. Anxious")
        print("4. Happy")
        print("5. I just want to talk")
        print("6. Surprise me")

        choice = input("Choose 1-6: ").strip()
        action = actions.get(choice)
        if action is None:
            typing_effect("That is not a valid option. Please choose a number from 1 to 6.")
            continue

        action()
        again = input("\nWould you like to continue? (y/n): ").strip().lower()
        if again != "y":
            typing_effect("Take care of yourself. Goodbye for now!")
            break


def welcome():
    typing_effect("Hi, I am Sunny, a small mood chatbot.")
    typing_effect("You can choose how you feel or simply talk for a moment.")
    mood_menu()


if __name__ == "__main__":
    welcome()

