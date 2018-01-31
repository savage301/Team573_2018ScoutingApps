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
##        conn = sqlite3.connect('573PitScouting.db')
##        c = conn.cursor()
##        c.execute('INSERT INTO PitScoutingData (teamName, scoreDoubleExchange, scale,scoreDoubleSwitch,scoreScale,exchange,notes,scoutName,deployRamp,driveOnPlatform,scoreSwitchandScale,switch,other,driveOnRamp,climbWithOther,scoreDoubleScale,climb,scoreExchange,scoreSwitch,crossLine,driveType,bumperHeight) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(loaded_json['teamName'], loaded_json['scoreDoubleExchange'],loaded_json['scale'],loaded_json['scoreDoubleSwitch'],loaded_json['scoreScale'],loaded_json['exchange'],loaded_json['notes'],loaded_json['scoutName'],loaded_json['deployRamp'],loaded_json['driveOnPlatform'],loaded_json['scoreSwitchandScale'],loaded_json['switch'],loaded_json['other'],loaded_json['driveOnRamp'],loaded_json['climbWithOther'],loaded_json['scoreDoubleScale'],loaded_json['climb'],loaded_json['scoreExchange'],loaded_json['scoreSwitch'],loaded_json['crossLine'],loaded_json['driveType'],loaded_json['bumperHeight']))
##        conn.commit()
##        conn.close()
##        print "Changes Stored"
        for x in loaded_json:
           print("%s: %s" % (x, loaded_json[x]))
        
    
    

        
