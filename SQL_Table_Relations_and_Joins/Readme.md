Project: Answering Business Questions using SQL

Chinook database was used for this project. The Chinook database contains information about the artists, songs, and albums from the music shop, as well as information on the shop's employees, customers, and the customers purchases. This information is contained in eleven tables. The Chinook database is provided as a SQLite database file called chinook.db.

The sqlite3.connect() function was used to create a connection object, and passed that to the pandas.read_sql_query() function. 

To save some time, some helper functions were included. Context manager were also included to handle the connection to the SQLite database.

In this project, SQL was used to carry out various statistical analysis to find relevant patterns. The questions include 1. Finding out which music genres sell the best in a particular country. 2. Analyze the purchases of customers belonging to each employee to see if any sales support agent is performing either better or worse than the others. 3. Analyze the sales data for customers from each different country. 4. Create a series of visualizations which communicate our findings, and then make recommendations on which countries may have potential for growth 5. Finding out what percentage of purchases are individual tracks vs whole albums.
