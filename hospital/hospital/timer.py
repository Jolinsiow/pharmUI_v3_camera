import time
import threading as th  
import threading
from threading import Thread
from threading import Timer
import time
from django.db import connection
import psycopg2
from django.shortcuts import redirect

# Version 1

class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = 300 # 5 minutes (300 seconds) first

    def run(self):
        while self.count > 0 and not self.event.is_set():
            print(self.count)
            self.count -= 1
            self.event.wait(1)

        if self.count == 0:
            # Write robot_prompt into the DB to send to REST Server / Link to call robot
            tmr.stop()
            print("Call the robot")

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
                conn.commit()

            except Exception as error:
                print(error)
         
    def stop(self):
        self.event.set()
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








