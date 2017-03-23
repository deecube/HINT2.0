import RPi.GPIO as GPIO
import os
import time
import datetime
import glob
import MySQLdb
from time import strftime
import serial

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN)
# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="username",passwd="password", db="temp_database")
cur = db.cursor()
 
def tempRead():
    t = open(temp_sensor, 'r')
    lines = t.readlines()
    t.close()
 
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0
    return round(temp_c,1)
 
while True:
    x = ser.readline()
    sensorValue = x
    temp = sensorValue
    print temp
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    #print datetimeWrite
    #sql = ("""INSERT INTO tempLog (datetime,temperature) VALUES (%s,%s)""",(datetimeWrite,temp))
    try:
        print "Writing to database..."
        # Execute the SQL command
        cur.execute(*sql)
        # Commit your changes in the database
        db.commit()
        print "Write Complete"
 
    except:
        # Rollback in case there is any error
        db.rollback()
        print "Failed writing to database"
 
    