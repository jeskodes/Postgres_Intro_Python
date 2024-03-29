import psycopg2 # import psycopg2 library/adapter

# Create variable and connect to Chinook database. Use the connect() method. 
connection = psycopg2.connect(database = "chinook")

# Connection needs a Cursor object - which is like a list, array or set. 
# Anything query from database gets added to cursor object. 
# Will iterate over the cursor object using a for loop. 

# build a cursor object of the database. 
cursor = connection.cursor() # anything query gets stored in cursor variable. Will "read" or iterate over with for loop.

# Query1 - execute query - select all results from Artist table 
cursor.execute('SELECT * FROM "Artist"')  # single quotes to wrap query and double quotes for value querying. 

# Query 2 - select only name from artist
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only queen from artist. Need to use placeholder for name and put name in string in list. 
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select by ArtistId. 
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - selects albums by queen in list 
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51]) d

# Query 6 - select all tracks from track table where the composer is queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - what happens if not in database? 

# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# fetch the results (multiple) Looking to fetch multiple records 
results = cursor.fetchall() # Then store data in results variable. 

# fetch the results (single) Intentionally looking for one record. 
# results = cursor.fetchone().


# In simple terms, the cursor is the tool you use to interact with the database, execute queries
# and keep track of the results. 
# The results variable is where the actual data fetched from the database is stored
# after you've used the cursor to retrieve it.

# close connection to database once fetched results so connection isn't persistent. 
connection.close()

# use for loop to iterate over each individual record retrieved in cursor list and print result variable. 

for result in results: 
    print(result)