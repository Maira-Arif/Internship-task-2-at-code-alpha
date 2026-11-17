# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total = 0

print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when finished.\n")

while True:
    name = input("Enter stock name: ").upper()

    if name == "DONE":
        break

    if name not in stock_prices:
        print("Stock not found. Try again.")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    value = stock_prices[name] * qty
    portfolio[name] = portfolio.get(name, 0) + qty
    total += value
    print(f"{name}: {qty} x ${stock_prices[name]} = ${value}\n")

print("\n--- Portfolio Summary ---")
for name, qty in portfolio.items():
    print(f"{name}: {qty} shares = ${stock_prices[name] * qty}")
print("Total Investment: $", total)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write("--- Portfolio Summary ---\n")
    for name, qty in portfolio.items():
        f.write(f"{name}: {qty} shares = ${stock_prices[name] * qty}\n")
    f.write(f"Total Investment: ${total}\n")

print("\nResult saved to portfolio.txt")