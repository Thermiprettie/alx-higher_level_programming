#!/usr/bin/node
// script that reads and prints the content of a file

const fileName = process.argv[2];
// Include fs module
const fs = require('fs');
  
// Use fs.readFile() method to read the file
fs.readFile(fileName, 'utf8', function(err, data) {
	if (err) {
		// Display the file content
		console.log(err);
		return;
	}
	console.log(data);
});
