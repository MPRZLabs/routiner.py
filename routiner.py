#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  routiner.py
#  
#  Copyright 2014 Michcioperz <michcioperz@autistici.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3, logging

def init():
    global rlog, conn, c
    rlog = logging.getLogger("routiner")
    rlog.setLevel(logging.DEBUG)
    rlogch = logging.StreamHandler()
    rlogch.setLevel(logging.DEBUG)
    rlogfm =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rlogch.setFormatter(rlogfm)
    rlog.addHandler(rlogch)
    rlogfh = logging.FileHandler('log.log')
    rlogfh.setFormatter(rlogfm)
    rlog.addHandler(rlogfh)
    rlog.info("Initializing SQLite database connection")
    conn = sqlite3.connect('db.db')
    c = conn.cursor();
	
def install():
    global rlog, c
    rlog.info("Performing initial queries")
    c.execute("CREATE TABLE IF NOT EXISTS timeconditions (starthour integer, startminute integer, endhour integer, endminute integer, target text)")

	
def deinit():
    global rlog, conn
    rlog.info("Closing SQLite database connection")
    conn.commit()
    conn.close()

def main():
    init()
    install()
    deinit()
    return 0

if __name__ == '__main__':
    main()
