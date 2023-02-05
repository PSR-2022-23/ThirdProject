#!/bin/bash

cd ~/catkin_ws

source delevel/setup.bash
catkin_make install && catkin_make

if [ "$1" = "1" ]; then
  roslaunch robutler_bringup bringup.launch
elif [ "$1" = "0" ]; then
  roslaunch robutler_bringup gazebo.launch
else
  echo "Invalid argument. Usage: ./runit.sh [0 or 1]. If ran with 0 launch robot with 1 launch apartment"
fi