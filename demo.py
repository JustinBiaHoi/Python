import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server}; SERVER=IBUYLOLI\\SQLEXPRESS;DATABASE=QLMonAn; Trusted_Connection=yes"
)
cursor = conn.cursor()
cursor.execute("SELECT @@version")

db_version = cursor.fetchone()
conn.close()
print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản ", db_version)
