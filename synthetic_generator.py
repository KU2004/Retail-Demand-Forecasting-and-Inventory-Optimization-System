import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    
    dates = pd.date_range(start="2023-01-01", periods=365)
    products = ['Milk', 'Bread', 'Rice', 'Sugar', 'Oil']
    venues = ['Mumbai_Store_1', 'Mumbai_Store_2', 'Pune_Store_1']
    
    data = []
    
    for venue in venues:
        for product in products:
            base = np.random.randint(50, 200)
            
            for date in dates:
                seasonal = 25 if date.month in [10,11,12] else 0
                weekend = 15 if date.weekday() >= 5 else 0
                store_effect = np.random.randint(-10, 10)
                
                sales = base + seasonal + weekend + store_effect + np.random.randint(-5, 5)
                
                data.append([date, product, venue, sales])
    
    df = pd.DataFrame(data, columns=['date','product','venue','sales'])
    df.to_csv("data/raw_sales.csv", index=False)

if __name__ == "__main__":
    generate_data()