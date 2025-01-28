# importing the necessary libraries
import pandas as pd
from sqlalchemy import create_engine

#link to data on the ny_taxi's website
url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz'

# Loading data from source
try:
    data = pd.read_csv(url) #reading the data
except Exception as e:
    print(f"Error Loading data from source: {e}") # Error handling
else:
    print("Data Loaded successfully") 
    print(data.head(5)) # first five rows of the data

#Converting the data type text of pickup date and dropoff date to Timestamp
data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
data['lpep_dropoff_datetime'] = pd.to_datetime(data['lpep_dropoff_datetime'])

dataset_with_zones = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

try:
    # Load the dataset
    dataset_with_zones = pd.read_csv(dataset_with_zones)
    print("Dataset with zones Loaded Successfully")
    print(dataset_with_zones.head(5))  # Display first 5 rows
except FileNotFoundError:
    print(f"File not found: {file_path}")
except pd.errors.EmptyDataError:
    print("File is empty or improperly formatted")


try:
    engine = create_engine('postgresql://root:root@localhost:5435/ny_taxi') #create the connection
    engine.connect # connect to the database
except Exception as e:
    print(f"Error while connecting to database: {e}")
else:
    print("Connection Sucessful")

# sending the schema to the database 
try:
    data.head(n=0).to_sql(name='green_taxi_data',con=engine, if_exists='replace')
except Exception as e:
    print(f"Failed to load schema into the database:, {e}")
else:
    print("Schema loaded successfully into the database")

# loading the data
try:
    %time data.to_sql(name='green_taxi_data',con=engine, if_exists='replace')
except Exception as e:
    print(f"Failed to load data into the database:, {e}")
else:
    print("data loaded successfully into the database")

# Loading the schema of the dataset with zones
try:
    %time dataset_with_zones.head(n=0).to_sql(con=engine, name='zones', if_exists='replace')
except Exception as e:
    print(f"Failed to load schema into the database:, {e}")
else:
    print("schema loaded successfully into the database")

#Loading the dataset_with_zones to the database
try:
    %time dataset_with_zones.to_sql(con=engine, name='zones', if_exists='replace')
except Exception as e:
    print(f"Failed to load data into the database:, {e}")
else:
    print("data loaded successfully into the database")
