#! /usr/bin/env python


import sqlite3
import hashlib
import Queue
import socket
from threading import Thread
from time import gmtime, strftime

class Backend:

  def __init__(self,theircall,mycall,theirexch,myexch,txfreq,rxfreq,mode,
               dxcc,theirname,country,state,county,cqzone,ituzone,xcvr,
               antenna,power,myqth,operator,satellite,mysummit,theirsummit,
               iota,clubs,notes):
    self.qso_id = hashlib.md5().hexdigest()
    self.time = strftime("%Y-%m-%d %H%M",gmtime())
    self.band = self.getBand(txfreq)
    self.theircall = theircall
    self.mycall = mycall
    self.theirexch = theirexch
    self.txfreq = txfreq
    self.rxfreq = rxfreq
    self.mode = mode
    self.dxcc = dxcc
    self.theirname = theirname
    self.country = country
    self.state = state
    self.county = county
    self.cqzone = cqzone
    self.ituzone = ituzone
    self.xcvr = xcvr
    self.antenna = antenna
    self.power = power
    self.myqth = myqth
    self.operator = operator
    self.satellite = satellite
    self.mysummit = mysummit
    self.theirsummit = theirsummit
    self.iota = iota
    self.clubs = clubs
    self.notes = notes

    self.database = "log.db"

    self.initDB() 
 
    self.netThread = Thread(target=self.netListener())
    self.netThread.start()


  def netListener(self:

    TCP_IP = '127.0.0.1'
    TCP_PORT = 7373
    BUFFER_SIZE = 512

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(TCP_IP,TCP_PORT)
    s.listen()

    conn, addr = s.accept()
    while 1:
      #get the stuff from the network, strip off the command and do the thing
      procData(conn.recv(BUFFER_SIZE))
      #options are log QSO, edit QSO, delete QSO

    conn.close()

  def procData(self,data):
#    returns tuple of the [action,restofdata]

  def qsoString(self):
    logstring = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},
                 {15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26}\n".format(
                 self.qso_id,self.time,self.band,send.theircall,self.mycall,
                 self.theircall,self.mycall,self.theirexch,self.txfreq,self.rxfreq,
                 self.mode,self.dxcc,self.theirname,self.country,self.state,
                 self.county,self.cqzone,self.ituzone,self.xcvr,self.antenna,
                 self.power,self.myqth,self.operator,self.satellite,self.mysummit,
                 self.theirsummit,self.iota,self.clubs,self.notes)
     print logstring
     return logstring


  def initDB(self,database):
    
    create_table_qsos = """CREATE TABLE IF NOT EXISTS qsos (
        id TEXT PRIMARY KEY,
        txfreq TEXT NOT NULL,
        rxfreq TEXT NOT NULL,
        band TEXT NOT NULL,
        mode TEXT NOT NULL,
        time TEXT NOT NULL,
        mycall TEXT NOT NULL,
        myexchange TEXT NOT NULL,
        theircall TEXT NOT NULL,
        theirexchange TEXT NOT NULL,
        opcall TEXT NOT NULL,
        dxcc TEXT NOT NULL,
        theirname TEXT NOT NULL,
        country TEXT NOT NULL,
        state TEXT NOT NULL,
        county TEXT NOT NULL,
        cqzone TEXT NOT NULL,
        ituzone TEXT NOT NULL,
        xcvr TEXT NOT NULL,
        antenna TEXT NOT NULL,
        power TEXT NOT NULL,
        myqth TEXT NOT NULL,
        satellite TEXT NOT NULL,
        mysummit TEXT NOT NULL,
        theirsummit TEXT NOT NULL,
        iota TEXT NOT NULL,
        clubs TEXT NOT NULL,
        notes TEXT NOT NULL
        );"""

    self.conn = sqlite3.connect(database)
    self.cur = conn.cursor()
    self.cur.execute(create_table_qsos)

  def getBand(self,freq):
    #if freq is blablabla band = 
    mhz = freq
    sixtymeters = [5.3305,5.3465,5.3570,5.3715,5.4035]
    
    if mhz >= .1357 and mhz <= .1358:
        band = "2200"
    elif mhz >= .472 and mhz <= .479:
        band = "630"
    elif mhz >= 1.8 and mhz <= 2:
        band = "160"
    elif mhz >= 3.5 and mhz <= 4:
        band = "80"
    elif mhz in sixtymeters:
        band = "60"
    elif mhz >= 7 and mhz <= 7.3:
        band = "40"
    elif mhz >= 10.1 and mhz <= 10.15:
        band = "30"
    elif mhz >= 14 and mhz <= 14.35:
        band = "20"
    elif mhz >= 18.068 and mhz <= 18.168
        band = "17"
    elif mhz >= 21 and mhz <= 21.45:
        band = "15"
    elif mhz >= 24.89 and mhz <= 24.99:
        band = "12"
    elif mhz >= 28 and mhz <= 29.7:
        band = "10"
    elif mhz >= 50 and mhz <=54:
        band = "50"
    elif mhz >= 70 and mhz <= 70.5:
        band = "70"
    elif mhz >= 144 and mhz <= 148:
        band = "144"
    elif mhz >= 220 and mhz <= 225:
        band = "222"
    elif mhz >= 420 and mhz <=450:
        band = "432"
    elif mhz >= 902 and mhz <= 928:
        band = "902"
    elif mhz >= 1240 and mhz <= 1300:
        band = "1.2G" 
    elif mhz >= 2300 and mhz <= 2450:
        band = "2.3G"
    elif mhz >= 3300 and mhz <= 3500:
        band = "3.4G"
    elif mhz >= 5650 and mhz <= 5925:
        band = "5.7G"
    elif mhz >= 10000 and mhz <= 10500:
        band = "10G"
    elif mhz >= 24000 and mhz <= 24250:
        band = "24G"
    elif mhz >= 47000 and mhz <= 47200:
        band = "47G"
    elif mhz >= 71500 and mhz <= 81500:
        band = "75G"
    elif mhz >= 122250 and mhz <= 123000:
        band = "123G"
    elif mhz >= 134000 and mhz <= 141000:
        band = "134G"
    elif mhz >= 241000 and mhz <= 250000:
        band = "241G"
    else:
        band = "INVALID"


     
