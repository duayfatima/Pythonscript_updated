import pymysql
from sshtunnel import SSHTunnelForwarder
from paramiko import RSAKey
import pandas as pd

# SSH configuration
ssh_host = '97.74.84.29'
ssh_port = 22
ssh_user = 'idsadmin'
ssh_password = 'Ide@$390++--'
ssh_key_path = 'C:/Users/Dell E590/Desktop/career/id_rsa'  # Update with the path to your private key

# MySQL database configuration
db_host = '127.0.0.1'
db_port = 3306
db_user = 'bi_career'
db_password = 'iD3@BiC@r33r'
db_name = 'jawwad_careers'
table_name = 'applicant_comments'

# Establish SSH tunnel
with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_password=ssh_password,
    ssh_pkey=RSAKey(filename=ssh_key_path),
    remote_bind_address=(db_host, db_port)
) as tunnel:
    # Connect to MySQL database through the SSH tunnel
    connection = pymysql.connect(
        host='127.0.0.1',
        port=tunnel.local_bind_port,
        user=db_user,
        password=db_password,
        db=db_name
    )

    try:
        # Perform your database operations here

        query = f'SELECT * FROM applicant_comments'
        df = pd.read_sql_query(query, connection)

        # Print the DataFrame
        print(df)

    finally:
        # Close the MySQL connection
        connection.close()
