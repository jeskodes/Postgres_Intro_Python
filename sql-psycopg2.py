import psycopg2 # import psycopg2 library/adapter

# Create variable and connect to Chinook database. Use the connect() method. 
connection = psycopg2.connect(database = "chinook")

# Connection needs a Cursor object - which is like a list, array or set. 
# Anything query from database gets added to cursor object. 
# Will iterate over the cursor object using a for loop. 

# build a cursor object of the database. 
cursor = connection.cursor() # anything query gets stored in cursor variable. Will "read" or iterate over with for loop.

# fetch the results (multiple) Looking to fetch multiple records 
results = cursor.fetchall() # Then store data in results variable. 

# fetch the results (single) Intentionally looking for one record. 
# results = cursor.fetchone()


# In simple terms, the cursor is the tool you use to interact with the database, execute queries
# and keep track of the results. 
# The results variable is where the actual data fetched from the database is stored
# after you've used the cursor to retrieve it.