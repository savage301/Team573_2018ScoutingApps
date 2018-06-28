This repo contains the scripts used to run FRC Team 573 Scouting data. 

There are 3 folders:
  -MatchScoutingApp
  -PitScoutingApp
  -ScoutLeaderScripts

In order to run the scripts you will need Python 2.7 and to pip install the following packages
  -openpyxl
  -htmlPY
  -PIL
  
The MatchScoutingApp is a python based application. It uses htmlPy to create a interactive webpage that is used by scouters to input data.
The data input is stored in the sqlite database (also in that folder)

Main.py - Calls gui and connect it to the backend

BackEnd.py - Function that puts data from webpage to database

index.html - Webpage layout

styles.css - Webpage styling

scripts.js - Webpage embedded functions (Allows for plus and minus buttons to work)

ExportMatchData.py - Exports database to a usb stick. (So we can consolidate datafrom multiple scouters at an event.)

The PitScoutingApp is a python based application. It uses htmlPy to create a interactive webpage that is used by scouters to input data.
The data input is stored in the sqlite database (also in that folder)

Main.py - Calls gui and connect it to the backend

BackEnd.py - Function that puts data from webpage to database

index.html - Webpage layout

styles.css - Webpage styling

scripts.js - Webpage embedded functions (Allows for plus and minus buttons to work)

ExportPitData.py - Exports database to a usb stick. (So we can consolidate datafrom multiple scouters at an event.)

The ScoutLeaderScripts contains python scripts that take multiple sqlite databases (one from each scouter) and combines the information into one database. Then it reads that database and puts the data into a template excel spreadsheet.

CombineMatchData.py - Combines Match scouting data databases

CombinePitData.py - Combines Pit scouting data databases

CreateExcelSpreadsheet.py - Populates the data into the excel spreadsheet

ScoutingDataTemplate.xlsx - Template excel spreadsheet. Each time we created a new excel spreadsheet it'd be based upon the template.

