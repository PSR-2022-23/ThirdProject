#!/usr/bin/env python3

import random
import rospkg
import rospy
from gazebo_msgs.srv import GetWorldProperties, SpawnModel
from geometry_msgs.msg import Pose, Point, Quaternion

# Define lists of basic models
basic_models = ['sphere_v']
# these models are too big to spawn on a table
only_ground_models = ['sphere_v']
#all placements
placements = {
    'placement_1': {'pose':Pose(position=Point(x=-5.69, y=4.37, z=0.6), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'large_bedroom', 'place': 'bed'},
    'placement_2': {'pose':Pose(position=Point(x=-7.33, y=5.29, z=0.58), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'large_bedroom', 'place': 'bedside_cabinet'}
}
#only gound level placements
floor_placements = {
    'placement_3': {'pose':Pose(position=Point(x=-7.33, y=5.29, z=0.58), orientation=Quaternion(x=0,y=0,z=0,w=1)),
              'room':'large_bedroom', 'place': 'bedside_cabinet'}
}



# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()
#dont forget to put models in proper folder :D
package_path = rospack.get_path('psr_apartment_description') + '/description/models/'

# get gazebo models for object spawning
rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)

rospy.wait_for_service('gazebo/get_world_properties')
getProperties = rospy.ServiceProxy('gazebo/get_world_properties', GetWorldProperties)

all_models = getProperties.call().model_names
spawned_models = [model for model in all_models if "_in_" in model and "_of_" in model]


if  len(list(placements.keys()))  == len(spawned_models):
    print("All placements occupied, delete an object to proceed...")
    exit(0)

# get inputs 
model_name = rospy.get_param('~object', "0")
model_placement = rospy.get_param('~place', "0")

temp = model_placement

while True:
    # flag
    occupied = False
    
    # unspec obj
    if model_name == "0" or model_name == 0:
        #unsepc place (no/no)
        if model_placement == "0" or model_placement == 0:

            # 20% chance of getting a only_ground_models instead of a basic model
            prob = random.randint(1, 100)
            if prob > 20:
                model_name = random.choice(basic_models)
                place=random.choice(list(placements.keys()))
                model_placement = (place, placements[place])
            else:
                model_name = random.choice(only_ground_models)
                place =random.choice(list(floor_placements.keys()))
                model_placement=(place,floor_placements[place])
        #no/yes
        else:
            #we have a placement

                    
            #but it doesnt exist
            if model_placement not in list(placements.keys()):
                print("Placement does not exist!!!")
                print(model_placement,model_name)
                exit(0)
            #but is occu+ied
            for model in spawned_models:
                if "_"+model_placement[0]+"_" in model:
                    print("Place in use, randomly going for another")
                    place =random.choice(list(placements.keys()))
                    model_placement=(place,placements[place])

            #not in floor means it can spawn only basic models obje
            if model_placement not in floor_placements:
                model_name = random.choice(basic_models)
            #if its a floor placement it can choose any model
            else:
                model_name= random.choice(basic_models+only_ground_models)

    else:
        #provided object but it doesn't exist 
        if model_name not in basic_models and model_name not in only_ground_models:
            print("Object does not exist!!")
            print(model_placement, model_name)
            exit(0)
        #it exists


        else:
            #object without placement (yes/no)
            if model_placement == 0 or model_placement == "0":
                #identify object type
                if model_name in basic_models:
                    place =random.choice(list(placements.keys()))
                    model_placement = (place, placements[place])
                #its a flooronly
                else:
                    place =random.choice(list(floor_placements.keys()))
                    model_placement = (place, floor_placements[place])

            else:
               # (yes/yes)
                #but is occupied or doesnt exist
                if model_placement not in list(placements.keys()):
                
                    print("Placement does not exist!!!")
                    print(model_placement[0],model_name)
                    exit(0)
                for model in spawned_models:
                    if "_"+model_placement[0]+"_" in model:
                        print("Place in use, randomly going for another")
                        place =random.choice(list(placements.keys()))
                        model_placement=(place,placements[place])
                #check object type 
                #if it is a complexmodel but given a nonfloor placement 
                if model_name in only_ground_models and model_placement not in list(floor_placements.keys()):
                    print("Placement and object not compatible, please choose a floor placement for this kind of object!!")
                    print(model_placement, model_name)
                    exit(0)
            #but is occupied
            for model in spawned_models:
                if "_"+model_placement[0]+"_" in model:
                    print("Place in use, randomly going for another")
                    place =random.choice(list(placements.keys()))
                    model_placement=(place,placements[place]) 
                

   
    for model in spawned_models:
        if "_"+model_placement[0]+"_" in model:
            occupied = True
            break
        
    if not occupied:
        break
    
    model_placement = temp
    


            
# name the object
name = model_name + '_in_' + model_placement[0] + '_of_' + model_placement[1]['room']

print(name)

# get the specific model
f = open( package_path + model_name + '/model.sdf' ,'r')
sdff = f.read()

# spawn the object
spawn_model_prox(name, sdff, model_name, model_placement[1]['pose'], "world")

               


