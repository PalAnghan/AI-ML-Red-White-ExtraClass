import pandas as pd

print("Pandas Version: ",pd.__version__)

# Series : alphabatiacl arrange like a,b,c,d.....
fruits = pd.Series(['Apple', 'Banana', 'BlueBerry', 'Cherry', 'Mango'])
print(fruits)

# Index : custom labels for series

colors = pd.Series(['red' , 'blue' , 'white' , 'purple' , 'red'] , index=['color1' , 'color2' , 'color3' , 'color4' , 'color5'])

result = colors.to_string(index=False)
print(result)
print(colors.values)
print(colors.tolist())

# iloc  = access data using integer position
print(colors.iloc[1]) # 1 is index value 

# loc = access data using index
print(colors.loc['color3'])

#len = find number of elements
print(len(colors))

# unique = return unique value

print(colors.unique()) # remove value dupliacte 

print(colors.nunique()) # only uniq value number return

# value counts() = return the total value how much time like if a vale same as two time so in return 2

print(colors.value_counts())

# DATAFRAMES

student_data = {
  'name':['Pal' , 'Shrey' , 'Nihar' , 'Amit'],
  'age':[10 , 20 , 30 , 40],
  'area':['surat' , 'vadodara' , 'mumbai' , 'pune']
}

df = pd.DataFrame(student_data)

print(df)



