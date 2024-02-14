import pandas as pd

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Specify the path to your XLSX file
xlsx_file_path = "AD 03-19 primers.xlsx"

# Read the XLSX file and access the "Source plate Map" sheet
source_plate = pd.read_excel(xlsx_file_path, sheet_name=2, skiprows=1, usecols="C:Z", nrows=19)
destination_plate = pd.read_excel(xlsx_file_path, sheet_name=3, skiprows=1, usecols="C:Z", nrows=19)


def get_source_well(destination_well):
    list_of_source_wells = [x.strip() for x in destination_well.split("+")]
    source_wells = []

    for i in range(source_plate.shape[0]):
        for j in range(source_plate.shape[1]):
            if pd.isna(source_plate.iloc[i, j]):
                continue
            if type(source_plate.iloc[i, j]) != str:
                continue


            if source_plate.iloc[i, j].strip() in list_of_source_wells:
                source_wells.append(f"{ALPHABET[i]}{j+1}")
    return source_wells

for i in range(destination_plate.shape[0]):
    for j in range(destination_plate.shape[1]):
        if pd.isna(destination_plate.iloc[i, j]):
            continue
        if type(destination_plate.iloc[i, j]) != str:
            continue
        
        temp = get_source_well(destination_plate.iloc[i, j])
        if len(temp) != 2:
            print(temp,destination_plate.iloc[i, j])
