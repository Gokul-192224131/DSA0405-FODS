import pandas as pd
data = {
    'Product': ['Mi', 'Realme', 'Apple', 'Poco', 'Moto', 'Samsung', 'Blackberry'],
    'Quantity': [10, 8, 5, 20, 45, 33, 22],
    'Revenue': [10000, 15000, 350000, 45000, 60000, 12000, 47000]
}
sales_data = pd.DataFrame(data)
product_sales = sales_data.groupby('Product')['Quantity'].sum()
sorted_products = product_sales.sort_values(ascending=False)
top_products = sorted_products.head(5)
print("Top 5 Products Sold the Most:")
print(top_products)
