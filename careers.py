import pandas as pd
import mysql.connector
from paramiko import SSHClient, AutoAddPolicy

# Connection details
host = '127.0.0.1'
user = 'bi_career_ip'  # Updated username
password = 'iD3@BiC@r33r'  # Updated password
port = 3306
ssh_host = '97.74.84.29'
ssh_user = 'idsadmin'
ssh_password = 'Ide@$390++--'
database = 'jawwad_careers'
table = 'applicant_comments'

# Establish SSH tunnel
print("Establishing SSH tunnel...")
ssh_client = SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(ssh_host, username=ssh_user, password=ssh_password, timeout=10)
print("SSH tunnel established successfully.")

# Connect to MySQL database
print("Connecting to MySQL database...")
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database,
    unix_socket=f'/tmp/mysql.sock'  # Provide the correct path if needed
)
print("Connected to MySQL database successfully.")

# Fetch data from MySQL table
print("Fetching data from MySQL table...")
query = f"SELECT * FROM applicant_comments"
data = pd.read_sql(query, conn)
print("Data fetched successfully.")

# Close the MySQL connection
conn.close()
print("MySQL connection closed.")

# Close the SSH tunnel
ssh_client.close()
print("SSH tunnel closed.")

# Print the fetched data
print("\nFetched Data:")
print(data)
