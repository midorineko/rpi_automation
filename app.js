var express = require('express');
var PythonShell = require('python-shell');
var app = express();
var fs = require('fs');
var ejs = require('ejs');

var bodyParser = require('body-parser')
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

app.get('/grow', function (req, res) {
	res.sendFile(__dirname + '/grow.html');
});

app.get('/water', function (req, res) {
	totalLines=[]
	var readline = require('linebyline'),
	rl = readline('water.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     totalLines.push(line)
	})
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
	console.log('in image?')
	res.sendFile(__dirname + '/image.html');
});

app.get('/image/new', function (req, res) {
	newImage = function(){
		PythonShell.run('cam.py', function (err) {
		res.statusCode = 302;
		res.setHeader("Location", "/image");
		res.end();
		});
	}
	newImage()
});

app.listen(3000, function () {
  console.log('Started Home Automation on 3000!');
});

app.get('/lights/:switch', function (req, res) {
	if(req.params.switch == "grow_on"){
		var options = {
		  args: ['b_on']
		};
		PythonShell.run('TransmitRF.py', options, function (err) {
			res.statusCode = 302;
			res.setHeader("Location", "/grow");
			res.end();
		});
	}else if(req.params.switch == "grow_off"){
		var options = {
		  args: ['b_off']
		};
		PythonShell.run('TransmitRF.py', options, function (err) {
			res.statusCode = 302;
			res.setHeader("Location", "/grow");
			res.end();
		});
	}else if(req.params.switch == "lights_on"){
		var options = {
		  args: ['on']
		};
		PythonShell.run('livolo.py', options, function (err) {
			res.statusCode = 302;
			res.setHeader("Location", "/");
			res.end();
		});
	}else if(req.params.switch == "lights_off"){
		var options = {
		  args: ['off']
		};
		PythonShell.run('livolo.py', options, function (err) {
			res.statusCode = 302;
			res.setHeader("Location", "/");
			res.end();
		});
	}else if(req.params.switch == "off"){
		var options = {
		  args: ['off']
		};
		PythonShell.run('livolo.py', options, function (err) {
			res.statusCode = 302;
			res.setHeader("Location", "/scenes");
			res.end();
		});
	}else{
		var options = {
		  args: [req.params.switch.toLowerCase()]
		};
		inputArgs=req.params.switch.toLowerCase()
		PythonShell.run('lights_main.py', options, function (err) {
			  res.statusCode = 302;
			  var myarr = ['led_off', 'lights_off', 'lights_on', 'all_off', 'led_off', 'led_on'];
			  var route_main = (myarr.indexOf(inputArgs) > -1);
			  if(route_main){
				res.setHeader("Location", "/");
			  }else{
			  	res.setHeader("Location", "/lights/off");
			  }
			  res.end();
			console.log(err)

		});
	}
});

app.get('/scenes', function (req, res) {
	scenes=[]
	var readline = require('linebyline'),
	rl = readline('scene.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     scenes.push(line)
	})
	PythonShell.run('current_hue_status.py', function (err, results) {
	  hue_status = results[0].split(',');
	  hue_status.shift();
	  strip_bri = hue_status[0]/254.0 * 100
	  bloom_1_bri = hue_status[1]/254.0 * 100
	  bloom_2_bri = hue_status[2]/254.0 * 100
	  strip_2_bri = hue_status[3]/254.0 * 100
	  fs.readFile('scene.html', 'utf-8', function(err, content) {
	    var renderedHtml = ejs.render(content, {scenes: scenes, hue_status: hue_status, strip_bri: strip_bri, bloom_1_bri: bloom_1_bri, bloom_2_bri: bloom_2_bri, strip_2_bri: strip_2_bri});  //get redered HTML code
	    res.end(renderedHtml);
	  });
	});
});

app.get('/scenes/new/:name', function (req, res) {
	var options = {
	  args: [req.params.name.toLowerCase()]
	};
	PythonShell.run('scene_new.py', options, function (err) {
		  res.statusCode = 302;
		  res.setHeader("Location", "/scenes");
		  res.end();
	});
});

app.post('/brightness', function (req, res) {
    var options = {}
    if(req.body.brightness != '1-255'){
    	options = {
    	  args: [req.body.brightness]
    	};
    }else{
    	options = {
    	  args: [req.body.brightness1, req.body.brightness2, req.body.brightness3, req.body.brightness4]
    	};
    }
    PythonShell.run('brightness.py', options, function (err) {
    	  res.statusCode = 302;
		    if(req.body.brightness == '1-255'){
		  		res.setHeader("Location", "/scenes");
		    }else{
		    	res.setHeader("Location", "/");
		    }
    	  res.end();
    });
});

app.get('/brightness/:value', function (req, res) {
	var options = {
	  args: [req.params.value.toLowerCase()]
	};
    PythonShell.run('brightness.py', options, function (err) {
    	  res.statusCode = 302;
		    if(req.body.brightness == '1-255'){
		  		res.setHeader("Location", "/scenes");
		    }else{
		    	res.setHeader("Location", "/");
		    }
    	  res.end();
    });
});

app.post('/set_scene', function (req, res) {
    options = {
    	  args: [req.body.strip_color, req.body.bloom_1_color, req.body.bloom_2_color, req.body.strip_2_color]
    	};
    PythonShell.run('scene_color_set.py', options, function (err) {
    	  res.statusCode = 302;
    	  res.setHeader("Location", "/scenes");
    	  res.end();
    });
});

app.get('/party', function (req, res) {
    PythonShell.run('party.py', function (err) {
    	  res.statusCode = 302;
    	  res.setHeader("Location", "/");
    	  res.end();
    });
});
