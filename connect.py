from dronekit import connect, VehicleMode, mavutil
import time

vehicle = connect('127.0.0.1:14550', wait_ready=True)

print("connected")
print(vehicle)

target_alt = 20

guided = VehicleMode('GUIDED')

vehicle.wait_for_armable(30)
print("Vehicle is armable")
vehicle.wait_for_mode(guided, timeout=10)
print("Mode changed")
vehicle.arm(wait=True, timeout=10)
print("Armed state {}".format(vehicle.armed))

print("takeoff")
vehicle.wait_simple_takeoff(target_alt, 0.5, timeout=10)

#vehicle.wait_for_mode(VehicleMode("LOITER"))

msg = vehicle.message_factory.command_long_encode(0, 1, mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 90, 0, 1, 1, 0, 0, 0)

vehicle.send_mavlink(msg)

# show parameter
try:
    while True:
        print("--------------------------" )
        print(" GPS: %s" % vehicle.gps_0 )
        print(" Battery: %s" % vehicle.battery )
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat )
        print(" Is Armable?: %s" % vehicle.is_armable )
        print(" System status: %s" % vehicle.system_status.state )
        print(" Mode: %s" % vehicle.mode.name )

        time.sleep(1)

except( KeyboardInterrupt, SystemExit):
    print("SIGINT")
    
# # parameter
# print("RTL ALT is {}".format(vehicle.parameters["RTL_ALT"]))
# vehicle.parameters["RTL_ALT"] = 2000
# print("RTL ALT is {}".format(vehicle.parameters["RTL_ALT"]))

# vehicle.armed = True
# vehicle.mode = VehicleMode("GUIDED")


# def location_callback(self, attr_vehicle, value):
#     print(attr_vehicle)
#     print(value)

# vehicle.add_attribute_listener("location.global_frame", location_callback)

# time.sleep(10)

#vehicle.remove_attribute_listener("location.global_frame", location_callback)

vehicle.close()