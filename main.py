from flask import Flask,jsonify,request
import api
import json

app=Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the API Development and Data Transformation Project'



@app.route('/api/total_items')
def total_items_api():
    start_date=request.args.get("start_date")
    end_date=request.args.get("end_date")
    department=request.args.get("department")
    items = api.total_items(start_date, end_date, department)
    return jsonify(items)




@app.route('/api/nth_most_total_item')
def nth_most_total_item_api():
    # return 'U r in 2nd function'
    item_by=request.args.get("item_by")
    start_date=request.args.get("start_date")
    end_date=request.args.get("end_date")
    n=int(request.args.get("n"))
    nth_item = api.nth_most_total_item(item_by, start_date, end_date, n)
    return jsonify(nth_item)






@app.route('/api/percentage_of_department_wise_sold_items')
def percentage_of_department_wise_sold_items_api():
    start_date=request.args.get("start_date")
    end_date=request.args.get("end_date")
    sold_items_percentages=api.calculate_sold_items_percentage(start_date, end_date)
    return jsonify(sold_items_percentages)




@app.route('/api/monthly_sales')
def monthly_sales_api():
    product = request.args.get("product")
    year = int(request.args.get("year"))
    sales=api.calculate_monthly_sales(product, year)
    return jsonify(sales)






app.run(debug=True)