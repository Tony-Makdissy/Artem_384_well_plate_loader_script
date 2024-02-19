"""
Written by: Tony MAKDISSY, Artem DEGTIAR
Last update: 2024-02-15 

This script is used to generate a transfer table for the Echo 550 liquid handler.
The script reads an XLSX file and generates a CSV file that contains the transfer table.
The XLSX file should contain two sheets, "Source plate Map" and "Destination plate Map".

The output CSV file contains the following columns:
- Source Plate: the name of the source plate
- Source Well: the name of the source well
- Destination Plate: the name of the destination plate
- Destination Well: the name of the destination well
- Transfer Volume: the volume to be transferred from the source well to the destination well

NOTES FOR USAGE:
you have to manually set the first two blocks of the code to match your file
- Configratraion
- Read the xlsx file, MIGHT NEED TO TWEEK IT FOR YOUR OWN FILE
"""

import pandas as pd

######  Configratraion ########
source_plate_default = "Source1"  # Default name for the source plate
destination_plate_default = "Dest1"  # Default name for the destination plate
transfer_volume_default = 500  # Default transfer volume
number_of_source_wells = 2  # Number of source wells per destination well. Set to -1 for arbitrary number of source wells
############################

##### Read the xlsx file, MIGHT NEED TO TWEEK IT FOR YOUR OWN FILE ######
# Specify the path to your XLSX file
xlsx_file_path = "AD 03-19 primers.xlsx"

# Read the XLSX file and access the "Source plate Map" sheet
source_plate = pd.read_excel(xlsx_file_path, sheet_name=2, skiprows=1, usecols="C:Z", nrows=19)
destination_plate = pd.read_excel(xlsx_file_path, sheet_name=3, skiprows=1, usecols="C:Z", nrows=19)
# both sheets start at C2, and resemble a 384 well plate
###########################################################################

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_source_well(destination_well):
    """
    Get the source wells corresponding to a destination well.
    """
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

transfer_table_columns = ["Source Plate", "Source Well", "Destination Plate", "Destination Well", "Transfer Volume"]
transfer_table = pd.DataFrame(columns=transfer_table_columns)

for i in range(destination_plate.shape[0]):
    for j in range(destination_plate.shape[1]):
        if pd.isna(destination_plate.iloc[i, j]):
            continue
        if type(destination_plate.iloc[i, j]) != str:
            continue
        
        source_wells = get_source_well(destination_plate.iloc[i, j])

        if number_of_source_wells != -1 and len(source_wells) != number_of_source_wells:
            raise ValueError(f"You set the number of source wells for each destination well to be {number_of_source_wells}, but the number of source wells for the destination well {destination_plate.iloc[i, j]} is {len(source_wells)}. Please check the source plate map or set the number_of_source_wells to -1 to allow an arbitrary number of source wells.")

        for source_well in source_wells:
            transfer_table = transfer_table._append({
                "Source Plate": source_plate_default,
                "Source Well": source_well,
                "Destination Plate": destination_plate_default,
                "Destination Well": f"{ALPHABET[i]}{j+1}",
                "Transfer Volume": transfer_volume_default
            }, ignore_index=True)

transfer_table.to_csv("transfer_table.csv", index=False)