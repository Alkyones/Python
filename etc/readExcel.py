import pandas as pd

excel_file_path = 'C:\\Users\\lifeo\\Desktop\\Python\\etc\\Generic Partners.xlsx'
excel_file_path2 = 'C:\\Users\\lifeo\\Desktop\\Python\\etc\\company-tradebase-match.xlsx'


# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)
df2 = pd.read_excel(excel_file_path2)


# Create an empty list to store the array of objects
data, data2 = [], []

# Iterate through the rows of the DataFrame and create objects
for index, row in df.iterrows():
    company_name = row['Company Name']
    anonname = row['AnonName']
    anonlocation = row['AnonLocation']
    code = row['code']

    # Create an object and append it to the list
    data.append({
        'company_name': company_name,
        'anonname': anonname,
        'anonlocation': anonlocation,
        'code': code
    })

   
for index, row in df2.iterrows():
    company_name = row['Company Name']
    code = row['code']

    # Create an object and append it to the list
    data2.append({
        'company_name': company_name,
        'code': code
    })


for rcd in data:
    code = rcd['code']
    companyName = ""
    for r in data2:
        if r['code'] == code:
            companyName = r['company_name']
            rcd["company_name"] = companyName
    
    
        

# Print the list of objects (you can also return or process it as needed)
for item in data:
    print(item,",")
