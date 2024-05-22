#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class CameraNode:
    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node('open_camera_node', anonymous=True)
        
        # Subscribe to the raspicam image topic
        self.image_sub = rospy.Subscriber("/raspicam_node/image", Image, self.image_callback)
        
        # Window for displaying the image
        cv2.namedWindow("Raspberry Pi Camera", cv2.WINDOW_NORMAL)
        
    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to OpenCV2 format
            cv2_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
        else:
            # Display the image
            cv2.imshow('Raspberry Pi Camera', cv2_img)
            cv2.waitKey(1)
        
    def spin(self):
        rospy.spin()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_node = CameraNode()
    camera_node.spin()
