import csv
import operator

sales_file = "sales.csv"
sales_cap = {}

def check_max_value(list_keys):
    list_max_value = []
    list_val = [int(val) for val in list_keys.values()]
    max_val = max(list(list_val))
    for key in list_keys:
        if max_val == int(list_keys[key]):
            list_max_value.append(key)

    return max_val , list_max_value

def check_value_greater_than_hundred(list_keys):
    counter = 0
    list_val = [int(val) for val in list_keys.values()]
    for val in list_val:
        if val > 100:
            counter = counter + 1

    return counter

def question1():
    # This is to read the csv file
    with open(sales_file, 'r') as fp:
        readcsv = csv.reader(fp)
        # We dont want to read the first line as its just the header
        sales_field = next(readcsv)
        sales_cap = {}
        # Read the data from the CSV
        for data in readcsv:
            sales_val = {data[1] : data[2]}
            if data[0] not in sales_cap:
                sales_cap[data[0]] = {}
            sales_cap[data[0]].update(sales_val)

        print ('Month', 'Max_Sales', 'Store_Max')
        for keys in sales_cap:
            max_val, list_max_values = check_max_value(sales_cap[keys])
            for values in list_max_values:
                print(keys, max_val, values)

def question2():
    # This is to read the csv file
    with open(sales_file, 'r') as fp:
        readcsv = csv.reader(fp)
        # We dont want to read the first line as its just the header
        sales_field = next(readcsv)
        sales_cap = {}
        # Read the data from the CSV
        for data in readcsv:
            sales_val = {data[1] : data[2]}
            if data[0] not in sales_cap:
                sales_cap[data[0]] = {}
            sales_cap[data[0]].update(sales_val)

        print ('Month', 'Sales_gt_100')
        for keys in sales_cap:
            counter = check_value_greater_than_hundred(sales_cap[keys])
            print(keys, counter)

def question3():
    # This is to read the csv file
    with open(sales_file, 'r') as fp:
        counter1 = counter2 = counter3 = 0
        readcsv = csv.reader(fp)
        # We dont want to read the first line as its just the header
        sales_field = next(readcsv)
        for data in readcsv:
            int_val = int(data[2])
            if int_val > 0 and int_val <= 150:
                counter1 = counter1 + 1
            
            if int_val >= 151 and int_val <= 299:
                counter2 = counter2 + 1
            
            if int_val >= 300:
                counter3 = counter3 + 1
            
    print ('Sales_Bucket', 'Count_Stores')
    print ('A.0-150', counter1)
    print ('B.151-299', counter2)
    print ('C.ge 300', counter3)

question1()
question2()
question3()