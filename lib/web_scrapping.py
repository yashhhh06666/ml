import requests
import pandas as pd
import matplotlib.pyplot as plt

#  API url

url = https://jsonplaceholder.typicode.com/comments

#  Step 2 Collect data from api

response = requests.get(url)

if response.status_code == 200:
    data = requests.json()

    print("Data collected")

else:
    print("Error collecting")

    exit()

#  Convert API data into dataframes

df = pd.DataFrame(data)

print("\n First 10 Rexord ")
print(df.head(10))

#  select useful coloums

df = df[
    {"id","name","email","body"}

]

#  Rename Coloum 

df.colums =[
    "ID",
    "Customer_NAme",
    "Email",
    "Review"
]
#  Basic Data cleaning

# Remove Duplicate records
df = df.drop_duplicates()

#Remove missing Values
df = df.dropna()  

# Convert review text to lowercase
df["Review"] = df["Review"].str.lower()

#  Display DAta
print("\nCleaned DAtaset ")

print(df.head(10))

print ("\n Number of records", len(df))

#  Save data to csv

df.to_csv (
    "Customer_reviews.csv",
    index=False
)

#  Cclculate Reviwe 

df["Review"] = df["Review"].str.len()

#  Visulation 

plt.figure(figsize=(10,5))

plt.hist(
    df["Review_Length"],
    bins = 20 
)

plt.xlable("Review Length")
plt.ylabel("number of Review")

plt.title(
    "Distributon of customer Review length"

)

plt.grid(True)
plt.show()