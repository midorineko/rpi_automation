var express = require('express');
var PythonShell = require('python-shell');
var app = express();
var fs = require('fs');
var ejs = require('ejs');
const util = require('util');
var readline = require('linebyline');
var https = require( 'https' );


var request = require('request');
var cheerio = require('cheerio');

app.use(express.static('public'))
const WebSocket = require('ws');
const ws = new WebSocket('http://192.168.0.110:8080');
var bodyParser = require('body-parser')
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

app.use(express.static(__dirname + '/public'));

app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

app.get('/ledgrid', function (req, res) {
	led_sockets = []
	r2 = readline('led_sockets.txt');
	r2.on('line', function(line, lineCount, byteCount) {
	     led_sockets.push(line)
	})
	fs.readFile('ledgrid.html', 'utf-8', function(err, content) {
	  var renderedHtml = ejs.render(content, {led_sockets: led_sockets});  //get redered HTML code
	  res.end(renderedHtml);
	});
});

app.get('/scrape', function(req, res){
  url = 'https://www.reddit.com/r/DotA2';

  request(url, function(error, response, html){
    if(!error){
      var $ = cheerio.load(html);
      var name_1;
      var name_2;
      var tournament;
      var live;

      $('.md').filter(function(){
        var data = $(this);
        tournament = data.first().children('blockquote').eq(1).children('blockquote').children('blockquote').children('blockquote').children('blockquote').children('p').children('a').children('del').eq(0).html();
        live = data.first().children('blockquote').eq(1).children('blockquote').children('blockquote').children('blockquote').children('blockquote').children('p').children('a').children('del').eq(1).html();
        name_1 = data.first().children('blockquote').eq(1).children('blockquote').children('blockquote').children('blockquote').children('blockquote').children('p').children('a').children('del').eq(2).html();
        name_2 = data.first().children('blockquote').eq(1).children('blockquote').children('blockquote').children('blockquote').children('blockquote').children('p').children('a').children('del').eq(3).html();
      });
    }

    res.send('Check your console!')
    res.statusCode = 302;
    res.end();
  })
})

app.get('/test', function (req, res) {
	https.get('https://www.reddit.com/r/DotA2/', function(response) {
		  var final_games_string = '';
	      var body = '';
          response.on('data', function(d) {
              body += d;
          });
          response.on('end', function() {
              var str = body;
              var result = str.match(/<del>(.*?)<\/del>/g).map(function(val){
                 return val.replace(/<\/?del>/g,'');
              });
              var a = result;
              var new_arrs = [];
              var final_string = '';
              var count = 1;
              var time_arr = [];
              while(a.length) {
              	  b = a.splice(0,4)
              	  if(b[1] != 'LIVE'){
                  	new_arrs.push(b);
                  	var time_arr = b[1].split(' ');
             		var time_string = '';
                  	time_arr.forEach(function(element) {
                  	    if(element.indexOf('d') !== -1){
                  	    	time_string += parseInt(element) + ' ' + 'days ';
                  	    }else if(element.indexOf('h') !== -1){
                  	    	time_string += parseInt(element) + ' ' + 'hours ';
                  	    }else if(element.indexOf('m') !== -1){
                  	    	time_string += parseInt(element) + ' ' + 'minutes ';
                  	    }else if(element.indexOf('s') !== -1){
                  	    	time_string += parseInt(element) + ' ' + 'seconds ';
                  	    }
                  	});
                  	final_string += count +', ' + b[2] + ', verse ' + b[3] + '. In ' + time_string +'. ';
                  	count += 1;
              	  }
              }
              console.log(final_string);
          });
          res.statusCode = 302;
          res.end();
	} );
});



app.get('/scene_select/:name', function (req, res) {
	rl = readline('scene_main_new.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     if(line.split('=')[0].toLowerCase().replace(/\s/g, '') == req.params.name.toLowerCase().replace(/\s/g, '')){
			ws.send(line.split('=')[1]);
	     }
	});
	var json_obj = {};
	r2 = readline('color_name_to_hex.txt');
	r2.on('line', function(line, lineCount, byteCount) {
	     if(line.split('=')[0].toLowerCase() == req.params.name.toLowerCase()){
			json_obj['color1'] = line.split('=')[1];
			ws.send(JSON.stringify(json_obj));
	     }
	});
	res.statusCode = 302;
	res.end();
});

app.get('/brightness/:bright', function (req, res) {
	bright_string = "brightness=" + req.params.bright;
	console.log(bright_string);
	ws.send(bright_string);
	res.statusCode = 302;
	res.end();
});

app.get('/color_select/:set/:color', function (req, res) {
	var set = req.params.set.toLowerCase();
	var color = req.params.color;
	var json_obj = {};
	rl = readline('color_name_to_hex.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     if(line.split('=')[0].toLowerCase() == req.params.color.toLowerCase()){
			json_obj[set] = line.split('=')[1];
			console.log(JSON.stringify(json_obj));
			ws.send(JSON.stringify(json_obj));
	     }
	});
	res.statusCode = 302;
	res.end();
});

app.get('/grow', function (req, res) {
	res.sendFile(__dirname + '/grow.html');
});

app.get('/water', function (req, res) {
	totalLines=[]
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
		PythonShell.run('scene_main.py', options, function (err) {
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

app.get('/scenes_main', function (req, res) {
	scenes=[]
	led_sockets = []
	rl = readline('scene_main_new.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     scenes.push(line)
	})
	r2 = readline('led_sockets.txt');
	r2.on('line', function(line, lineCount, byteCount) {
	     led_sockets.push(line)
	})
	fs.readFile('scenes_main.html', 'utf-8', function(err, content) {
	  var renderedHtml = ejs.render(content, {scenes: scenes, led_sockets: led_sockets});  //get redered HTML code
	  res.end(renderedHtml);
	});
});

app.get('/scenes', function (req, res) {
	scenes=[]
	rl = readline('scene.txt');
	rl.on('line', function(line, lineCount, byteCount) {
	     scenes.push(line)
	})
	PythonShell.run('current_hue_status.py', function (err, results) {
		console.log(err);
	  if (results){
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
	  }
	});
});

var request = require('request');
app.get('/weather', function (req, res) {
	console.log('hit weather')
	res.send("I am going to parse the weather and leave it here like a boss :3");
	res.end();
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

app.post('/save_json_scene', function (req, res) {
	console.log(req.body);
	var options = {
	  args: [req.body['json_str'], req.body['name']]
	};
	PythonShell.run('save_json_scene.py', options, function (err) {
		console.log(options)
		  res.statusCode = 302;
		  res.setHeader("Location", "/ledgrid");
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

app.get('/nfl', function (req, res) {
	PythonShell.run('nfl.py', function (err, results) {
	});
	res.statusCode = 302;
	res.setHeader("Location", "/");
	res.end();
});

app.get('/nfl/score', function (req, res) {
	res.sendFile(__dirname + '/nfl.html');
});

app.get('/nfl/plays', function (req, res) {
	res.sendFile(__dirname + '/nfl_events.html');
});

app.get('/curtain/open', function (req, res) {
	PythonShell.run('blinds_open.py', function (err, results) {
	});
	res.statusCode = 302;
	res.setHeader("Location", "/");
	res.end();
});

app.get('/curtain/close', function (req, res) {
	PythonShell.run('blinds_close.py', function (err, results) {
	});
	res.statusCode = 302;
	res.setHeader("Location", "/");
	res.end();
});
