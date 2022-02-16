import sqlite3
import subprocess as sp
import sys




def create_table():
	conn = sqlite3.connect('Movies.db')

	cursor = conn.cursor()

def add_movies( name, actor, actress, director , year_of_release ):
	conn = sqlite3.connect('Movies.db')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO Movies( name, actor, actress, director , year_of_release )
	    	        VALUES ( ?,?,?,?,? )
	'''

	cursor.execute(query,( name, actor, actress, director , year_of_release ))

	conn.commit()
	conn.close()



def get_movies():
	conn = sqlite3.connect('Movies.db')

	cursor = conn.cursor()

	query = '''
	    SELECT *
	    FROM Movies
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def get_data_by_actor(actor):
	conn = sqlite3.connect('Movies.db')

	cursor = conn.cursor()


	query = '''
	    SELECT  name, actor  FROM Movies
	    WHERE actor = '{}'
	''' .format(actor)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

create_table()



def add_data( name, actor, actress, director , year_of_release):
	add_movies( name, actor, actress, director , year_of_release)

def get_data():
	return get_movies()

def show_movies():
	Movies = get_movies()
	for movie in Movies:
		print(movie)

def show_data_by_actor(actor):
	Movies = get_data_by_actor(actor)
	if not Movies:
		print("No data found at actor",actor)
	else:
		print (Movies)

def select():
	sp.call('clear',shell=True)
	sel = input("1. Add Movie\n2.Show Movies\n3.Search Movie by actor name\n4.Exit\n\n")

	
	if sel=='1':
		sp.call('clear',shell=True)
		name = (input('Name: '))
		actor = input('Actor: ')
		actress = input('Actress: ')
		director= input('Director :')
		year_of_release=int(input("Year of Release: "))
		add_movies( name, actor, actress, director , year_of_release)
	elif sel=='2':
		sp.call('clear',shell=True)
		show_movies()
		input("\n\npress enter to back:")
	elif sel=='3':
		sp.call('clear',shell=True)
		actor = input('Enter Actor: ')
		show_data_by_actor(actor)
		input("\n\nPress Enter To back:")
	else:
		return 0
	return 1


while(select()):
	pass