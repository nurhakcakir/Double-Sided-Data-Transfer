Guide for Transferring Data from Database to Excel and from Excel to Database
This Python script assists you in transferring data from a specified table in a PostgreSQL database to an Excel file, adding data from an Excel file to a PostgreSQL database, and printing data from an Excel file to the screen.

This Python script assists you in transferring data from a specified table in a PostgreSQL database to an Excel file, adding data from an Excel file to a PostgreSQL database, and printing data from an Excel file to the screen.

Usage:
1. Open the Terminal or Command Prompt. Navigate to the directory where your requirements.txt file is located. This is typically the main directory of your project. Use the following command to install the packages listed in the requirements.txt file: "pip install -r requirements.txt".

2. Configure Connection Information: Update the database connection information in the config.py file.
database_name = "dbname"
user = "username"
password = "passw0rd"
host = "localhost"
port = 5432

3.Specify Excel Files and Table Settings: Specify the names of the Excel files to be created and the PostgreSQL table names using the file_path1, file_path2, table_name1, and table_name2 variables in the config.py file.
file_path1 = "to_account_move.xlsx"
file_path2 = "to_account_move_line.xlsx"
table_name1 = "account_move"
table_name2 = "account_move_line"

4.Transfer Data from Database to Excel: Run the from_database_to_excel_data_entry.py file to transfer the specified table from the PostgreSQL database to an Excel file.
python from_database_to_excel_data_entry.py

5.Transfer Data from Excel to Database: Run the from_excel_to_database_data_entry.py file to add data from the Excel file to the PostgreSQL database.
Transfer Data from Excel to Database: Run the from_excel_to_database_data_entry.py file to add data from the Excel file to the PostgreSQL database.

6.Print Data from Excel Files to the Screen:First, modify the following values in the config.py file according to your preferences: 
sheet_name="Sheet1"
start_row=0
finish_row=4
start_column=0
finish_column=70
excel_path ="to_account_move.xlsx"
and after Run the print_excel_screen.py file to print the specified data from the Excel file to the screen.
python print_excel_screen.py

Notes:
-It is recommended to run data transfer operations from the database to Excel and from Excel to the database separately.
-Ensure that the connection information is correct.



