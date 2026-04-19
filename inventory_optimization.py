def optimize_inventory(df):
    lead_time = 7
    service_level = 1.65

    # simulate current stock (important fix)
    df['current_stock'] = df['sales'] * 1.2   # assume stock slightly higher than sales

    df['safety_stock'] = df.groupby(['product','venue'])['forecast'].transform('std') * service_level

    df['reorder_point'] = df['forecast'] * lead_time + df['safety_stock']

    # ✅ FIX: compare with stock (NOT sales)
    df['order_qty'] = (df['reorder_point'] - df['current_stock']).clip(lower=0)

    return df