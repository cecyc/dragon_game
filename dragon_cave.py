import random
import sys

print(
    """You arrive to a magical land full of dragons. In front of you are 2 caves. One cave contains a friendly dragon that will give you treasure. The other contains a hungry dragon that will eat you on sight. Which will you choose?***"""
)
choice = input()
# can only choose between 1 and 2
# check that the choice is not a number that is not 1 or 2
while choice not in range(1, 3):
    print("You can only choose 1 or 2")
    choice = input()

# set a friendly dragon at random
friendly_dragon = random.randint(1, 2)

if choice is friendly_dragon:
    print("Hooray, you entered the friendly dragon's cave and win a million dollars! \o/")
else:
    print("Oh no, you entred the hungry dragon's cave. You have been eaten.")

sys.exit(0)
