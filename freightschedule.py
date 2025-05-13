import pandas as pd
import numpy as np

# Define SKUs
skus = [
    "Travel Duffel 30L", "Travel Duffel 45L",
    "Everyday Backpack 20L", "Everyday Backpack 30L",
    "Capture Clip v3", "Capture Clip Pro",
    "Tech Pouch", "Wash Pouch"
]

# Define origin and destination warehouses
origin = "Vietnam Factory"
destinations = ["US Warehouse", "EU Warehouse", "Asia Warehouse"]

# Estimated transit days by destination
transit_days = {
    "US Warehouse": 18,
    "EU Warehouse": 24,
    "Asia Warehouse": 10
}

# Simulate shipment schedule for Q1 2025
shipment_dates = pd.date_range(start="2025-01-05", end="2025-03-25", freq='15D')

# Generate freight schedule data
freight_data = []

for date in shipment_dates:
    for dest in destinations:
        sku = np.random.choice(skus)
        quantity = np.random.randint(500, 1500)
        est_days = transit_days[dest]
        est_arrival = date + pd.Timedelta(days=est_days)
        actual_delay = np.random.choice([0, 1, 2, 3, 5], p=[0.6, 0.2, 0.1, 0.05, 0.05])
        actual_arrival = est_arrival + pd.Timedelta(days=actual_delay)

        freight_data.append({
            "Shipment Date": date.date(),
            "Origin": origin,
            "Destination": dest,
            "SKU": sku,
            "Units Shipped": quantity,
            "Estimated Transit Days": est_days,
            "Estimated Arrival": est_arrival.date(),
            "Actual Arrival": actual_arrival.date(),
            "Days Delayed": actual_delay
        })

# Create DataFrame and export to CSV
df_freight = pd.DataFrame(freight_data)
df_freight.to_csv("freight_schedule.csv", index=False)

print("freight_schedule.csv generated successfully.")
