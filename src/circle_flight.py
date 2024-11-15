# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger
import math 

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

radius = 5.0

circle_points = 36

navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)

rospy.sleep(5)


for i in range(circle_points):
    angle = 2 * math.pi * i / circle_points

    x_p = radius * math.cos(angle)
    y_p = radius * math.sin(angle)

    navigate(x=x_p, y=y_p, z=0, frame_id='body')
    rospy.sleep(1)


land()