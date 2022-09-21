#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[10]:


get_ipython().system('pip install --upgrade pyshp')

get_ipython().system('pip install --upgrade shapely')

get_ipython().system('pip install --upgrade descartes')

get_ipython().system('pip install --upgrade geopandas')


# In[3]:


pip install
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

df = pd.read_csv("Geolocation.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['geolocation_lng'], df['geolocation_lat'])]
gdf = GeoDataFrame(df, geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=0.001);


# In[2]:


df1=pd.read_csv("Product Category.csv")
df1.head()


# In[4]:


df2=pd.read_csv("Order Items.csv")
df2.sort_values(by=["order_id"],inplace=True)
df2.head()


# In[5]:


df3=pd.read_csv("Customers.csv")
df3


# In[ ]:





# In[6]:


df4=pd.read_csv("Order Payments.csv")
df4.sort_values(by=["order_id"],inplace=True)
df4.dropna()
# df4.drop(df4[df4["payement_value"]>13000].index,inplace=True,axis=1)
df4=df4[df4["payment_value"]<1000]
df4


# In[42]:



df5=pd.read_csv("Products.csv")
df5.dropna(inplace=True)

series7=df5["product_category_name"]
series7=series7.drop_duplicates()
len(series7)
# df5.isna().sum().sum()


# In[8]:


df6=pd.read_csv("Sellers.csv")
df6


# In[6]:


df7=pd.read_csv("Order Reviews.csv")
df7=df7.sort_values(by=["order_id"])
df7


# In[99]:


df8=pd.read_csv("Orders.csv")
df8.dropna(inplace=True)

# print(df8.isna().sum().sum())
# df8.dropna(inplace=True)

df8.sort_values(by=["order_id"],inplace=True)
# # df8=df8["Time_duration"].astype('float64')

# df8["Time_duration"] = df8["Time_duration"].apply(pd.to_numeric, errors='coerce')

# df8.dropna(inplace=True)
# print(df8.isna().sum().sum())
# # df8=df8[df8["Time_duration"]<100]
df8


# In[104]:


df9=pd.read_csv("Orders2.csv")
df9.dropna(inplace=True)
df9


# In[132]:


final=pd.DataFrame()

final["order_id"]=df8["order_id"]
final["order_status"]=df8["order_status"]
final["order_item_id"]=df2["order_item_id"]
final["review_score"]=df7["review_score"]
final["payment_sequential"]=df4["payment_sequential"]
final["payment_installments"]=df4["payment_installments"]
final["payment_value"]=df4["payment_value"]
final["payment_type"]=df4["payment_type"]
final["Hour"]=df9["Hour_of_purchase"]
final.dropna(inplace=True)
# final.isna().sum().sum()
final["Hour"]=final["Hour"].astype('int64')

# final["payment_value"]=df7[""]








# final.sort_values(by=["order_id"],inplace=True)




# final


# In[ ]:





# In[203]:


# fig,ax=plt.subplots(figsize=(10,10))
# final.plot(x="payment_value",y="payment_installments",kind="bar",ax=ax);
# # plt.xticks(np.arange(0,1000,150));
# # plt.yticks(np.arange(0.1,0.1))


# In[2]:


pip install seaborn


# In[14]:


import seaborn as sns
plt.subplots(figsize=(10,6))
sns.histplot(final["payment_value"])
plt.xticks(np.arange(0,1000,100))
plt.xlabel("Payment Value",fontsize=15)
plt.ylabel("No Of Orders",fontsize=15)
plt.show()


# In[24]:


ds=pd.read_csv("Orders.csv")
ds.dropna(inplace=True)

# print(df8.isna().sum().sum())
# df8.dropna(inplace=True)

ds.sort_values(by=["order_id"],inplace=True)
ds


# In[89]:


series=pd.Series(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

# series
l=[]
for i in series:
    l.append(df8["order_approved_at.2"].value_counts()[i])
l    
series2=pd.Series(l)   
ds=pd.DataFrame({"Months":series,"No of Orders":series2})
ds


# In[93]:


fig,ax=plt.subplots(figsize=(10,5))
ds.plot(x="Months",y="No of Orders",kind="bar",color="lightblue",ax=ax);
ax.axhline(ds["No of Orders"].mean(),linestyle='--')
plt.xticks(fontsize=15,rotation=30);
plt.yticks(fontsize=15,rotation=0);


# In[ ]:





# In[70]:


series3=pd.Series(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# series
l=[]
for i in series3:
    l.append(df8["order_approved_at.1"].value_counts()[i])
l    
series4=pd.Series(l)   
ds2=pd.DataFrame({"Days":series3,"No of Orders":series4})
ds2


# In[97]:


fig,ax=plt.subplots(figsize=(10,5))
ds2.plot(x="Days",y="No of Orders",color="salmon",kind="bar",ax=ax);
ax.axhline(ds2["No of Orders"].mean(),linestyle='--');
plt.xticks(fontsize=15,rotation=0);
plt.yticks(fontsize=15,rotation=0);


# In[155]:


series5=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

l=[]
for i in range(1,24,1):
   
    l.append(final["Hour"].value_counts()[i])
l
series6=pd.Series(l)
ds3=pd.DataFrame({"Hour":series5,"Count of Orders":series6})
ds3["Count of Orders"].fillna(0,inplace=True)
ds3
    



# In[169]:


fig,ax=plt.subplots(figsize=(8,5))
ds3.plot(x="Hour",y="Count of Orders",color="Green",kind="bar",ax=ax);
ax.axhline(ds3["Count of Orders"].mean(),linestyle='--');
plt.xticks(fontsize=15,rotation=90);
plt.xlabel("Delivery Time",fontsize=15);
plt.ylabel("No of Orders",fontsize=15);
plt.yticks(fontsize=15,rotation=0);


# In[179]:


import seaborn as sns
plt.subplots(figsize=(10,6))
sns.histplot(df5["product_description_lenght"])
plt.xticks(np.arange(0,4500,500),fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Product Description",fontsize=15)
plt.ylabel("No Of Orders",fontsize=15)
plt.show()


# In[220]:


import seaborn as sns
plt.subplots(figsize=(10,6))
sns.histplot(df3["customer_city"])
plt.xticks(np.arange(0,13,1),fontsize=15,rotation=90)
plt.xlim(0,13)
plt.yticks(np.arange(0,18000,1000),fontsize=15)
plt.xlabel("Product photos qty",fontsize=1)
plt.ylabel("No Of Orders",fontsize=15)
# fig.savefig('productdescri.jpg')
plt.show()


# In[21]:


import seaborn as sns

df5.sort()
plt.subplots(figsize=(30,5))
sns.histplot(df5["product_category_name"])
plt.xticks(fontsize=15,rotation=90)
# plt.xlim(0,13)
plt.yticks(np.arange(0,4000,500),fontsize=15)
plt.xlabel("Product Category",fontsize=1)
plt.ylabel("No Of Orders",fontsize=15)
# fig.savefig('productdescri.jpg')
plt.show()


# In[44]:


l=[]
for i in series7:
    l.append(df5["product_category_name"].value_counts()[i])
l    


# In[49]:


series8=pd.Series(l)
ds4=pd.DataFrame({"Product category":series7,"Counts of order":l})
ds4.sort_values(by=["Counts of order"],inplace=True)
ds4


# In[61]:


fig,ax=plt.subplots(figsize=(40,10))
ds4.plot(x="Product category",y="Counts of order",ax=ax,kind="bar");
plt.yticks(fontsize=40);
plt.xticks(fontsize=25);

