# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

print('Take off and hover 1 m above the ground')
navigate(x=0, y=0, z=1, frame_id='map', auto_arm=True)

# Wait for 5 seconds
rospy.sleep(5)

print('Fly forward 1 m')
navigate(x=5, y=5, z=5, frame_id='map')

# Wait for 5 seconds
rospy.sleep(20)

print('Fly left 1 m')
navigate(x=3, y=3, z=3, frame_id='map')

# Wait for 5 seconds
rospy.sleep(20)

print('Fly backward 1 m')
navigate(x=2, y=2, z=2, frame_id='map')

# Wait for 5 seconds
rospy.sleep(20)

print('RTH')
navigate(x=0, y=0, z=1, frame_id='map')
# Wait for 5 seconds
rospy.sleep(30)

print('Perform landing')
land()
