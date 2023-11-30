import pandas as pd
import pymysql
from sshtunnel import SSHTunnelForwarder
from paramiko import RSAKey
import io

# SSH configuration
ssh_host = '97.74.84.29'
ssh_port = 22
ssh_user = 'idsadmin'
ssh_password = 'Ide@$390++--'
ssh_key_string = """-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----"""

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
    ssh_pkey=RSAKey(file_obj=io.StringIO(ssh_key_string)),
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
        # Perform your database operations and store the result in a DataFrame
        query = f'SELECT * FROM {table_name}'
        df = pd.read_sql_query(query, connection)

        # Print the DataFrame
        print(df)

        # You can now use the DataFrame 'df' for further analysis or processing

    finally:
        # Close the MySQL connection
        connection.close()
