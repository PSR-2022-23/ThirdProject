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

This script will launch gazebo with apartment and bringup the rest 

##Spawn objects 


It is possible to spawn objects with 

```
rosrun psr_apartment_description spawn_object.py _place:=<place> _object:=<object>
```
where after = we can place a string from the following list or a 0 
0 means random generation
normal models: ['Ball','beer','bowl','hammer','Handle','plastic_cup','Portrait','SeasoningBox','sphere_v']
models that only spawn on floor: ['female','male','box']

all possible placements, ground level ones (only ones that can take male, female, box) tagged with *
placements : outside*,living_room_table,kitchen_counter,hall*,office*,gym*,kitchen_floor*,bed,bedside_cabinet

Before running its highly advised to run 

```
rosrun gmapping slam_gmapping scan:=/scan _base_frame:=base_footprint
```

Making a slam map and save it in the navigation package.

## Missions

- [x] Move to specified rooms
- [x] Robot search for objects in selected room/everywhere
- [x] Robot photograph selected room
- [x] Robot search for something in the appartement
- [x] Move anywhere in the house with coordinates or semantics
- [x] Spawn objects in at will

## References
- [YOLOv7-trained](https://github.com/WongKinYiu/yolov7)
- [Wiki-ROS](http://wiki.ros.org)
- [ROBOTIS] (https://github.com/ROBOTIS-GIT/turtlebot3)

