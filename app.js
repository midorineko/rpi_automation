var express = require('express');
var PythonShell = require('python-shell');
var app = express();
var fs = require('fs');
var ejs = require('ejs');

app.use(express.static('public'));

app.get('/', function (req, res) {
	PythonShell.run('first.py', function (err) {
	  if (err) throw err;
	  console.log('finished');
	});
	res.sendFile(__dirname + '/index.html');
});

app.get('/water', function (req, res) {
	var lineReader = require('readline').createInterface({
	  input: require('fs').createReadStream('water.txt')
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

app.get('/water/:one', function (req, res) {
	if(req.params.one == "one"){
		time = 60
	}else if(!isNaN(parseInt(req.params.one))){
		time = parseInt(req.params.one)
	}else{
		time = false
	}
	if (time){		
		var options = {
		  args: [time]
		};
		PythonShell.run('water_one.py', options, function (err) {
		  if (err) throw err;
		  console.log('finished');
			res.statusCode = 302; 
			res.setHeader("Location", "/water");
			res.end();
		});
	}else{
		res.statusCode = 302; 
		res.setHeader("Location", "/water");
		res.end();
	}
});

app.get('/image', function (req, res) {
	res.sendFile(__dirname + '/image.html');
});

app.get('/image/new', function (req, res) {
	PythonShell.run('cam.py', options, function (err) {
	  if (err) throw err;
	  console.log('finished');
		res.statusCode = 302; 
		res.setHeader("Location", "/image");
		res.end();
	});
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});