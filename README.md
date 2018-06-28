This repo contains the scripts used to run FRC Team 573 Scouting data. 

There are 3 folders:
  -MatchScoutingApp
  -PitScoutingApp
  -ScoutLeaderScripts
  
The MatchScoutingApp is a python based application. It uses htmlPy to create a interactive webpage that is used by scouters to input data.
The data input is stored in the sqlite database (also in that folder)

Main.py - Calls gui and connect it to the backend
BackEnd.py - Function that puts data from webpage to database
index.html - Webpage layout
styles.css - Webpage styling
scripts.js - Webpage embedded functions (Allows for plus and minus buttons to work)
ExportMatchData.py - Exports database to a usb stick. (So we can consolidate datafrom multiple scouters at an event.)
