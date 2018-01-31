
function minus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-1;
}

function plus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-(-1);
}

function submittodb(){

var tN = document.getElementsByName('teamName')[0].value;


const sqlite3 = require('sqlite3').verbose();
 
// open the database
let db = new sqlite3.Database('573MatchScouting.db', sqlite3.OPEN_READWRITE);
 
 db.run(`INSERT INTO PitScoutingData(teamName) VALUES(?)`, [tN])

db.close();

}