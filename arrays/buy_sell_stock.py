
def buy_sell_stock(prices: list[int]):
    """
    Return the maximum profit from a stock sale
    """
    min_price = prices[0]
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = max(profit, price - min_price)
    
    return profit


if __name__ == "__main__":
    result = buy_sell_stock([7, 10, 1, 3, 6, 9, 2])
    print(result)