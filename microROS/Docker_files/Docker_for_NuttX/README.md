# Docker file for code generation in NuttX

## Generation

This Docker file generates an image which can be used to generate code for the NuttX RTOS.

Build the docker image with

```
$ docker build -t nuttx .
```

## Generation of nodes for the NuttX RTOS
It is possible to generate specific applications for the NuttX OS by modifying the program "micorros_main.c" in the /NUTTX/apps/microros/example_app folder.

To compile this code it is important to do the following tasks
```
cd /NUTTX/nuttx
make menuconfig
```

In the menu Application Configuration->micro-ROS library and app we have to choose

  * micro-ROS library
  * micro-ROS example app

It is also possible to choose the "micro-ROS publisher app" and the micro-ROS subscriber app.

Then close and save the new configuration and launch
```
make $(nproc)
```
If the compilation is ok you should receive at the end a file called "nuttx". This file must be flashed on the nucleo-F746ZG board
```
flash_f7 nuttx
```
Then simply open a NuttX shell on the board
```
tio /dev/ttyACM0
```
and at the prompt launch
```
microros
```















