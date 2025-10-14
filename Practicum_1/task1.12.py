total_revenue = int(input())
silver = 96
gold = silver / 16
price_silver = 48
price_gold = (total_revenue - (silver * price_silver)) / gold
print(price_gold)