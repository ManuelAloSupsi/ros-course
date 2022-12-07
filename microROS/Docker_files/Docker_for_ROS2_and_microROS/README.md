# Docker file for ROS2 and microROS with freertos on ESP32

## Generation

This Docker file generates an images suitable to work with both ROS2 and microROS.

There are 2 specific folders:

  * /user/microros_ws
  * /user/ros2_ws

the first folder is used for all the tasks related to microROS, the second one is reserved for applications related to ROS2.

The docker images already contains the files required for microros.

Build the docker image with

```
$ docker build -t microros .
```


## Generating the files for freertos for ESP32 (Olimex ESP32 board with WIFI)

The docker image shows a terminal wit the prompt

```
root@debian:/user/microros_ws# 
```
The files for the ESP32 (Olimex) target can be installed with:

**All the following command must be launched from the shell.**


```
ros2 run micro_ros_setup create_firmware_ws.sh freertos esp32
```

*This operation requires about 5 minutes*

**It is possible now to freeze the container! The following operations are now for specific ROS2 and microROS applications.**

## Generating a test application

The next steps generate a publisher application on the microROS node

```
ros2 run micro_ros_setup configure_firmware.sh int32_publisher -t udp -i 10.17.11.31 -p 8888
```

*(Modify 10.17.11.31 with the address of your PC!)*

*Now the ESP32 must be configured to work with the provided WLAN*

```
ros2 run micro_ros_setup build_firmware.sh menuconfig

```

*In the menu choose "micro-ROS Transport Setting->WiFi Configuration" to set the WiFi SSID (ex. LMBS24) and the WiFi Password (ex. lmbslmbs), Save ("S"+enter) and quit (enter+"Q")*

Now it is possible to build and flash the microROS application

```
ros2 run micro_ros_setup build_firmware.sh
ros2 run micro_ros_setup flash_firmware.sh
```

## Generate the agent

**In order to see the messages sent from the microros node, we need to generate a micro_ros_agent**

```
ros2 run micro_ros_setup create_agent_ws.sh
ros2 run micro_ros_setup build_agent.sh
. install/local_setup.bash
```
We have now to start the agent and after thit we must reset the embedded board
```
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888
```

After resetting, the shell should be similar to this
```

[1670410139.957678] info     | UDPv4AgentLinux.cpp | init                     | running...             | port: 8888
[1670410139.957997] info     | Root.cpp           | set_verbose_level        | logger setup           | verbose_level: 4
[1670410147.218645] info     | Root.cpp           | create_client            | create                 | client_key: 0x6B56DC24, session_id: 0x81
[1670410147.218809] info     | SessionManager.hpp | establish_session        | session established    | client_key: 0x6B56DC24, address: 10.17.42.162:53450
[1670410147.254750] info     | ProxyClient.cpp    | create_participant       | participant created    | client_key: 0x6B56DC24, participant_id: 0x000(1)
[1670410147.269708] info     | ProxyClient.cpp    | create_topic             | topic created          | client_key: 0x6B56DC24, topic_id: 0x000(2), participant_id: 0x000(1)
[1670410147.275385] info     | ProxyClient.cpp    | create_publisher         | publisher created      | client_key: 0x6B56DC24, publisher_id: 0x000(3), participant_id: 0x000(1)
[1670410147.282320] info     | ProxyClient.cpp    | create_datawriter        | datawriter created     | client_key: 0x6B56DC24, datawriter_id: 0x000(5), publisher_id: 0x000(3)
```

In order to see the message we open a new terminal and we list the topics:
```
ros2 topic list
```
and we should obtain
```
/freertos_int32_publisher
/parameter_events
/rosout
```
Now it is possible to see the transmitted data with
```
ros2 topic echo /freertos_int32_publisher
```
and the result is like:
```
data: 246
---
data: 247
---
data: 248
---
data: 249
---
data: 250
---
data: 251
```






















