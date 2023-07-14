import pandas as pd

df = pd.read_excel('assets/cars-2023.xlsx')

# print(df)

# Print columns names and the type
for col in df.columns:
    print("Column Name:", col, "| Column Type", type(df[col][1]))

brand_column = df.columns[0]
# print(brand_column)

row_label_1 = df.loc[0]  # Access row with label/index 0
row_label_2 = df.loc[1]  # Access row with label/index 1

# print("Row based on label/index:")
# print(row_label_1)
# print(row_label_2)

# Iterate over the rows and save data in an array of objects (dictionaries)
objects_array = []
for index, row in df.iterrows():
    obj = {
        'Marca': row[0],
        'Modelo': row[1],
        'Precio': row[2]
    }
    objects_array.append(obj)

# Print the array of objects, ROWS
# for obj in objects_array:
#     print(obj)

print("Number of rows that are in the first sheet: " + str(len(objects_array)))    
