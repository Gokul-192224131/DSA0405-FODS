import numpy as np
import pandas as pd

#pip install openpyxl(to read the excel file)

path = "D:/FODS/7_house_data.scv.xlsx"
data = pd.read_excel(path)
house_data = data.to_numpy()
bedroom = 1
sales_price = -1
more_than_four_bed = house_data[:,bedroom]>4
sales_more_than_four_bed = house_data[more_than_four_bed,sales_price]
avg = np.mean(sales_more_than_four_bed)
print("The Average Sales prices : ",avg)

