import htmlPy
import json
import sqlite3
import os
from shutil import copyfile

oscwd = os.getcwd()
#Create new database
db = sqlite3.connect('CombinedMatchedData')
cursor = db.cursor()
cursor.execute('''CREATE TABLE matchdata(crosslineauto TEXT,exchangeauto TEXT,matchName TEXT,notes TEXT,scoutName TEXT,deployRamp TEXT,startingposauto TEXT,driveOnPlatform TEXT,teamName TEXT,switchclosetele TEXT,allianceStation TEXT,switchauto TEXT,driveOnRamp TEXT,climbWithOther TEXT,scaleauto TEXT,scaletele TEXT,climb TEXT,exchangetele TEXT,switchfartele TEXT)
''')
db.commit()


for filename in os.listdir("D:/"):
    if filename.endswith(".db"):
        db_b = sqlite3.connect('D:/' + filename)
        # Get the contents of a table
        b_cursor = db_b.cursor()
        b_cursor.execute('SELECT * FROM MatchScoutingData')
        output = b_cursor.fetchall()   # Returns the results as a list.

        for row in output:
            cursor.execute('INSERT INTO matchdata VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        db.commit()
        b_cursor.close()


#close files
cursor.close()
print 'Data Combinaton Complete'

#Put data in excel
        
    
    

        
