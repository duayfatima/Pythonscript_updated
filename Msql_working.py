import pandas as pd
import pymysql
import paramiko

# Database credentials
db_host = '127.0.0.1'
db_user = 'reporter'
db_password = 'iJ1oshie5Aich3Se'
db_port = 3306

# SSH credentials
ssh_host = 'ssh.ap-3.magento.cloud'
ssh_user = '1.ent-alemqossuhjio-production-vohbr3y'
private_key_path = r"C:\Users\Dell E590\Desktop\apk\mykey.ppk"

# Database and table information
database_name = 'alemqossuhjio'
table_name = 'amasty_acart_history'

# MySQL query
query = f'SELECT * FROM {table_name};'

# Create an SSH tunnel
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey(filename=private_key_path)
ssh_client.connect(ssh_host, username=ssh_user, pkey=private_key)

# Connect to MySQL through the SSH tunnel
connection = pymysql.connect(host=db_host, user=db_user, password=db_password,
                             port=db_port, database=database_name,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    # Display the DataFrame (for testing purposes)
    print(df)

finally:
    # Close the MySQL connection
    connection.close()

    # Close the SSH tunnel
    ssh_client.close()

