import htmlPy
import json
import sqlite3
import os
from shutil import copyfile

class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
        self.app.html = u"Hello, world"

    @htmlPy.Slot(str, result=str)
    def recordData(self, json_data):
        loaded_json = json.loads(json_data)
        conn = sqlite3.connect('573MatchScouting.db')
        c = conn.cursor()
        c.execute('INSERT INTO MatchScoutingData(crosslineauto,exchangeauto,matchName,notes,scoutName,deployRamp,startingposauto,driveOnPlatform,teamName,switchclosetele,allianceStation,switchauto,driveOnRamp,climbWithOther,scaleauto,scaletele,climb,exchangetele,switchfartele) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(loaded_json['crosslineauto'],loaded_json['exchangeauto'],loaded_json['matchName'],loaded_json['notes'],loaded_json['scoutName'],loaded_json['deployRamp'],loaded_json['startingposauto'],loaded_json['driveOnPlatform'],loaded_json['teamName'],loaded_json['switchclosetele'],loaded_json['allianceStation'],loaded_json['switchauto'],loaded_json['driveOnRamp'],loaded_json['climbWithOther'],loaded_json['scaleauto'],loaded_json['scaletele'],loaded_json['climb'],loaded_json['exchangetele'],loaded_json['switchfartele']))
        conn.commit()
        conn.close()
        print "Changes Stored"
##        for x in loaded_json:
##           print("%s: %s" % (x, loaded_json[x]))

    @htmlPy.Slot()
    def exportdb(self):
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
        
    
    

        
