# API Development and Data Transformation
The objective of this project is to develop APIs, using the attached dataset, of purchases of different softwares through out the year. Initially, it is tested with the dataset attached, but later on, the working project will be implemented on Real-Time SQL Database. 

## Dataset : Card transaction data
https://drive.google.com/file/d/1YfhCPZbofAekMy9tPH_7ZXChVX8w_OUF/view?usp=sharing

## Requirements.txt
Following are the Python libraries used:
  - flask (Flask, jsonify, request)
  - pandas
  - json

## Tasks
### Api 1
  - End point : /api/total_items
  - API Use Cases :
    - Total item (total seats) sold in Marketting for last in q3 of the year?
    - Expected O/P: returns integer
    - Parameters: {start_date: DATE, end_date: DATE, department: string}
    - Link : http://127.0.0.1:5000/api/total_items?start_date=2022-07-01&end_date=2022-09-30&department=Marketting
      
    - ![image_2023_06_24T03_35_35_074Z](https://github.com/umesh-sugara/API-Development-Data-Transformation/assets/73294581/845d3d12-ebae-48f4-980a-686ca6e0c4fc)


### Api 2
  - End point : /api/nth_most_total_item
  - API Use Cases :
    - What is the 2nd most sold item in terms of quantity sold in q4?
    - What is the 4th most sold item in terms of Total price in q2?
    - Expected O/P: returns string name
    - Parameters: { item_by: ("quantity" | | "price"), start_date: DATE, end_date:DATE, n:integer }
    - Link : http://127.0.0.1:5000/api/nth_most_total_item?item_by=quantity&start_date=2022-10-01&end_date=2022-12-31&n=2
    - ![image_2023_06_24T03_38_00_157Z](https://github.com/umesh-sugara/API-Development-Data-Transformation/assets/73294581/a058426b-b9ad-4041-8c95-dbb9a10f8e24)

    - Link : http://127.0.0.1:5000/api/nth_most_total_item?item_by=price&start_date=2022-10-01&end_date=2022-12-31&n=2
      
    - ![image_2023_06_24T03_38_54_982Z](https://github.com/umesh-sugara/API-Development-Data-Transformation/assets/73294581/7dc45a51-459a-42d3-a0d6-cc97d2c3b580)

### Api 3
  - End point : /api/percentage_of_department_wise_sold_items
  - API Use Cases:
    - What is the percentage of sold items (seats) department wise?
    - Expected O/P: {dept_name: x%,……. }
    - Parameters: {start_date: Date, end_date: Date}
    - Link : http://127.0.0.1:5000/api/percentage_of_department_wise_sold_items?start_date=2022-01-01&end_date=2022-12-31
      
    - ![image_2023_06_24T03_41_06_810Z](https://github.com/umesh-sugara/API-Development-Data-Transformation/assets/73294581/995564f9-1183-4626-a0b0-27279757d31a)


### Api 4
  - End point : /api/monthly_sales
  - API Use Cases:
    - How does the monthly sales for any product look like?
    - Expected O/P: [1908.0, … 1952.0] for all 12 months
    - Parameters: {product: String, year:Number}
    - Link : http://127.0.0.1:5000/api/monthly_sales?product=Outplay&year=2022
    
    - ![image_2023_06_24T03_43_39_816Z](https://github.com/umesh-sugara/API-Development-Data-Transformation/assets/73294581/4f762583-dc82-4749-8369-f111dd6fa019)

## Feedback
If you have any feedback, please reach out at umeshsugara9@gmail.com
