import art

print(art.logo)

print("Welcome to the Blind Auction Project.")
input("Let's get started. Press Enter to continue.")
name = input("What is your name? ")
bid = int(input("What is your bid? $ "))

bids = {}
bids[name] = bid

more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
print("\n" * 100)


while more_bids == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    print("\n" * 100)

highest_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")



