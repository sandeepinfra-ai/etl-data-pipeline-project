import pandas as pd

def extract_data():
    data = pd.read_csv("data/employees.csv")

    print("Data Extracted Successfully")
    print(data)

    return data