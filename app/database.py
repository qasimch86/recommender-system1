# Database connection logic goes here
import pandas as pd
from sqlalchemy import create_engine

server = r'WIN-48U8EVMH3JO\SQLEXPRESS'
database = 'PostAgents_Jan11'
username = 'sa'
password = 'SS_ITServices'
driver = 'ODBC Driver 17 for SQL Server'

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)

engine = create_engine(connection_string, fast_executemany=True)

def fetch_orders():
    query = """
    SELECT 
        o.CustomerId,
        p.Id AS ProductId,
        p.Name AS ProductName,
        oi.Quantity,
        o.CreatedOnUtc AS OrderDate
    FROM [Order] o
    JOIN OrderItem oi ON o.Id = oi.OrderId
    JOIN Product p ON oi.ProductId = p.Id
    """
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)
    return df
