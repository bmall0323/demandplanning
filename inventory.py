import pandas as pd
import numpy as np

# Define SKUs and warehouse regions
skus = [
    "Travel Duffel 30L", "Travel Duffel 45L",
    "Everyday Backpack 20L", "Everyday Backpack 30L",
    "Capture Clip v3", "Capture Clip Pro",
    "Tech Pouch", "Wash Pouch"
]

regions = ["US", "EU", "Asia"]

# Generate starting inventory numbers
data_inventory = []

for sku in skus:
    for region in regions:
        base_inventory = np.random.randint(800, 3000)  # simulate typical starting inventory
        data_inventory.append({
            "SKU": sku,
            "Warehouse Region": region,
            "Starting Inventory": base_inventory
        })

# Create DataFrame
df_inventory = pd.DataFrame(data_inventory)

# Save as CSV
output_path_inventory = "C:/Users/billm/Demand Planning/inventory_levels.csv"
df_inventory.to_csv(output_path_inventory, index=False)

df_inventory.head()
