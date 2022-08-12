import psycopg2

def save_to_db(article_link, title, description):
	sql_command = "INSERT INTO our_table(article_link, title, description) VALUES (%s, %s, %s)"
	insert_values = (article_link, title, description)

	conn = None

	try:
		# connect to the PostgreSQL database
		conn = psycopg2.connect("dbname and user infos")
		# create a new cursor
		cur = conn.cursor()
		# execute the INSERT statement
		cur.execute(sql_command, insert_values)
		# commit the changes to the database
		conn.commit()
		# close communication with the database
		cur.close()

	except (Exception, psycopg2.DatabaseError) as e:
		print("Error: ", e)

	finally:
		if conn is not None:
			conn.close()