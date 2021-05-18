import pandas as pd
sales_data=pd.read_csv("grocery_sales.csv")
#fill in missing values
avg_sales=sales_data["sales"].mean()
#use fillna to fill the not assigned number(nan) with any fixed value and inplace it-make that change
sales_data["sales"].fillna(value=avg_sales,inplace=True)
#sum sales by day
sales_summary=sales_data.groupby("transaction_date")["sales"].sum()
#plot sales
sales_summary.plot(rot=30)