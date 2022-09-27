from replit import clear
from art import logo
print(logo)

bid_dictionary = {
    "bidders": [],
    "bids": [],
}

def add_bids(bidder, bid_amount):
    new_bidders = bidder
    new_bids = bid_amount
    bid_dictionary["bidders"].append(new_bidders)
    bid_dictionary["bids"].append(new_bids)

should_continue = True
while should_continue:
    name = input("Please enter your name:\n")
    bid = int(input("How much would you like to bid? Please enter a whole dollar amount.\n$"))
    add_bids(bidder=name, bid_amount=bid);
    
    more_bids = input("Are there more bidders? Type 'yes' or 'no':\n")
    if more_bids == "no":
        should_continue = False
        winning_bid = max(bid_dictionary["bids"])
        bid_position = bid_dictionary["bids"].index(winning_bid)
        winner = bid_dictionary["bidders"][bid_position]
        print(f"The winner of the auction is: {winner}")
    else:
        clear()
