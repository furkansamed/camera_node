#!/usr/bin/env python3
import rosy
import cv2

class Camera_node:
    def __init__(self):
        rospy.init_node('camera', anonymous_=False)
        self.vid = cv2.VideoCapture(0)


    def main_control(self):

        while(True):
            ret, frame = self.vid.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.vid.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    CN = Camera_node()
    r = rospy.Rate(60)
    while not rospy.is_shutdown():
        CN.main_control()
        r.sleep()
