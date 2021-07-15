from os import system
bidders={}
def high(bidders):
    """Chooses the highest bidder among the list of bidders"""
    high_bid=0
    winner=''
    for bidder in bidders:
        bid=bidders[bidder]
        if bid > high_bid:
            high_bid=bid
            winner=bidder
    print(f"highest bidder is {winner} with a bid of {high_bid}")
while True:
    name=input("please enter your name: ")
    bid=int(input("please enter your bid: "))
    bidders[name]=bid
    left=input("are there any bidders left,type yes or no: ")
    if left=="yes":
        _=system('clear')
    if left == "no":
        high(bidders)
        break
