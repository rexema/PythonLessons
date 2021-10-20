prices = [32.48, 46.51, 97.2, 52.15, 85, 20.09, 35.4, 75.5, 15.4, 64, 150, 212.56, 46]
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
prices2=list(reversed(prices))
print(prices2)
print(id(prices2))

prices.sort()
print(prices[-1:-6:-1])
