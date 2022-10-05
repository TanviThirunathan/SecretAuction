
import os
from art import logo
print(logo)

print("Welcome to the Secret Auction program!")

gameon = True
dict_auction = {}

while(gameon == True):
    
    name = input("What is your name ? : ")
    bid = int(input("What is your bid ? : $ "))
    
    def secret_auction(name,bid):
        dict_auction[name] = bid
        print(dict_auction)
        
    secret_auction(name,bid)
    
    
    continue_game = input("Are there any other bidders ? Type 'yes' or 'no'.")
    
    if (continue_game == "yes"):
        os.system("cls")
    elif (continue_game == "no"):
        gameon = False
        break
    

highest_auction_key = max(dict_auction, key = dict_auction.get)
print(highest_auction_key)
highest_auction_value = max(dict_auction.values())
print(highest_auction_value)

print("The winner is " +str(highest_auction_key) + ", with a bid of " +  str(highest_auction_value))

    


