
# Importing the clear function from the replit module to clear the console
from replit import clear
# Importing the logo from the art module to print the program's logo
from art import logo

# Printing the program's logo
print(logo)

# Initializing an empty dictionary to store bidder names and bid amounts
client = {}
# Initializing a boolean variable to track if the bidding process has finished
bidding_finished = False

# Defining a function to find the bidder with the highest bid
def find_highest_bidder(bidding_record):
    # Initializing a variable to store the highest bid
    highest_bid = 0 
    # Iterating through each bidder in the bidding record
    for bidder in bidding_record:
        # Retrieving the bid amount for the current bidder
        bid_amount = bidding_record[bidder] 
        # Checking if the current bid is higher than the highest bid so far
        if bid_amount > highest_bid:
            # Updating the highest bid and winner if the current bid is higher
            highest_bid = bid_amount
            winner = bidder
    # Printing the winner and their bid amount
    print(f"the winner is {winner} with the highest bid: ${highest_bid}")

# Running the bidding process until bidding_finished becomes True
while not bidding_finished:
    # Asking the user for their name
    name = input("What is your name?: ")
    # Asking the user for their bid amount and converting it to an integer
    price = int(input("What is your bid?: $"))
    # Adding the bidder's name and bid amount to the client dictionary
    client[name] = price
    # Asking the user if there are any other bidders
    restart = input("Are there any other bidders? Type 'yes' or 'no': ")
    # Checking if the user wants to continue bidding
    if restart == "no":
        # Setting bidding_finished to True if the user doesn't want to continue
        bidding_finished = True
        # Calling the find_highest_bidder function to determine the winner
        find_highest_bidder(client)
    elif restart == "yes":
        # Clearing the console if the user wants to continue bidding
        clear()
