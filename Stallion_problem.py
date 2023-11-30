import datetime
import requests

# Calculate dynamic date ranges
current_date = datetime.date.today()
from_date = current_date - datetime.timedelta(days=90)
to_date = current_date - datetime.timedelta(days=1)

# Format dates in the desired format ("YYYY-MM-DD")
from_date_str = from_date.strftime('%Y-%m-%d')
to_date_str = to_date.strftime('%Y-%m-%d')

# Construct the request body
request_body = {
    "FromDate": from_date_str,
    "ToDate": to_date_str
}

# Make the API request
url = "https://bitrix.pk/Rest/Stallion/Get_Parcel_Position"
response = requests.post(url, json=request_body)

# Print the response (for demonstration purposes)
print(response.json())
