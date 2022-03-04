from replit import clear
from logo import logo
print(logo)

auction_continue = True
bidders = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  for key in bidding_record:
    bid_amount = bidding_record[key]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = key

  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

# dict.values() or dict.keys() returns a list of values or keys
def find_highest_bidder_2(bidding_record):
  bids_values = bidding_record.values()
  max_bid = max(bids_values)

  for bidder in bidding_record:
    if bidding_record[bidder] == max_bid:
      print(f"The winner is {bidder} with a bid of ${max_bid}")

while auction_continue:
  bidder_name = input("What is your name?: ")
  bidder_amount = int(input("What is your bid?: $"))
  bidders[bidder_name] = bidder_amount
  another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if another_bidder == "no":
    auction_continue = False
    find_highest_bidder_2(bidders)
  else:
    clear()
