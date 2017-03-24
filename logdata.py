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
db = MySQLdb.connect(host="localhost", user="root",passwd="deb280794", db="temp_database")
cur = db.cursor()

#opening file to log data locally
file = open("/home/pi/Desktop/sensordata.txt","rw+")
start = time.time()
while True:  
    x = ser.readline()
    f=x.split()
    moisture = f[1]
    humidity = f[4]
    temp = f[7]
    print moisture
    print humidity
    print temp
    m = str(moisture)   
    h = str(humidity)
    t = str(temp)
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    dtr = str(datetimeWrite)
    file.write(dtr + "\t")
    file.write(m + "\t")
    file.write(h + "\t")
    file.write(t + "\n")
    
    if time.time() - start < 900:
        continue
            
    #print datetimeWrite
    for line in file:
        data = line.split()
        datetimeWrite = data[0]
        moisture = data[1]
        humidity = data[2]
        temp = data[3]
        sql = ("""INSERT INTO tempLog (datetime,temperature,humidity,moisture) VALUES (%s,%s,%s,%s)""",(datetimeWrite,temp,humidity,moisture))
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

    #time.sleep(1)
    file = open("/home/pi/Desktop/sensordata.txt","rw+")  
    start = time.time()
    
