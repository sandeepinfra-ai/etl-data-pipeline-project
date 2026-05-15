def transform_data(data):

    # Remove missing values
    data = data.dropna()

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Tax calculation
    data["tax"] = data["amount"] * 0.18

    # Final amount
    data["final_amount"] = data["amount"] + data["tax"]

    print("Data Transformed Successfully")
    print(data)

    return data