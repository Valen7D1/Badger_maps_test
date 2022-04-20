import pandas as pd

if __name__ == "__main__":
    # first we need to read the csv file, we will be using pandas for the task
    df = pd.read_csv("Sample test file - Sheet1.csv")
    # store actual size for later error detection
    actual_size = df.shape[0]
    # delete al rows with NaN in all their columns
    df = df.dropna(how='all')
    # if size is different there are empty rows
    if df.shape[0] != actual_size:
        print("ERROR: There were", str(actual_size - df.shape[0]), "columns empty")