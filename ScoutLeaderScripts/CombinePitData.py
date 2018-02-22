import htmlPy
import json
import sqlite3
import os
from shutil import copyfile

oscwd = os.getcwd()
#Create new database
db = sqlite3.connect('CombinedPitData')
cursor = db.cursor()
cursor.execute('''CREATE TABLE pitdata(teamName TEXT,scoreDoubleExchange TEXT,scale TEXT,scoreDoubleSwitch TEXT,scoreScale TEXT,exchange TEXT,notes TEXT,scoutName TEXT,deployRamp TEXT,driveOnPlatform TEXT,scoreSwitchandScale TEXT,switch TEXT,other TEXT,driveOnRamp TEXT,climbWithOther TEXT,scoreDoubleScale TEXT,climb TEXT,scoreExchange TEXT,scoreSwitch TEXT,crossLine TEXT,driveType TEXT,bumperHeight)
''')
db.commit()


for filename in os.listdir("D:/"):
    if filename.endswith(".db"):
        db_b = sqlite3.connect('D:/' + filename)
        # Get the contents of a table
        b_cursor = db_b.cursor()
        b_cursor.execute('SELECT * FROM PitScoutingData')
        output = b_cursor.fetchall()   # Returns the results as a list.

        for row in output:
            cursor.execute('INSERT INTO pitdata VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        db.commit()
        b_cursor.close()


#close files
cursor.close()
print 'Data Combinaton Complete'

#Put data in excel
        
    
    

        
