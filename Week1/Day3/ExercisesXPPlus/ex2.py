'''
🌟 Exercise 2 : Advanced Data Manipulation and Analysis
Instructions
In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.



sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]


Tasks:
Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

Sales Data Enhancement:

Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
Use a loop to modify the sales_data list with this new information.
High-Value Transactions:

Using list comprehension, create a list of all transactions where the total price is greater than $500.
Sort this list by the total price in descending order.
Customer Loyalty Identification:

Identify any customer who has made more than one purchase, suggesting potential loyalty.
Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.
Bonus: Insights and Analysis:

Calculate the average transaction value for each product category.
Identify the most popular product based on the quantity sold.
Provide insights into how these analyses could inform the company’s marketing strategies.
'''
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Step 1: Calculate total sales for each product
prod_rev = {}
cust_spend = {}

for el in sales_data:
    product = el['product']
    revenue = el['price'] * el['quantity']
    
    if product not in prod_rev:
        prod_rev[product] = revenue
    else:
        prod_rev[product] += revenue

print("Total Sales for Each Product:", prod_rev)

# Step 2: Calculate total spending for each customer
for el in sales_data:
    customer = el['customer_id']
    money_spent = el['price'] * el['quantity']
    
    if customer not in cust_spend:
        cust_spend[customer] = money_spent
    else:
        cust_spend[customer] += money_spent

print("Total Spending for Each Customer:", cust_spend)

# Step 3: Add 'total_price' to each transaction
for el in sales_data:
    total_price = el['price'] * el['quantity']
    el['total_price'] = total_price

print("Sales Data with 'total_price':", sales_data)

# Step 4: Identify high-value transactions
high_value_transactions = [el for el in sales_data if el['total_price'] > 500]
high_value_transactions.sort(key=lambda x: x['total_price'], reverse=True)
print("High-Value Transactions:", high_value_transactions)

# Step 5: Identify loyal customers
purchase_count = {}
loyal_customers = []

for el in sales_data:
    customer = el['customer_id']
    
    if customer not in purchase_count:
        purchase_count[customer] = 1
    else:
        purchase_count[customer] += 1

# Customers with more than one purchase
loyal_customers = [customer for customer, count in purchase_count.items() if count > 1]

print("Loyal Customers:", loyal_customers)

# Bonus: Insights and Analysis

# Calculate the average transaction value for each product category
avg_transaction_value = {product: total / sum([1 for el in sales_data if el['product'] == product]) for product, total in prod_rev.items()}
print("Average Transaction Value for Each Product:", avg_transaction_value)

# Identify the most popular product based on the quantity sold
product_quantities = {}

for el in sales_data:
    product = el['product']
    if product not in product_quantities:
        product_quantities[product] = el['quantity']
    else:
        product_quantities[product] += el['quantity']

most_popular_product = max(product_quantities, key=product_quantities.get)
print("Most Popular Product:", most_popular_product)
