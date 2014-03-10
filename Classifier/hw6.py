#Created by Mark Shi for Web Intelligence and Big Data Coursera Assignment HW6 - Bayesian Classifier

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('hw6.db')
    cur = con.cursor()
    
# for Tuberculosis
    cur.execute("SELECT PT.T, SUM(PA.P*PB.P*PD.P*PE.P*PL.P*PS.P*PT.P*PX.P) FROM PA, PB, PD, PE, PL, PS, PT, PX WHERE PT.A=PA.A AND PL.S=PS.S AND PB.S = PS.S AND PE.T=PT.T AND PE.L=PL.L AND PX.E=PE.E AND PD.E=PE.E AND PB.B=PD.B AND PA.A = 'n' AND PS.S = 'y' AND PX.X = 'y' AND PD.D = 'y' GROUP BY PT.T");
    rows = cur.fetchall()
    for r in rows:
        if r[0] == 'y':
            y = r[1]
        if r[0] == 'n':
            n = r[1]
    print "P(T) = " + str(y / (y + n))
    print "P(!T) = " + str(1 - y / (y + n))

# for Lung-Cancer
    cur.execute("SELECT PL.L, SUM(PA.P*PB.P*PD.P*PE.P*PL.P*PS.P*PT.P*PX.P) FROM PA, PB, PD, PE, PL, PS, PT, PX WHERE PT.A=PA.A AND PL.S=PS.S AND PB.S = PS.S AND PE.T=PT.T AND PE.L=PL.L AND PX.E=PE.E AND PD.E=PE.E AND PB.B=PD.B AND PA.A = 'n' AND PS.S = 'y' AND PX.X = 'y' AND PD.D = 'y' GROUP BY PL.L");
    rows = cur.fetchall()
    for r in rows:
        if r[0] == 'y':
            y = r[1]
        if r[0] == 'n':
            n = r[1]
    print "P(L) = " + str(y / (y + n))
    print "P(!L) = " + str(1 - y / (y + n))
    
# for Bronchitis
    cur.execute("SELECT PB.B, SUM(PA.P*PB.P*PD.P*PE.P*PL.P*PS.P*PT.P*PX.P) FROM PA, PB, PD, PE, PL, PS, PT, PX WHERE PT.A=PA.A AND PL.S=PS.S AND PB.S = PS.S AND PE.T=PT.T AND PE.L=PL.L AND PX.E=PE.E AND PD.E=PE.E AND PB.B=PD.B AND PA.A = 'n' AND PS.S = 'y' AND PX.X = 'y' AND PD.D = 'y' GROUP BY PB.B");
    rows = cur.fetchall()
    for r in rows:
        if r[0] == 'y':
            y = r[1]
        if r[0] == 'n':
            n = r[1]
    print "P(B) = " + str(y / (y + n))
    print "P(!B) = " + str(1 - y / (y + n))
    
finally:
    
    if con:
        con.close()
