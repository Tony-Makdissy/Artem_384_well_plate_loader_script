# Echo 550 Liquid Handler Transfer Table Generator

This script is used to generate a transfer table for the Echo 550 liquid handler. It reads an XLSX file and generates a CSV file that contains the transfer table.

## Usage

1. Set the configuration parameters at the beginning of the script to match your requirements. These parameters include the default names for the source and destination plates, the default transfer volume, and the number of source wells per destination well.

2. Specify the path to your XLSX file in the `xlsx_file_path` variable.

3. Run the script. The script will read the XLSX file, generate the transfer table, and save it as a CSV file named "transfer_table.csv".

## Input

The input to the script is an XLSX file that contains two sheets, "Source plate Map" and "Destination plate Map". Both sheets should start at C2 and resemble a 384-well plate.

The "Source plate Map" sheet should contain the names of the source wells, and the "Destination plate Map" sheet should contain the names of the destination wells.

## Output

The output of the script is a CSV file named "transfer_table.csv". This file contains the following columns:

- Source Plate: the name of the source plate
- Source Well: the name of the source well
- Compound: the name of the compound in the source plate
- Destination Plate: the name of the destination plate
- Transfer Volume: the volume to be transferred from the source well to the destination well

**NOTES:** I have `source_plate_volumes.csv` new to the output, will document it later!

## Notes

If you set the `number_of_source_wells` variable to a specific number (other than -1), the script will raise an error if the number of source wells for a destination well does not match this number. To allow an arbitrary number of source wells, set `number_of_source_wells` to `-1`.
- Destination Well: the name of the destination well
- Transfer Volume: the volume to be transferred from the source well to the destination well

## Notes

If you set the `number_of_source_wells` variable to a specific number (other than -1), the script will raise an error if the number of source wells for a destination well does not match this number. To allow an arbitrary number of source wells, set `number_of_source_wells` to `-1`.