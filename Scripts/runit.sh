#!/bin/bash

gnome-terminal -e "bash -c 'cd ~/catkin_ws; source devel/setup.bash; catkin_make install && catkin_make; roslaunch robutler_bringup bringup.launch; exec bash'" &
gnome-terminal -e "bash -c 'cd ~/catkin_ws; source devel/setup.bash; roslaunch robutler_bringup gazebo.launch; exec bash'"

