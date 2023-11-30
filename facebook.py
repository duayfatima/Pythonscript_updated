import requests
import pyodbc

# API URL
api_url = "https://connectors.windsor.ai/facebook"

# API parameters
api_key = "cb9ffbcf9dedf1ff792a7df99e7ea53120a9"
params = {
    "api_key": api_key,
    "date_preset": "last_7d",
    "select_accounts": "335302090981771",
    "fields": "action_values_omni_purchase,campaign,clicks,cpc,cpm,ctr,date,frequency,impressions,reach,spend,website_purchase_roas_offsite_conversion_fb_pixel_purchase"
}

# Make API request
response = requests.get(api_url, params=params)
data = response.json()
#print(data)

# SQL Server connection parameters
server = "202.61.49.52"
database = "Couriers"
username = "idsDua"
password = "Ideas@123"


# Create connection
connection_string = f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Insert data into SQL Server table
for entry in data['data']:
    insert_query = """
    INSERT INTO FacebookData (action_values_omni_purchase, campaign, clicks, cpc, cpm, ctr, date, frequency, impressions, reach, spend, website_purchase_roas_offsite_conversion_fb_pixel_purchase)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = (
        entry.get("action_values_omni_purchase"),
        entry.get("campaign"),
        entry.get("clicks"),
        entry.get("cpc"),
        entry.get("cpm"),
        entry.get("ctr"),
        entry.get("date"),
        entry.get("frequency"),
        entry.get("impressions"),
        entry.get("reach"),
        entry.get("spend"),
        entry.get("website_purchase_roas_offsite_conversion_fb_pixel_purchase")
    )
    cursor.execute(insert_query, values)
    conn.commit()

# Close connection
conn.close()

print("Data inserted into the SQL Server database.")
