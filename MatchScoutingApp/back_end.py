import htmlPy
import json
import sqlite3

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
        
    
    

        
