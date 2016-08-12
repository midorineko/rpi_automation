var express = require('express');
var PythonShell = require('python-shell');
var app = express();
var fs = require('fs');
var ejs = require('ejs');

app.get('/', function (req, res) {
	PythonShell.run('first.py', function (err) {
	  if (err) throw err;
	  console.log('finished');
	});
	res.sendFile(__dirname + '/index.html');
});

app.get('/water', function (req, res) {
	PythonShell.run('water.py', function (err) {
	  if (err) throw err;
	  console.log('finished');
	});
	var lineReader = require('readline').createInterface({
	  input: require('fs').createReadStream('myfile.txt')
	});

	var totalLines = []

	lineReader.on('line', function (line) {
	  totalLines.push(line);
	});

	fs.readFile('water.html', 'utf-8', function(err, content) {
	  if (err) {
	    res.end('error occurred');
	    return;
	  }
	  var renderedHtml = ejs.render(content, {totalLines: totalLines[totalLines.length-1]});  //get redered HTML code
	  res.end(renderedHtml);
	});
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});