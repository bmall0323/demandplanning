import pandas as pd
import numpy as np

# Define SKUs and routes
skus = [
    "Travel Duffel 30L", "Travel Duffel 45L",
    "Everyday Backpack 20L", "Everyday Backpack 30L",
    "Capture Clip v3", "Capture Clip Pro",
    "Tech Pouch", "Wash Pouch"
]

routes = {
    "Vietnam Factory → US Warehouse": 7500,
    "Vietnam Factory → EU Warehouse": 9000,
    "Vietnam Factory → Asia Warehouse": 3500
}

# Simulate cost structure: per kg rates by route + product weight approximations
sku_weights = {
    "Travel Duffel 30L": 2.5,
    "Travel Duffel 45L": 2.8,
    "Everyday Backpack 20L": 2.2,
    "Everyday Backpack 30L": 2.6,
    "Capture Clip v3": 0.4,
    "Capture Clip Pro": 0.5,
    "Tech Pouch": 0.7,
    "Wash Pouch": 0.8
}

# Freight rate per kg (USD)
base_rate_per_kg = {
    "Vietnam Factory → US Warehouse": 2.5,
    "Vietnam Factory → EU Warehouse": 2.8,
    "Vietnam Factory → Asia Warehouse": 1.8
}

# Build dataset
freight_cost_data = []

for route, distance_km in routes.items():
    for sku, weight in sku_weights.items():
        rate = base_rate_per_kg[route]
        cost_per_unit = weight * rate
        freight_cost_data.append({
            "Route": route,
            "SKU": sku,
            "Product Weight (kg)": weight,
            "Freight Rate ($/kg)": rate,
            "Cost per Unit (USD)": round(cost_per_unit, 2),
            "Distance (km)": distance_km
        })

# Create DataFrame and save
df_freight_costs = pd.DataFrame(freight_cost_data)
output_path_costs = "C:/Users/billm/Demand Planning/freight_costs.csv"
df_freight_costs.to_csv(output_path_costs, index=False)

df_freight_costs.head()
