# ThirdProject for PSR using ROS


## Setup

To setup simply have a catking workspace created and have turtlebot installed

It's also a must exporting the turtlebot model 
using `export TURTLEBOT3_MODEL=waffle_pi`

You must also have the turtlebot's simulation repositories cloned. As well as the following two worlds

```
cd ~/catkin_ws/src
git clone https://github.com/aws-robotics/aws-robomaker-small-house-world
git clone https://github.com/aws-robotics/aws-robomaker-hospital-world
```

## Running

To run the simulation simply add the runit.sh file to your workspace (~/catkin_ws i.e) and run it 