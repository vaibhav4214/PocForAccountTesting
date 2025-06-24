import pandas as pd
from sqlalchemy import create_engine

 # --- Database Configuration (Example: MySQL) ---
    # Replace with your actual database credentials
db_hostname = 'localhost'
db_username = 'root'
db_password = 'root'
db_name = 'employees'
db_table_name = 'emp' # Name of the table to create/update in the database

    # Create a SQLAlchemy engine to connect to the database
    # Adjust the connection string based on your database (e.g., 'postgresql+psycopg2', 'sqlite:///')
db_connection_string = f'mysql+pymysql://{db_username}:{db_password}@{db_hostname}/{db_name}'
engine = create_engine(db_connection_string)

    # --- Excel File Configuration ---
excel_file_path = 'indian_employee_data.xlsx' # Update this path

# try:
        # Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

#         # Upload the DataFrame to the database table
#         # if_exists options: 'fail', 'replace', 'append'
#         # index=False prevents pandas from writing the DataFrame index as a column in the database
# df.to_sql(db_table_name, con=engine, if_exists='replace', index=False)

#     print(f"Data from '{excel_file_path}' successfully imported into table '{db_table_name}' in database '{db_name}'.")

#     except FileNotFoundError:
#         print(f"Error: Excel file not found at '{excel_file_path}'")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the database connection (optional, as engine handles pooling)
#         if 'engine' in locals():
#             engine.dispose()