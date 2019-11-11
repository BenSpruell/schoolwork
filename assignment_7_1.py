# make a list of stocks: their ticker symbol is the key and current price is the value
#If stock symbol isn't on the list print msg that it isn't on the list

stocks = {
    'dis': 137.89, 
    'jnj': 133.09, 
    'msft': 146.13, 
    'csco': 48.91, 
    'pfe': 37.00, 
    'intc': 58.27, 
    'v': 178.97, 
    'jpm': 130.21, 
    'mcd': 193.61, 
    'aapl': 260.03, 
    'goog': 1311.37, 
    'ko': 52.20, 
    'nke': 89.85, 
    'ba': 351.20, 
    'mmm': 172.95
    }


print("Welcome to Stock Price Search!")

while True:
    ticker = input("\nPlease enter the ticker abbrevation for the stock: ")

    if ticker == "":
        print("You did not enter a ticker abbrevation!")
        continue
    else:
        break

if ticker in stocks:
    print("The price for the stock is currently: " + stocks[ticker])

else:
    print("Sorry we do not have that information as this time!")