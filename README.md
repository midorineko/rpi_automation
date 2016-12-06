# NFL PY
Alright, things are about to get bigger and better. I had an epiphany, use this api as a way for alexa to talk. Which basically meant I had to actually write an API. Starting with nfl.py. This is actually a server to populate files for me to pull on the alexa side. So I can get alexa to do things based on a server I am controlling. Right now it is going to give us the score and the last 5 plays, but we are going to ideally get 'Game Stream' going, which will stream the entire game and notify you when seahawks score. It is pretty easy to manipulate and can be used to view any team you like!
Much thanks to 
# **UPDATE 12/1/16**
Hello friends, just a quick updated of what has been going on. I moved to seattle thus my entire home automation was put to a stop. I am now ready to start automating 2.0, using this as a server and API for my Alexa Hub Skill.

If you want to checkout how I am interecting with this server checkout, https://github.com/midorineko/inouye_hub. This is how I am writing the amazon alexa skill, which is being hosted on a lambda. 

How does it all work?
I use a raspberry pi to physically controll my home. I interact with that pi through a tunnel. I talk to the tunnel through the amazon alexa skill. 'Alexa ask home lights seafoam' 'Alexa ask home welcome jordan' are both sentences which could be used to interact with my home. 

# rpi_automation
Early start of some rpi home automation

This is a fairly simple tool to use with a raspberry pi to control my bedroom.

I use a raspberry pi and 433mhz transmitter and receiver to encode RF signals for outlet control and main lights.

The receiver and transmitter are interacted with through python scripts.

I use a simple python library to interact with my philips hue LED lights.

A few cron jobs are used for light and water automation in my indoor garden, since these are the most important.

The water cron job checks a file to see when the last water was, if it has been three days it will water.

A python script which can take a photo of my garden at anytime so I can monitor it on the go.

# How to use the python scripts

This home automation is based on python scrips running on a Raspberry Py. Each of the python scripts could be useful in its own, so I will take the following section to explain them individually. 

##TransmitFR.py
Used to send RF signal to 433mhz outlets, I used Etekcity outlets. The following instructable will teach you how to use it. 
http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/

##Brightness.py
Sets brightness of philips hue light depending on input from node server. 

##cam.py
Takes a photo using a USB webcam, used to monitor my garden.

##lights_main.py
Brains behind main bedroom lighting. Dynamically updates to add new scenes.

##livolo.py
Connects Raspberry Pi to Livolo Light Switches. Instructions are held within the file.

##scene_new.py
Saves new scenes, by updating a text file and the lights_main.py file, via node request.

##server_check.py
Keeps my server and the tunnel running.

##water_cron.py
Works with a cron job on my raspberry pi to make sure my plants are watered every 3 days.

##water_one.py
Will water the garden based on node input.

# Node Server

I created a node server so I can interact with the python scripts on the fly.

The main functionality is to display captured image, control lighting schemes, and have the ability to manually override parts of my garden.

Most notably being able to water at anytime by accessing a specific url, which is taking into account by the cron job, so there is never overwatering.

The node server is hosted through a tunneling service so I can access it anywhere and my tunnel is maintained by a script which checks if it is running every 5 minutes. 

# Future Improvements

Create and amazon echo skill which will interact with the node server.

Have the garden lighting cron job rely off of a file, similarly to the water_cron.py. This will allow me to update when lights should turn on an off on the fly via the webserver.

Imrpove the water_cron.py so the amount of days to wait inbetween watering can be changed on the fly via the server.

Save current LED scenes to a file and have the lights_main.py file be able to pull from this file. (dynamically save led scenes)

Possibly add a soil gauge, but I honestly mostly water on a schedule. 
