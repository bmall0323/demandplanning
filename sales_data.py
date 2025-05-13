<<<<<<< HEAD
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define date range
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Define SKUs
products = [
    {"Product": "Travel Duffel 30L", "Base Price": 150},
    {"Product": "Travel Duffel 45L", "Base Price": 170},
    {"Product": "Everyday Backpack 20L", "Base Price": 180},
    {"Product": "Everyday Backpack 30L", "Base Price": 200},
    {"Product": "Capture Clip v3", "Base Price": 70},
    {"Product": "Capture Clip Pro", "Base Price": 90},
    {"Product": "Tech Pouch", "Base Price": 60},
    {"Product": "Wash Pouch", "Base Price": 65}
]

# Define regions and channels
regions = ["US", "EU", "Asia"]
channels = ["DTC", "Wholesale"]

# Create data
data = []

for date in date_range:
    for product in products:
        for region in regions:
            for channel in channels:
                # Simulate unit sales with some randomness and seasonality
                base_sales = np.random.poisson(lam=20 if channel == "DTC" else 35)
                # Add seasonality effect
                month_factor = 1.2 if date.month in [3, 4, 5, 11, 12] else 0.9
                units_sold = int(base_sales * month_factor * np.random.uniform(0.8, 1.2))
                unit_price = product["Base Price"] * (1 if channel == "DTC" else 0.85)
                revenue = units_sold * unit_price

                data.append({
                    "Date": date,
                    "SKU": product["Product"],
                    "Region": region,
                    "Channel": channel,
                    "Units Sold": units_sold,
                    "Unit Price": round(unit_price, 2),
                    "Revenue": round(revenue, 2)
                })

# Create DataFrame
df_sales = pd.DataFrame(data)

# Save as CSV
output_path = "C:/Users/billm/Demand Planning/sales_data_daily.csv"
df_sales.to_csv(output_path, index=False)

=======
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define date range
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Define SKUs
products = [
    {"Product": "Travel Duffel 30L", "Base Price": 150},
    {"Product": "Travel Duffel 45L", "Base Price": 170},
    {"Product": "Everyday Backpack 20L", "Base Price": 180},
    {"Product": "Everyday Backpack 30L", "Base Price": 200},
    {"Product": "Capture Clip v3", "Base Price": 70},
    {"Product": "Capture Clip Pro", "Base Price": 90},
    {"Product": "Tech Pouch", "Base Price": 60},
    {"Product": "Wash Pouch", "Base Price": 65}
]

# Define regions and channels
regions = ["US", "EU", "Asia"]
channels = ["DTC", "Wholesale"]

# Create data
data = []

for date in date_range:
    for product in products:
        for region in regions:
            for channel in channels:
                # Simulate unit sales with some randomness and seasonality
                base_sales = np.random.poisson(lam=20 if channel == "DTC" else 35)
                # Add seasonality effect
                month_factor = 1.2 if date.month in [3, 4, 5, 11, 12] else 0.9
                units_sold = int(base_sales * month_factor * np.random.uniform(0.8, 1.2))
                unit_price = product["Base Price"] * (1 if channel == "DTC" else 0.85)
                revenue = units_sold * unit_price

                data.append({
                    "Date": date,
                    "SKU": product["Product"],
                    "Region": region,
                    "Channel": channel,
                    "Units Sold": units_sold,
                    "Unit Price": round(unit_price, 2),
                    "Revenue": round(revenue, 2)
                })

# Create DataFrame
df_sales = pd.DataFrame(data)

# Save as CSV
output_path = "C:/Users/billm/Demand Planning/sales_data_daily.csv"
df_sales.to_csv(output_path, index=False)

>>>>>>> 8fc0d83d0d77ce64ba953ed9c02a467607cc98a7
df_sales.head()