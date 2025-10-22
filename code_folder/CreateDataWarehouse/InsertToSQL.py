import pyodbc
from faker import Faker
import random
from datetime import datetime, timedelta

server = "pt"
port = 1433
user = "iya"
password = "P@1"
database = "asset-management-test"
# Establish connection to MySQL database
db = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER='+server+';'
    'DATABASE='+database+';'
    'UID='+user+';'
    'PWD='+password+';'
)

cursor = db.cursor()
#
def create_tables():
    f= open("SQL/create_tables.sql")
    cursor.execute(f.read())

def create_views():
    f= open("SQL/create_views_sql.sql")
    cursor.execute(f.read())

def create_sp():
    f= open("SQL/stored_procedures.sql")
    cursor.execute(f.read())

# create_tables()


# Initialize Faker for generating fake data
fake = Faker()

# Constants for generating large datasets
# NUM_CLIENTS = 100000  # Number of clients
# NUM_ADVISORS = 1000  # Number of advisors
# NUM_ACCOUNTS = 200000  # Number of accounts
# NUM_ASSETS = 10000  # Number of assets
# NUM_TRANSACTIONS = 500000  # Number of transactions
# NUM_PORTFOLIOS = 100000  # Number of portfolios
# NUM_PORTFOLIO_ASSETS = 300000  # Number of portfolio assets
# NUM_PROJECTIONS = 200000  # Number of projections

# Constants for generating large datasets
NUM_CLIENTS = 1000  # Number of clients
NUM_ADVISORS = 100 # Number of advisors
NUM_ACCOUNTS = 2000 # Number of accounts
NUM_ASSETS = 1000 # Number of assets
NUM_TRANSACTIONS = 5000  # Number of transactions
NUM_PORTFOLIOS = 1000  # Number of portfolios
NUM_PORTFOLIO_ASSETS = 3000# Number of portfolio assets
NUM_PROJECTIONS = 2000  # Number of projections

# Insert Advisors -- DONE
# for _ in range(NUM_ADVISORS):
#     name = fake.name()
#     contact_info = fake.phone_number()
#     cursor.execute(
#         "INSERT INTO Advisors (Name, ContactInfo) VALUES (?, ?)",
#         (name, contact_info)
#     )
# db.commit()

# Insert Clients -- DONE
for i in range(NUM_CLIENTS):
    print(i)
    name = fake.name()
    contact_info = fake.phone_number()
    advisor_id = random.randint(1, NUM_ADVISORS)
    risk_profile = random.choice(['High', 'Medium', 'Low'])
    cursor.execute(
        "INSERT INTO Clients (Name, ContactInfo, AdvisorID, RiskProfile) VALUES (?, ?, ?, ?)",
        (name, contact_info, advisor_id, risk_profile)
    )
db.commit()
#
#Insert Accounts -- DONE
for _ in range(NUM_ACCOUNTS-91000):
    print(_)
    try:
        account_type = random.choice(['Savings', 'Checking', 'Investment'])
        client_id = random.randint(97057, 97057 + NUM_CLIENTS)
        cursor.execute(
            "INSERT INTO Accounts (AccountType, ClientID) VALUES (?, ?)",
            (account_type, client_id)
        )
        if _ % 1000 == 0:
            db.commit()
    except Exception as e:
        print(e)
        db.commit()
        continue
db.commit()
#
# Insert Assets -- DONE
for _ in range(NUM_ASSETS):
    print(_)
    name = fake.company()
    asset_type = random.choice(['Stock', 'Bond', 'Real Estate', 'Commodity', 'Cash'])
    current_value = round(random.uniform(10, 1000), 2)
    cursor.execute(
        "INSERT INTO Assets (Name, AssetType, CurrentValue) VALUES (?, ?, ?)",
        (name, asset_type, current_value)
    )
db.commit()

# Insert Portfolios -- DONE
for _ in range(NUM_PORTFOLIOS):
    client_id = random.randint(1, NUM_CLIENTS)
    name = f"Portfolio {fake.word()}"
    risk_level = random.choice(['High', 'Medium', 'Low'])
    cursor.execute(
        "INSERT INTO Portfolios (ClientID, Name, RiskLevel) VALUES (?, ?, ?)",
        (client_id, name, risk_level)
    )
db.commit()

# Insert PortfolioAssets
for _ in range(NUM_PORTFOLIO_ASSETS):
    portfolio_id = random.randint(1, NUM_PORTFOLIOS)
    asset_id = random.randint(1, NUM_ASSETS)
    allocation = round(random.uniform(1, 100), 2)
    cursor.execute(
        "INSERT INTO PortfolioAssets (PortfolioID, AssetID, Allocation) VALUES (?, ?, ?)",
        (portfolio_id, asset_id, allocation)
    )
db.commit()
#
# # Insert Transactions
start_date = datetime(2020, 1, 1)
for _ in range(NUM_TRANSACTIONS-44000-54000-8000-73700):
    print(_)
    try:
        account_id = random.randint(1993, NUM_ACCOUNTS+1993)
        asset_id = random.randint(15, NUM_ASSETS+14)
        date = start_date + timedelta(days=random.randint(1, 365 * 4))
        transaction_type = random.choice(['Buy', 'Sell', 'Deposit', 'Withdraw'])
        amount = round(random.uniform(100, 10000), 2)
        cursor.execute(
            "INSERT INTO Transactions (AccountID, AssetID, Date, Type, Amount) VALUES (?, ?, ?, ?, ?)",
            (account_id, asset_id, date, transaction_type, amount)
        )
    except Exception as e:
        print(e)
        db.commit()
        continue
db.commit()

# Insert Projections
for _ in range(NUM_PROJECTIONS):
    portfolio_id = random.randint(1, NUM_PORTFOLIOS)
    future_value = round(random.uniform(1000, 100000), 2)
    projection_date = start_date + timedelta(days=random.randint(1, 365 * 10))
    cursor.execute(
        "INSERT INTO Projections (PortfolioID, FutureValue, ProjectionDate) VALUES (?, ?, ?)",
        (portfolio_id, future_value, projection_date)
    )
db.commit()

# Closing the connection
cursor.close()
db.close()

create_views()
create_sp()