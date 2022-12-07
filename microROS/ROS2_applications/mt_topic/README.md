This folder contains the python applications required to interact with microROS on ESP32 (Olimex) with freertos and on a NuttX board (here for example the nucleo-F746ZG board) on the same time, in multithread mode

mt_topic provides 3 applications
  * subscriber.py
  * subs_freertos.py
  * subs_nuttx.py

## Build the applications

In the Docker image do the following tasks
```
cd /user/ros2_ws
```
In this example I have the "mt_topic" folder in a directory mapped as "/mnt" in the docker container.
```
cd src
ros2 pkg create --build-type ament_python mt_topic
cp /mnt/mt_topic/setup.py mt_topic
cp /mnt/mt_topic/my_topic/*.py mt_topic
```
To build the files simply type
```
cd /user/ros2_ws
colcon build --packages-select my_topic
. install/setup.bash
```
We can now start the microros agent
```
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```

Reset the Olimex and launch the "publisher" application on the NuttX board.

In a second terminal do
```
cd /user/ros2_ws
. install/setup.bash
ros2 run mt_topic listen
```
to see the messages.