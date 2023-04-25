#!/usr/bin/node
// script that gets the contents of a webpage
// and stores it in a file
const request = require('request');
const fs = require('fs');
const route = process.argv[2];
const fileName = process.argv[3];

request(route, (err, res, body) => {
  if (err) {
	console.log(err);
  } else {
  // Use fs.writeFile() method to write the file
  fs.writeFile(fileName, body, 'utf8', (err) => {
    if (err) {console.log(err);
    }
  });
  }
});
