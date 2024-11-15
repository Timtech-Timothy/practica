# Information: https://clover.coex.tech/en/simple_offboard.html#gettelemetry

import rospy
from clover import srv

rospy.init_node('get_telemetry')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

# Print drone's state
print(get_telemetry())
