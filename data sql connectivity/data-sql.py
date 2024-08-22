import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc

server = 'DESKTOP-2O5RLHV'  # replace with your server name
database = 'testing'  # replace with your database name
username = 'sa'  # replace with your username
password = 'RPSsql12345'  # replace with your password

connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-2O5RLHV;'
                            'Database=testing;' 'Trusted_connection=yes;')

def Read(connection):
    cursor = connection.cursor()
    print('Read')
    cursor.execute('SELECT * FROM agencies')
    for row in cursor:
        print(row)
    connection.commit()

Read(connection)

def Write(connection):
    cursor = connection.cursor()
    print('Write')
    name = input('Enter agency Name: ')
    cursor.execute('insert into agencies(name) values(?);', (name))
    Read(connection)
    connection.commit()
    
Write(connection)