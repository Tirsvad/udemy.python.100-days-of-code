from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}


def add_bidder(name, bid):
    bidders[name] = bid


def find_highest_bidder(h_bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in h_bidders:
        if h_bidders[bidder] > highest_bid:
            highest_bid = h_bidders[bidder]
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bidder(name, bid)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        more_bidders = False
        find_highest_bidder(bidders)
    else:
        clear()
