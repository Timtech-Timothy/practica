# Information: https://clover.coex.tech/camera

# Example on basic working with the camera and image processing:

# - cuts out a central square from the camera image;
# - publishes this cropped image to the topic `/cv/center`;
# - computes the average color of it;
# - prints its name to the console.

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from clover import long_callback
import numpy as np

rospy.init_node('cv')
bridge = CvBridge()



@long_callback
def image_callback(msg):
    img = bridge.imgmsg_to_cv2(msg, 'bgr8')

    # convert to HSV to work with color hue
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    down_mask = np.array([10, 10, 0])
    upper_mask = np.array([100, 100, 255])

    mask = cv2.inRange(img_hsv, down_mask, upper_mask)


    cv2.imshow("rect", mask)
    cv2.waitKey(1)

# process every frame:
image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback, queue_size=1)

# process 5 frames per second:
# image_sub = rospy.Subscriber('main_camera/image_raw_throttled', Image, image_callback, queue_size=1)

rospy.spin()
