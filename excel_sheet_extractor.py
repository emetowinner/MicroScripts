import pandas as pd

# Using the pandas Excel class to raed the excel file load the excel file
data_set = pd.ExcelFile('KPMG_VI_New_raw_data_update_final.xlsx')

sheet = 0  # Sheet counter

# Seperating the sheets and saving them as CSV file
for sheet_name in data_set.sheet_names:
    if sheet <= len(data_set.sheet_names):
        print(f'Reading {data_set.sheet_names[sheet]} to a DataFrame....')
        df = pd.read_excel(data_set, sheet_name)

        name = f'sheet-{sheet}.csv'
        df.to_csv(name)
        """
        ## You can you contional statement to target specific sheet and ignore others. Eg: See below
            if sheet == 2:
                name = 'NewCustomerList.csv'
                df.to_csv(name)
            elif sheet == 3:
                name = 'CustomerDemographic.csv'
                df.to_csv(name)
            elif sheet == 4:
                name = 'CustomerAddress.csv'
                df.to_csv(name)
            else:
                pass
            
        """
        print()
        print(
            f'Saved {data_set.sheet_names[sheet]} as a CSV file with the name {name}')
        sheet += 1
