# chained functions
#     learning how to use resuse functions // limits rewriting code
def convert_USD_to_UGX(usd):
    exchange_rate = 3750
    ugx = usd*exchange_rate
    return ugx

wallet = convert_USD_to_UGX(500)
print(f"Cash in UGX is {wallet}")


def buy_smartphone(amount):
    if amount >= 900000:
        return "You can afford a smartphone, make purchase"
    else:
        return "Insufficient funds!"

status = buy_smartphone(wallet)

smartphone = 900000
wallet = wallet-smartphone
print(status)
print(f"Current balance: {wallet}")

def internet(current_balance, price):
    new_balance = current_balance-price
    if current_balance >= price:
        print("You can afford the special bundle")
        return new_balance 
    else:
        print("Insufficient funds!")
        return current_balance
    
wallet = internet(wallet, 1000000)
print(wallet)