import pandas as pd

# Extract Step
print("Extracting data...")

data = {
    "customer_id": [1, 2, 3, 4],
    "name": ["John", "Alice", "Bob", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Chicago", "Houston", "Seattle"]
}

df = pd.DataFrame(data)

print("\nRaw Data:")
print(df)

# Transform Step
print("\nTransforming data...")

df["age_category"] = df["age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)

# Load Step
output_path = "data/processed_data.csv"

df.to_csv(output_path, index=False)

print("\nData successfully loaded!")
print(f"Processed file saved at: {output_path}")

print("\nFinal Transformed Data:")
print(df)