#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointCloud

def points_callback(data):
    point_cloud = PointCloud()
    point_cloud.header = data.header
    pub.publish(point_cloud)
    rospy.loginfo("Published to /imageProjection")

def listener():
    global pub
    rospy.init_node('ouster_points_listener', anonymous=True)
    pub = rospy.Publisher('/imageProjection', PointCloud, queue_size=10)
    rospy.Subscriber("/ouster/points", PointCloud2, points_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

