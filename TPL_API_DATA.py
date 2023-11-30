import requests
import pyodbc
from datetime import datetime, timedelta

# Calculate date ranges
current_date = datetime.now()
#to_date = (current_date - timedelta(days=31)).strftime("%Y-%m-%d")
#from_date = (current_date - timedelta(days=31)).strftime("%Y-%m-%d")

# API URL and request payload
api_url = "http://api.withrider.com/rider/v2/GetMerchantPaymentReport"
headers = {"Content-Type": "application/json"}
payload = {
    "fromDate":"2023-06-01",
    "toDate":"2023-06-30",
    #"fromDate": from_date,
    #"toDate": to_date,
    "loginId": 91,
    "apikey": "PEB@UfqE7Z7Vb$ZT4Bmn0jub4@Xk7$!k)ETiVQeewxJ87oNgCZ2y0E$FjAgYxfL!"
}

try:
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
        # SQL Server credentials
    server = "192.168.161.250,57398"
    database = "Couriers"
    username = "sa"
    password = "Ideas@1234"

    # Establish database connection
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Iterate through the API response and insert data into the database
    for item in data:
        query = """
        INSERT INTO COURIER_TPL_DATA (BookingDate, ConsignmentNumber, DeliveryStatus, StatusChangeDate, PaymentStatus, PaymentDate, NetAmount, ServiceCharges, ParcelWeight, DestCity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            item["BookingDate"],
            item["ConsignmentNumber"],
            item["DeliveryStatus"],
            item["StatusChangeDate"],
            item["PaymentStatus"],
            item["PaymentDate"],
            item["NetAmount"],
            item["ServiceCharges"],
            item["ParcelWeight"],
            item["DestCity"]
        ))
        connection.commit()

    # Close the connection
    connection.close()

    print("Data inserted into the database successfully.")


        
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
    data = []  # Set an empty data list to continue the work


