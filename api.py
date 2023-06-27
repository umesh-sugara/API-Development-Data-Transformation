import pandas as pd
import numpy as np
from collections import OrderedDict

#Reading the data and defining the date column
df=pd.read_csv('data.csv',parse_dates=['date'])

# converting the datetime column to date
df['date'] = pd.to_datetime(df['date'].dt.date)

#TODO 1
'''
Api 1:
End point : /api/total_items ,
API Use Cases :
1. Total item (total seats) sold in Marketting for last in q3 of the year?
Expected O/P: returns integer
Parameters: {start_date: DATE, end_date: DATE, department: string}
'''

def total_items(start_date, end_date, department):
    # Filter records based on date range and department
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['department'] == department)]
    
    # Calculate the total seats sold
    response = {
        f'total_seats in {department} department between {start_date} and {end_date} is ' : str(filtered_df['seats'].sum())
    }
    return response









#TODO 2
'''
Api 2:
End point : /api/nth_most_total_item ,
API Use Cases:
1.What is the 2nd most sold item in terms of quantity sold in q4,
2.What is the fourth most sold item in terms of Total price in q2?
Expected O/P: returns string name
Parameters: { item_by: ("quantity" | | "price"), start_date: DATE, end_date:
DATE, n:integer }
'''

def nth_most_total_item(item_by, start_date, end_date, n):

    # Filter records based on date range and quarter
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    output = ''

    if item_by == 'quantity':
        # Calculate the total quantity sold per item
        item_quantity = filtered_df.groupby('software')['seats'].sum()
        # Sort the items by quantity sold in descending order
        sorted_items = item_quantity.sort_values(ascending=False)
    elif item_by == 'price':
        # Calculate the total price per item
        item_price = filtered_df.groupby('software')['amount'].sum()
        # Sort the items by total price in descending order
        sorted_items = item_price.sort_values(ascending=False)
    else:
        return {'message' :"Invalid value for item_by parameter...."}
    
     # Get the nth most sold item
    try:
        nth_item = sorted_items.index[int(n)-1]
        response = {
            f"The Rank {n}, most sold item in terms of {item_by} is : " : nth_item
            # 'This is nth item' : nth_item
        }
        return response
    except IndexError:
        return {'message' :"There is no item at the specified rank....."}


#TODO 3
'''
Api 3:
End point : /api/percentage_of_department_wise_sold_items
API Use Cases:
1.What is the percentage of sold items (seats) department wise?
Expected O/P: {dept_name: x%,……. }
Parameters: {start_date: Date, end_date: Date}
'''

def calculate_sold_items_percentage(start_date, end_date):
    # Filter records based on date range
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # Calculate the total sold seats per department
    department_seats = filtered_df.groupby('department')['seats'].sum()

    # Calculate the total sold seats across all departments
    total_seats = department_seats.sum()

    # Calculate the percentage of sold seats department-wise
    department_percentages = (department_seats / total_seats) * 100
    return dict(department_percentages)




#TODO 4
'''
Api 4:
End point : /api/monthly_sales
API Use Cases:
1.How does the monthly sales for any product look like?
Expected O/P: [1908.0, … 1952.0] for all 12 months
Parameters: {product: String, year:Number}
'''

def calculate_monthly_sales(product, year):
    # Filter records for the specified product and year
    filtered_df = df[(df['software'] == product) & (df['date'].dt.year == year)]

    # Group by month and calculate the total sales per month
    monthly_sales = filtered_df.groupby(filtered_df['date'].dt.month)['seats'].sum()

    # Create a list to hold the monthly sales
    sales_list = []

    for month in range(1, 13):
        # Get the sales for the current month
        sales = int(monthly_sales.get(month, 0))

        # Add the sales to the list
        sales_list.append(sales)

    # return sales_list
    response= {f"Monthly sales for {product} in {year} : " : sales_list}
    return response