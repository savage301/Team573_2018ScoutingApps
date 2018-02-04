import htmlPy
import json
import sqlite3
import os
from shutil import copyfile

print "blah"
oscwd = os.getcwd()
db = '573MatchScouting'
dbnew = db
filestart = 0

for filename in os.listdir("D:/"):
    if filename.endswith(".db"):
        filenamenum = filename[-4:-3]
        if int(filenamenum) > filestart:
            filestart = int(filenamenum)

dbnew = db + str(filestart+1)
print dbnew
copyfile(db+'.db', 'D:/'+ dbnew + '.db')
#'573MatchScouting.db'
print 'Data Export Complete'
        
    
    

        
