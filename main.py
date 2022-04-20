import pandas as pd
import time


def oldest_check(dataset):
    # modify index for visual simplicity
    winner = None
    for i in range(dataset.shape[0]):
        data = dataset.iloc[[i]].values[0]
        if type(data[6]) != float:
            if winner is None:
                try:
                    time.strptime(data[6], "%d/%m/%Y")
                    winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row", str(i))
            else:
                date1 = time.strptime(winner[6], "%d/%m/%Y")
                try:
                    date2 = time.strptime(data[6], "%d/%m/%Y")
                    if date1 > date2:
                        # draws will let the previous winner to stay
                        winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row", str(i))

    return winner


def latest_check(dataset):
    # modify index for visual simplicity
    winner = None
    for i in range(dataset.shape[0]):
        data = dataset.iloc[[i]].values[0]
        if type(data[6]) != float:
            if winner is None:
                try:
                    time.strptime(data[6], "%d/%m/%Y")
                    winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row ", str(i))
            else:
                date1 = time.strptime(winner[6], "%d/%m/%Y")
                try:
                    date2 = time.strptime(data[6], "%d/%m/%Y")
                    if date1 < date2:
                        # draws will let the previous winner to stay
                        winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row ", str(i))

    return winner


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

    # if used the exercise will be simplified to almost nothing
    # search for the most old check-in
    elder = oldest_check(df)
    print("Oldest customer check-in:", list(elder))

    # search for the most recent check-in
    youngling = latest_check(df)
    print("\nLatest customer check-in:", list(youngling))
