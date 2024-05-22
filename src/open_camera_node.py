#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    # Convert the ROS Image message to OpenCV2 format
    bridge = CvBridge()
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    # Display the image
    cv2.imshow('Webcam', cv2_img)
    cv2.waitKey(1)

def main():
    rospy.init_node('open_camera_node')
    
    # Subscribe to the USB camera image topic
    rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    
    # Keep the node running
    rospy.spin()

    # Close any OpenCV windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
