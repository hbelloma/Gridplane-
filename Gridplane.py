GlowScript 2.9 VPython
 
 
 #run online with https://create.withcode.uk/
#or use https://repl.it/languages/tkinter
# this program makes a XY Gridplane simulation

#from visual import*
#from math import*

scene.background=vector(0,0,0.1)
us=vector(0,0,0)
r=2#50   #distancia al planeta

                
#   plano espacio temporal
for i in range(r+50):
     curve(pos=[vector(2*(i)-(r+50),0,-(r+50)),vector(2*(i)-(r+50),0,(r+50))], color=color.cyan)       
     curve(pos=[vector(-(r+50),0,2*(i)-(r+50)),vector((r+50),0,2*(i)-(r+50))], color=color.cyan)
     
