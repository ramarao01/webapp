import sqlite3
with sqlite3.connect("sample3.db") as connection:
	c = connection.cursor()
	try:
	    c.execute("DROP TABLE Ram")	
	except:
	    pass
	finally:
	    c.execute("CREATE TABLE Ram(FirstName Text, SurName Text,email Text,MobileNo Int)")
	    c.execute('INSERT INTO Ram VALUES("Ramarao","KEDARASETTI","ramarao.kedarasetti@nexiilabs.com","9553491072")')
	    c.execute('INSERT INTO Ram VALUES("SAIDATTA","KEDARASETTI","saidatta003@gmail.com","9177420596")')
	    c.execute('INSERT INTO Ram VALUES("Satya","KEDARASETTI","satyakedarse@gmail.com","85000813568")')
	    c.execute('INSERT INTO Ram VALUES("Venkateswararao","KEDARASETTI","","7396342255")')
	    c.execute('INSERT INTO Ram VALUES("kameswari","KEDARASETTI","","7386652165")')
	    c.execute('INSERT INTO Ram VALUES("Manikanta","PATWARI","manikanth.patwari@nexiilabs.com","")')

