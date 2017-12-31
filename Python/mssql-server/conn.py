
# test connecting to a sql server using python
# https://www.continuum.io/blog/developer-blog/anaconda-easy-button-microsoft-sql-server-and-python

import pyodbc


conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};' +
    ('SERVER={server},{port};'   +
     'DATABASE={database};'      +
     'UID={username};'           +
     'PWD={password}').format(
            server= 'bciqdevsqlserver.database.windows.net',
              port= 1433,
          database= 'BCIQ_DW',
          username= 'bc',
          password= 'eQUAP22yukM3!')
)
