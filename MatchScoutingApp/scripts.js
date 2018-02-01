
function minus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-1;
}

function plus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-(-1);
}

// function WriteToFile() {
// 	console.log('TEST')

// var fs= CreateObject("Scripting.FileSystemObject"); 
// var fname=fs.CreateTextFile("c:\test.txt",true)
// fname.WriteLine("Hello World!")
// fname.Close


    // set fso = CreateObject("Scripting.FileSystemObject");  
    // set s = fso.CreateTextFile("C:\test.txt", True);
    // s.writeline(document.passForm.input1.value);
    // s.writeline(document.passForm.input2.value);
    // s.writeline(document.passForm.input3.value);
    // s.Close();
//  }
// function submittodb(){

// var tN = document.getElementsByName('teamName')[0].value;


// const sqlite3 = require('sqlite3').verbose();
 
// // open the database
// let db = new sqlite3.Database('573MatchScouting.db', sqlite3.OPEN_READWRITE);
 
//  db.run(`INSERT INTO PitScoutingData(teamName) VALUES(?)`, [tN])

// db.close();

// }