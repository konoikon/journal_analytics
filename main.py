import os
import csv
from pprint import pprint

answer = {
    # Morning Section
    "grateful": [], # 3 Things I'm grateful for
    "great_today": null, # What would make today great?
    "affirmations": [], #D Daily affirmations: I am...
    "ideas": [],
    # Night Section
    "amazing_today": [], # 3 amazing things that happened today
    "learned": null, # 3 things I learned today
    "rating": null, # -2 to 2
    "tasks": [] # 6 Important tasks for the next day
}

def main():
    time = input("Welcome to your journal! Is it morning or night (m/n): ").lower()
    if (time == "m"):
        print("Great! Let's get started!")
        print("What are 3 things you are greatful for today?")
        for _ in range(3):
            answer["grateful"].append(input("> "))
        print("What would make today great?")
        answer["great_today"] = input("> ")
        print("Go on with your daily affirmations! I am...")
        for _ in range(3):
            answer["affirmations"].append(input("> "))
        print("Go on now, tell me three of the ideas you have...")
        for _ in range(3):
            answer["ideas"].append(input("> "))
    elif (time == "n"):
        print("Before you go to bed. Tell me 3 things that made today an amazing day.")
        for _ in range(3):
            answer["amazing_today"].append(input("> "))
        print("List 3 things that you learned today.")
        for _ in range(3):
            answer["learned"].append(input("> "))
        answer["rating"] = input("How would you rate your day from -2 to 2: ")
        print("Last. List the 6 most important tasks you have to do tomorrow.")
        for _ in range(6):
            answer["tasks"].append(input("> "))
        
    pprint(answer)


if __name__ == "__main__":
    main()