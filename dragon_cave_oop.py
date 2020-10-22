import random


class Game:
    def __init__(self):
        self.friendly_dragon = random.randint(1, 2)
        self.choice = None

    def print_intro(self):
        print(
            """You arrive to a magical land full of dragons. In front of you are 2 caves. One cave contains a friendly dragon that will give you treasure. The other contains a hungry dragon that will eat you on sight. Which will you choose?***"""
        )

    def get_user_choice(self):
        while self.choice not in range(1, 3):
            print("You can only choose 1 or 2")
            self.choice = input()

    def check_user_choice(self):
        if self.choice is self.friendly_dragon:
            print(
                "Hooray, you entered the friendly dragon's cave and win a million dollars! \o/")
        else:
            print("Oh no, you entred the hungry dragon's cave. You have been eaten.")


if __name__ == '__main__':
    new_game = Game()
    new_game.print_intro()
    new_game.get_user_choice()
    new_game.check_user_choice()
