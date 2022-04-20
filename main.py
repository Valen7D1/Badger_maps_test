import pandas as pd
import time
from queue import PriorityQueue


def latest_check(dataset):
    # modify index for visual simplicity
    winner = None
    # for every row in dataset
    for i in range(dataset.shape[0]):
        # data in "array" form for processing
        data = dataset.iloc[[i]].values[0]
        if type(data[6]) != float:
            if winner is None:
                try:
                    # transform into time structure
                    time.strptime(data[6], "%d/%m/%Y")
                    winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row ", str(i))
            else:
                # no need to check winner because it was already checked
                # transform into time structure
                date1 = time.strptime(winner[6], "%d/%m/%Y")
                try:
                    # transform into time structure
                    date2 = time.strptime(data[6], "%d/%m/%Y")
                    if date1 < date2:
                        # draws will let the previous winner to stay
                        winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row ", str(i))

    return winner


def oldest_check(dataset):
    # modify index for visual simplicity
    winner = None
    # for every row in dataset
    for i in range(dataset.shape[0]):
        # data in "array" form for processing
        data = dataset.iloc[[i]].values[0]
        if type(data[6]) != float:
            if winner is None:
                try:
                    # transform into time structure
                    time.strptime(data[6], "%d/%m/%Y")
                    winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row", str(i))
            else:
                # no need to check winner because it was already checked
                # transform into time structure
                date1 = time.strptime(winner[6], "%d/%m/%Y")
                try:
                    # transform into time structure
                    date2 = time.strptime(data[6], "%d/%m/%Y")
                    if date1 > date2:
                        # draws will let the previous winner to stay
                        winner = data
                except ValueError:
                    print("ERROR: Invalid date format, ignoring row", str(i))

    return winner


def order_by_name(dataset):
    q = PriorityQueue()
    for i in range(dataset.shape[0]):
        # data in "array" form for processing
        data = dataset.iloc[[i]].values[0]
        # if there is no valid data the full_name will remain none
        full_name = None
        # check if first name is str type, if not, it means it is empty (NaN)
        if type(data[0]) == str:
            # check if last name is str type, if not, it means it is empty (NaN)
            if type(data[1]) == str:
                full_name = data[0] + " " + data[1]
            else:
                print("ERROR: Last name cell empty for column", str(i))
        else:
            # check if last name is str type, if not, it means it is empty (NaN)
            if type(data[1]) == str:
                print("ERROR: First name cell empty for column", str(i))
                full_name = data[1]
            else:
                print("ERROR: First and last name cells empty for column", str(i), " ignoring row")
        if full_name is not None:
            # add ordered to the queue
            q.put(full_name)

    full_name_array = []
    # I would usually give the queue but the exercise asks for a list so I will transform it first
    while not q.empty():
        # dequeue data and append it to the final array
        full_name_array.append(q.get())
    return full_name_array


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
    # we will not use the sort library module or the order module from pandas
    # if used the exercise will be simplified to almost nothing
    # search for the most old check-in
    elder = oldest_check(df)
    if elder is None:
        print("ERROR: None rows with valid check-in data cells found")
    else:
        print("Oldest customer check-in:", list(elder))
        # search for the most recent check-in
        youngling = latest_check(df)
        print("\nLatest customer check-in:", list(youngling))

    # array of the names in alphabetical order
    customers = order_by_name(df)
    if not len(customers):
        print("ERROR: None rows with valid first/ last name cells found")
    else:
        print("\nList with customers sorted by Name:", customers)
