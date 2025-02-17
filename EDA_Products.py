import pandas as pd

# Load CSV files
products = pd.read_csv("C:/Users/vorug/Downloads/PRODUCTS_TAKEHOME.csv")


import matplotlib.pyplot as plt
import seaborn as sns

# Visualize missing values using a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(products.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Values in Products DataFrame')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

# Count the occurrences of each barcode
barcode_counts = products['BARCODE'].value_counts()

# Filter barcodes that appear more than once
duplicate_barcodes = barcode_counts[barcode_counts > 1]

# Plot the duplicate barcodes
plt.figure(figsize=(15, 6))
duplicate_barcodes.plot(kind='bar', color='skyblue')
plt.title('Frequency of Duplicate Barcodes')
plt.xlabel('Barcode')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# Count the occurrences of each brand
brand_counts = products['BRAND'].value_counts()

# Plot the brand distribution
plt.figure(figsize=(12, 6))
brand_counts.plot(kind='bar', color='coral')
plt.title('Distribution of Brands in Products DataFrame')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()




# Count exact duplicates (all columns are identical)
exact_duplicates_count = products.duplicated(keep="first").sum()

print(f"Exact duplicate rows in Products table: {exact_duplicates_count}")

# Drop exact duplicates (all columns must be identical)
products.drop_duplicates(keep="first", inplace=True)

# Verify the number of remaining rows after dropping duplicates
print(f"Remaining rows after dropping exact duplicates: {products.shape[0]}") 

# Count duplicate barcodes (considering only the BARCODE column)
duplicate_barcodes_count = products["BARCODE"].duplicated(keep="first").sum()

print(f"Total duplicate barcodes: {duplicate_barcodes_count}")


print(products.head())
# Calculate percentage of missing values in the 'BRAND' column
missing_brand_percentage = (products["BRAND"].isnull().sum() / len(products)) * 100

print(f"Percentage of missing values in BRAND column: {missing_brand_percentage:.2f}%")
print(products.columns)


def impute_by_category(series):
    mode_value = series.mode()
    return series.fillna(mode_value[0] if not mode_value.empty else "Unknown")

products["BRAND"] = products.groupby(["CATEGORY_1", "CATEGORY_2", "CATEGORY_3", "CATEGORY_4"])["BRAND"].transform(impute_by_category)

# Step 2: If BRAND is still missing, fill it based on the most common brand within the same manufacturer
products["BRAND"] = products.groupby("MANUFACTURER")["BRAND"].transform(impute_by_category)

# Step 3: If BRAND is still missing, fill with the most common brand in the dataset
products["BRAND"].fillna(products["BRAND"].mode()[0], inplace=True)



# Calculate percentage of missing values in the 'BRAND' column
missing_brand_percentage2 = (products["BRAND"].isnull().sum() / len(products)) * 100
print(f"Percentage of missing values in BRAND column: {missing_brand_percentage2:.2f}%")


# Find barcodes that have duplicates
duplicate_barcodes_list = products["BARCODE"].value_counts()
duplicate_barcodes = duplicate_barcodes_list[duplicate_barcodes_list > 1].index.tolist()

# Convert to a DataFrame for better readability
duplicate_barcodes_df = pd.DataFrame({"Duplicate_Barcodes": duplicate_barcodes})

print(duplicate_barcodes_df)

# Find barcodes that have duplicates with different CATEGORY_1 values
duplicate_barcode_category = products.groupby("BARCODE")["CATEGORY_1"].nunique()

# Filter only barcodes that have more than one unique CATEGORY_1
duplicate_barcode_category = duplicate_barcode_category[duplicate_barcode_category > 1].index

# Retrieve the full records for these barcodes
duplicate_barcode_category_df = products[products["BARCODE"].isin(duplicate_barcode_category)]

print(duplicate_barcode_category_df)

products = products.dropna(subset=['CATEGORY_3'])

missing_percentage4 = products["CATEGORY_4"].isna().mean() * 100
print(f"Percentage of missing values in {missing_percentage4}: {missing_percentage4:.2f}%")

missing_percentage3 = products["CATEGORY_3"].isna().mean() * 100
print(f"Percentage of missing values in {missing_percentage3}: {missing_percentage3:.2f}%")

missing_percentage2 = products["CATEGORY_2"].isna().mean() * 100
print(f"Percentage of missing values in {missing_percentage2}: {missing_percentage2:.2f}%")

missing_percentage1 = products["CATEGORY_1"].isna().mean() * 100
print(f"Percentage of missing values in {missing_percentage1}: {missing_percentage2:.2f}%")

missing_percentage_brand = products["BRAND"].isna().mean() * 100
print(f"Percentage of missing values in 'brand': {missing_percentage_brand:.2f}%")

unknown_percentage = (products['BRAND'].str.lower() == 'unknown').mean() * 100
print(f"Percentage of records with 'unknown' in brand: {unknown_percentage:.2f}%")

# Remove the 'CATEGORY_4' column in place
products.drop(columns=['CATEGORY_4'], inplace=True)

import numpy as np

products['BRAND'].replace('Unknown', np.nan, inplace=True)


# Perform hot-deck imputation using forward-fill within each CATEGORY_1, CATEGORY_2, and CATEGORY_3 group
products['BRAND'] = products.groupby(['CATEGORY_1', 'CATEGORY_2', 'CATEGORY_3'])['BRAND'].ffill()

# If there are still missing values, use backward-fill as a fallback
products['BRAND'] = products.groupby(['CATEGORY_1', 'CATEGORY_2', 'CATEGORY_3'])['BRAND'].bfill()

missing_percentage_brand = products["BRAND"].isna().mean() * 100
print(f"Percentage of missing values in 'brand': {missing_percentage_brand:.2f}%")




export_path="C:/Users/vorug/Downloads/products_cleaned2.csv"
products.to_csv(export_path, index=False)




