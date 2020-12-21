# Problem: Write a program that takes an array denoting the daily stock price, and returns the maximum
#          profit that could be made by buying and selling one share of that stock. There is no need to buy if
#          no profit is possible

def buy_and_sell_stock_once(prices):
    max_profit = 0
    min_so_far = float('inf')

    for price in prices:
        profit = price - min_so_far
        max_profit = max(profit, max_profit)
        min_so_far = min(price, min_so_far)

    return max_profit

if __name__ == "__main__":
    prices = [3.2, 4.6, 2.7, 16.4, 15.1, 13.9, 14.5, 10.5, 1.7, 6.5, 3.6, 16.3, 2.8, 14.5, 14.2, 12.1, 5.9, 15.9, 13.6, 3.0, 6.8, 2.8, 0.3, 1.4, 7.2, 11.7, 12.1, 8.5, 10.9, 16.2, 5.5, 13.9, 1.8, 1.2, 1.4, 5.7, 11.5, 5.2, 0.6, 10.5, 9.7, 1.8, 14.0, 4.4, 1.5, 16.9, 6.9, 12.0, 13.4, 5.1, 12.9, 2.5, 4.3, 7.6, 5.6, 1.7, 1.0, 3.4, 8.7, 6.6, 7.8, 10.7, 8.1, 16.5, 10.1, 7.2, 0.5, 0.5, 16.2, 6.8, 4.9, 13.2, 0.7, 8.1, 2.9, 14.0, 9.1, 0.8, 7.6, 10.2, 2.2, 1.3, 1.2, 9.0, 9.5, 13.4, 6.2, 4.0, 8.0, 7.8, 6.5, 5.8, 16.5, 13.8, 11.1, 8.5, 1.4, 2.0, 12.6, 12.0, 1.5, 6.8, 3.8, 4.2, 12.9, 4.2, 15.8, 7.5, 5.2, 15.8, 15.4, 1.5, 9.0, 13.1, 4.8, 6.1, 8.0, 16.9, 9.4, 11.2, 6.5, 1.7, 13.1, 13.2, 7.1, 14.6, 16.6, 14.8, 3.0, 6.9, 4.7, 10.8, 9.8, 10.7, 11.3, 10.3, 5.0, 1.7, 9.0, 14.0, 11.9, 12.4, 13.3, 8.3, 8.9, 6.7, 12.6, 5.3, 14.7, 11.8, 16.9, 10.6, 14.0, 3.3, 12.4, 14.5, 1.9, 0.5, 2.7, 13.5, 10.0, 3.1, 0.8, 15.6, 15.6, 13.5, 3.7, 6.3, 14.7, 5.7]
    print(buy_and_sell_stock_once(prices))