Once the PostgreSQL container is running, you can connect to it from your API or other services as needed using the host name database and the default port 5432. For example, in your Python code, you can use the psycopg2 package to connect to the database:


Run docker-compose up from the root directory of your project to start the PostgreSQL container and any other services you have defined in the docker-compose.yml file.


import psycopg2

conn = psycopg2.connect(
    host="database",
    database="mydatabase",
    user="postgres",
    password="password"
)

cur = conn.cursor()
cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()