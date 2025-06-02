from ..strategy_simulation.advanced_strategy import simulate


df = simulate("data/uploads/sample_stock_data.csv")
print(df.tail(10))
