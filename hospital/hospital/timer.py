import time
import threading as th  
import threading
from threading import Thread
from threading import Timer
import time
from django.db import connection
import psycopg2
from django.shortcuts import redirect

import webbrowser

# Version 1

class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.initial_count = 900 # 5 minutes (300 seconds) first
        self.count = self.initial_count
        self.is_running = False # initialize to False

    def run(self):
        self.is_running = True # update to True when timer starts
        
        while self.count > 0 and not self.event.is_set():
            print(self.count)
            self.count -= 1
            self.event.wait(1)

        if self.count == 0:
            # Write robot_prompt into the DB to send to REST Server / Link to call robot
            self.stop()
            print("Timer is up. Send a REST call to the server to call the fleet server.")

            hostname = "database-2.cxjd4rzryhvg.ap-southeast-1.rds.amazonaws.com"
            database = "aws_db"
            username = "jolinsiow_db"
            pwd = "jolinsiow"
            port_id = 5430

            conn = None
            cur = None

            try:
                conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id
                )

                cur = conn.cursor() # Cursor allows me to perform any of the sql operations
                robot_prompt = "Activate"
                cur.execute("INSERT INTO robot_prompt (robot_prompt) VALUES ('{0}');".format(robot_prompt))
                webbrowser.open_new_tab('http://192.168.97.177:5000/startpharm')
                print("Successfully sent a REST call to the server.")
                conn.commit()

            except Exception as error:
                print(error)

    def start(self):
        self.is_running = True # update to True when timer starts
        self.count = self.initial_count # reset count to initial value
        threading.Thread.start(self)
        # print("Send a REST call to the server to call the robot.")

    def stop(self):
        self.event.set()
        self.is_running = False # update to False when timer stops
        print("Timer has stopped")

tmr = TimerClass()
#tmr.start()
#time.sleep(5)
#tmr.stop()






##### Redirect 1 (Fai - Django can't go with Flask as both are backend app l#####
from flask import Flask, render_template, request, redirect

flaskapp = Flask(__name__)


@flaskapp.route("/trylink", methods={"GET"})
def try_link():
    url = 'https://google.com'
    print("It works")
    return redirect(url)

if __name__ == "__main__":
    flaskapp.run(debug=True, port=5000, host='0.0.0.0') #127.0.0.1:5000/trylink








