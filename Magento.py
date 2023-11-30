import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
import pandas as pd

# SSH Connection Details
ssh_host = 'ssh.ap-3.magento.cloud'
ssh_user = '1.ent-alemqossuhjio-production-vohbr3y'
ssh_port = 22
local_port = 3307  # Local port to use for the tunnel
private_key_path = 'C:/Users/Dell E590/Desktop/apk/id_rsa.pem'  # Update with your PPK file path

# MySQL Connection Details
mysql_host = '127.0.0.1'
mysql_user = 'reporter'
mysql_password = 'iJ1oshie5Aich3Se'
mysql_port = 3306  # Default MySQL port
mysql_db = 'alemqossuhjio'

# Load private key
private_key = paramiko.RSAKey(filename=private_key_path)

# Establish SSH Tunnel
with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_pkey=private_key,
    remote_bind_address=(mysql_host, mysql_port),
    local_bind_address=('0.0.0.0', local_port)
) as tunnel:

    # Connect to MySQL through the SSH tunnel
    connection = pymysql.connect(
        host='127.0.0.1',
        port=tunnel.local_bind_port,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )

    # Perform your database operations here
    query = "SELECT * FROM amasty_acart_history"
    df = pd.read_sql_query(query, connection)

    excel_file_path = 'C:/Users/Dell E590/Desktop/excel/amasty_acart_data.xlsx'
    df.to_excel(excel_file_path, index=False, mode='w')

    print(df)

    # Close the MySQL connection
    connection.close()
