"""task3.py"""

def minimal_cost(N, prices):
    prices.sort(reverse=True)
    total_cost = 0
    for i in range(0, N, 3):
        total_cost += sum(prices[i:i+2])
    return total_cost

if __name__ == "__main__":
    N = int(input("Enter a count of goods: "))
    prices = list(map(int, input("Enter a price of goods: ").split()))
    print(minimal_cost(N, prices))
