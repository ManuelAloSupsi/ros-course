This folder contains the python applications required to interact with microROS on ESP32 (Olimex) with freertos and on a NuttX board (here for example the nucleo-F746ZG board).

my_topic provides 3 applications
  * publisher.py
  * subs_freertos.py
  * subs_nuttx.py

## Build the applications

In the Docker image do the following tasks
```
cd /user/ros2_ws
```
In this example I have the "my_topic" folder in a directory mapped as "/mnt" in the docker container.
```
cd src
ros2 pkg create --build-type ament_python my_topic
cp /mnt/my_topic/setup.py my_topic
cp /mnt/my_topic/my_topic/*.py my_topic
```
To build the files simply type
```
cd /user/ros2_ws
colcon build --packages-select my_topic
. install/setup.bash
```
As example, we can start the microros agent and the application on the Olimex target, and see the sent message using the ROS2 application.
```
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```

Reset the Olimex

and in a second terminal do
```
cd /user/ros2_ws
. install/setup.bash
ros2 run my_topic listener_freertos
```
The output is like this
```
[INFO] [1670412208.835893057] [minimal_subscriber]: I heard: "86"
[INFO] [1670412209.745498190] [minimal_subscriber]: I heard: "87"
[INFO] [1670412210.754434147] [minimal_subscriber]: I heard: "88"
[INFO] [1670412211.754553756] [minimal_subscriber]: I heard: "89"
[INFO] [1670412212.755432374] [minimal_subscriber]: I heard: "90"
[INFO] [1670412213.757360964] [minimal_subscriber]: I heard: "91"
[INFO] [1670412214.764439946] [minimal_subscriber]: I heard: "92"
[INFO] [1670412215.774532576] [minimal_subscriber]: I heard: "93"
[INFO] [1670412216.775526414] [minimal_subscriber]: I heard: "94"
[INFO] [1670412217.774732949] [minimal_subscriber]: I heard: "95"
[INFO] [1670412218.776006696] [minimal_subscriber]: I heard: "96"
[INFO] [1670412219.784581501] [minimal_subscriber]: I heard: "97"
[INFO] [1670412220.785550412] [minimal_subscriber]: I heard: "98"
[INFO] [1670412221.794692899] [minimal_subscriber]: I heard: "99"
[INFO] [1670412222.793078356] [minimal_subscriber]: I heard: "100"
```












