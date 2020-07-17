from kbhit import *
from dronekit import connect        
from dronekit import VehicleMode
from dronekit import LocationGlobal, LocationGlobalRelative
import time                         

vehicle = connect('127.0.0.1:14551', wait_ready=True)

print("connected")
print(vehicle)

# for using kbhit.py
atexit.register(set_normal_term)
set_curses_term()

#loop until pushing "Ctrl+c"
try:
    while True:
        if kbhit():     # wait for pushing some key
            key = getch()   # get 1 letter

            #select according contents of key
            if  key=='s':               # stabilize
                vehicle.mode = VehicleMode('STABILIZE')
            elif key=='p':              # PosHold
                vehicle.mode = VehicleMode('POSHOLD')
            elif key=='l':              # loiter
                vehicle.mode = VehicleMode('LOITER')
            elif key=='g':              # guided
                vehicle.mode = VehicleMode('GUIDED')
            elif key=='r':              # RTL
                vehicle.mode = VehicleMode('RTL')
            elif key=='l':              # land
                vehicle.mode = VehicleMode('LAND')
            
            # command for arm/disarm
            elif key=='a':              # arm
                vehicle.armed = True
            elif key=='d':              # disarm
                vehicle.armed = False
            
            # takeoff
            elif key == 't':
                vehicle.simple_takeoff(alt=10)
            
            # simple_goto
            elif key=='1':              # simple_goto
                point = LocationGlobalRelative( -35.3631210, 149.1632438 , 30 )
                vehicle.simple_goto(point)
            elif key=='2':              # simple_goto
                point = LocationGlobalRelative( -35.3647134, 149.1654539 , 50 )
                vehicle.simple_goto(point)
            elif key=='3':              # simple_goto
                point = LocationGlobalRelative( -35.3630685, 149.1670847 , 50 )
                vehicle.simple_goto(point)

        # Show current flight mode
        print("--------------------------" )
        print(" System status: %s" % vehicle.system_status.state)
        print(" Is Armable?: %s" % vehicle.is_armable)
        print(" Armed: %s" % vehicle.armed) 
        print(" Mode: %s" % vehicle.mode.name )
        print(" Global Location: %s" % vehicle.location.global_frame)
        
        time.sleep(1)

except( KeyboardInterrupt, SystemExit):    # break when push "Ctrl+c"
    print( "SIGINT" )

# close connection between flight controller
vehicle.close()

print("finish!!")