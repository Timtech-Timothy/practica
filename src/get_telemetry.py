# Information: https://clover.coex.tech/en/simple_offboard.html#gettelemetry

import rospy
from clover import srv

rospy.init_node('get_telemetry')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
cnt = 0
def log(data, count):
    global cnt
    if count == 0:
        with open(f"log{cnt}.txt", 'w') as file:
            file.write(f"log_number: {count}" + "\n")
            file.write(str(data) + "\n")
            file.close()
    else:
        with open(f"log{cnt}.txt", 'a') as file:
            file.write("\n")
            file.write(f"log_number: {count}" + "\n")
            file.write(str(data) + "\n")
            file.close()

# Print drone's state
counter = 0
while True:
    tm = get_telemetry()
    print(tm)
    log(tm, counter)
    rospy.sleep(1)
    counter += 1
