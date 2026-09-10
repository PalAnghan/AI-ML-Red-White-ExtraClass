import pandas as pd

student_data = {
  'name':['Alice' , 'Bob' , 'Rahul' , 'Amit' , 'vivek' , 'Nihar'],
  'age':[10 , 20 , 20 , 40 , 20 , 60],
  'area':['surat' , 'vadodara' , 'mumbai' , 'pune' , 'USA' , 'Canada'],
  'score': [85, 92, 78, 92, 88 , 90]
}

student_df = pd.DataFrame(student_data)

print(student_df)
'''
#First 2 rows 
print("First 2 Rows:\n",student_df.head(2))

#Last 2 Rows
print("Last 2 Rows:\n",student_df.tail(2))

#Index 
print("Index:\n",student_df.index)

#data type
print("Data Types:\n",student_df.dtypes)

#Column
print("Columns:",student_df.columns)

#info
print("Info:",student_df.info())

print("Statistical Summary:\n",student_df.describe())

#Select columns and rows

print("Name Column: \n", student_df[['name', 'score', 'area']])

print("Second Row:\n",student_df.iloc[2])
print("Second Row:\n",student_df.iloc[0:2])
'''
# Dataframe operations

# Add new column
student_df['email'] = ["exmple1@gmail.com" , "exmple2@gmail.com" , "exmple3@gmail.com" ,"exmple4@gmail.com" , "exmple5@gmail.com"  ,"exmple6@gmail.com"]

print(student_df)

student_df = student_df.drop('area', axis=1)

print(student_df)

ages = student_df[student_df['age'] == 20]

sorted_df = student_df.sort_values(by="name")

print(ages)

print(sorted_df)

# mean()

average_age = student_df['age'].mean()

print(average_age)