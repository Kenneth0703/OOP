import CoinClass as c
#coin is placeholder
def show_coin_status(coin_obj):
    print(f"This side is up: {coin_obj.get_sideup()}") 

def flip(coin_obj):
    coin_obj.toss()






my_coin = c.Coin()# create instance

show_coin_status(my_coin) # passing obj thru function
flip(my_coin)
show_coin_status(my_coin)
#show_coin_status("coin")    #STR to coin obj, does not work