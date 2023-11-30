import pandas as pd
import re

# Read the Excel file into a DataFrame
file_path = 'C:\\Users\\Dell E590\\Desktop\\sep\\sepFinal\\SORTED123.xlsx'
df = pd.read_excel(file_path)

# Find duplicate values in the "Rep_phone" column
duplicate_phone_numbers = df[df.duplicated(subset='Rep_phone', keep=False)]

# Create a mapping from duplicate phone numbers to unique identifiers
duplicate_phone_to_id = {}
unique_id_counter = 1

for phone_number in duplicate_phone_numbers['Rep_phone']:
    if phone_number not in duplicate_phone_to_id:
        duplicate_phone_to_id[phone_number] = f'ID_{unique_id_counter}'
        unique_id_counter += 1

# Add a new column 'Unique_ID' to the DataFrame based on the mapping
df['Unique_ID'] = df['Rep_phone'].map(duplicate_phone_to_id)

# Create a new DataFrame with only the duplicate records and assigned IDs
duplicate_records_df = df[df.duplicated(subset='Rep_phone', keep=False)]

# Save the DataFrame with duplicate records to an Excel file
output_file_duplicates = 'C:\\Users\\Dell E590\\Desktop\\sep\\sepFinal\\SORTED123_duplicate_records_with_ids.xlsx'
duplicate_records_df.to_excel(output_file_duplicates, index=False)

# Optionally, you can also print the DataFrame with duplicate records
print("Duplicate Records with Assigned IDs:")
print(duplicate_records_df)
