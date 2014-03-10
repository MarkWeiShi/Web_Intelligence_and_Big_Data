#Created by Mark Shi for Web Intelligence and Big Data Coursera Assignment HW6 - Bayesian Classifier

import sqlite3 as lite
import sys

con = None

try:
        con = lite.connect('hw6.db')
        
        cur = con.cursor()        
        cur.execute("CREATE TABLE PA (A TEXT, P REAL)")
        cur.execute("INSERT INTO PA VALUES('y', 0.01)");
        cur.execute("INSERT INTO PA VALUES('n', 0.99)");

        cur.execute("CREATE TABLE PS (S TEXT, P REAL)")
        cur.execute("INSERT INTO PS VALUES('y', 0.5)");
        cur.execute("INSERT INTO PS VALUES('n', 0.5)");

        cur.execute("CREATE TABLE PT (T TEXT, A TEXT, P REAL)")
        cur.execute("INSERT INTO PT VALUES('y', 'y', 0.05)");
        cur.execute("INSERT INTO PT VALUES('y', 'n', 0.01)");
        cur.execute("INSERT INTO PT VALUES('n', 'y', 0.95)");
        cur.execute("INSERT INTO PT VALUES('n', 'n', 0.99)");

        cur.execute("CREATE TABLE PL (L TEXT, S TEXT, P REAL)")
        cur.execute("INSERT INTO PL VALUES('y', 'y', 0.10)");
        cur.execute("INSERT INTO PL VALUES('y', 'n', 0.01)");
        cur.execute("INSERT INTO PL VALUES('n', 'y', 0.90)");
        cur.execute("INSERT INTO PL VALUES('n', 'n', 0.99)");

        cur.execute("CREATE TABLE PB (B TEXT, S TEXT, P REAL)")
        cur.execute("INSERT INTO PB VALUES('y', 'y', 0.60)");
        cur.execute("INSERT INTO PB VALUES('y', 'n', 0.30)");
        cur.execute("INSERT INTO PB VALUES('n', 'y', 0.40)");
        cur.execute("INSERT INTO PB VALUES('n', 'n', 0.70)");
        
        cur.execute("CREATE TABLE PX (X TEXT, E TEXT, P REAL)")
        cur.execute("INSERT INTO PX VALUES('y', 'y', 0.98)");
        cur.execute("INSERT INTO PX VALUES('y', 'n', 0.05)");
        cur.execute("INSERT INTO PX VALUES('n', 'y', 0.02)");
        cur.execute("INSERT INTO PX VALUES('n', 'n', 0.95)");
        
        cur.execute("CREATE TABLE PE (E TEXT, L TEXT, T TEXT, P REAL)")
        cur.execute("INSERT INTO PE VALUES('y', 'y', 'y', 1)");
        cur.execute("INSERT INTO PE VALUES('y', 'y', 'n', 1)");
        cur.execute("INSERT INTO PE VALUES('y', 'n', 'y', 1)");
        cur.execute("INSERT INTO PE VALUES('y', 'n', 'n', 0)");
        cur.execute("INSERT INTO PE VALUES('n', 'y', 'y', 0)");
        cur.execute("INSERT INTO PE VALUES('n', 'y', 'n', 0)");
        cur.execute("INSERT INTO PE VALUES('n', 'n', 'y', 0)");
        cur.execute("INSERT INTO PE VALUES('n', 'n', 'n', 1)");
        
        cur.execute("CREATE TABLE PD (D TEXT, E TEXT, B TEXT, P REAL)")
        cur.execute("INSERT INTO PD VALUES('y', 'y', 'y', 0.90)");
        cur.execute("INSERT INTO PD VALUES('y', 'y', 'n', 0.70)");
        cur.execute("INSERT INTO PD VALUES('y', 'n', 'y', 0.80)");
        cur.execute("INSERT INTO PD VALUES('y', 'n', 'n', 0.10)");
        cur.execute("INSERT INTO PD VALUES('n', 'y', 'y', 0.10)");
        cur.execute("INSERT INTO PD VALUES('n', 'y', 'n', 0.30)");
        cur.execute("INSERT INTO PD VALUES('n', 'n', 'y', 0.20)");
        cur.execute("INSERT INTO PD VALUES('n', 'n', 'n', 0.90)");
        con.commit()
        
finally:
        if con:
                con.close()
