# Installation under NuttX

It is possible to generate a Docker image specific to generate the microROS applications on NuttX boards. In this case it is possible to skip the next section.

## Install NuttX on your PC Linux

Create a directory for the nuttx files
```
mkdir NUTTX
```
The build of NuttX requires a couple of additional packages
```
apt install kconfig-frontends
apt install gcc-arm-none-eabi binutils-arm-none-eabi
apt-get install openocd
apt-get install tio
apt-get install python3-pip
```
Install the files required for microROS
```  
pip install catkin_pkg lark-parser empy colcon-common-extensions
```

Get the NuttX files from GIT
```
cd NUTTX
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps apps
```
Now we can install the files for micoROS
```
git clone -b galactic https://github.com/robertobucher/micro_ros_nuttx_app apps/microros
```
For the nucleo-F746ZG target we must modify the colcon file in the micro_ros_lib directory
```
cd apps/microros/micro_ros_lib
cp colcon.meta_udp colcon.meta
cd ../../..
```
The colcon.meta filr must be edited to fit the address of your ROS2 PC
```
       "rmw_microxrcedds": {
            "cmake-args": [
                "-DRMW_UXRCE_TRANSPORT=udp",
                "-DRMW_UXRCE_DEFAULT_UDP_IP=10.17.11.31",
                "-DRMW_UXRCE_DEFAULT_UDP_PORT=8888"
            ]
        },
        "tracetools": {
```

We can configure our system
```
cd nuttx;
make -j12 distclean
./tools/configure.sh -l nucleo-144:f746-pysim
kconfig-tweak --enable CONFIG_MICROROSLIB
kconfig-tweak --enable CONFIG_MICROROS_PUBLISHER
kconfig-tweak --enable CONFIG_MICROROS_SUBSCRIBER
```
and now we can launch the full compilation
```
make -j$(nproc)
```
and now we can flash the software using
```
flash_f7 nuttx
```
To start the microros application we need to enter the shell 
```
tio /dev/ttyACM0
```
we obtain a nuttx shell
```
nsh>
```
We can look at the installe files using
```
nsh> ?
```
with the result
```
nsh> ?
help usage:  help [-v] [<cmd>]

  .         cat       df        help      mkdir     ps        sleep     umount    
  [         cd        dmesg     hexdump   mkfifo    pwd       source    unset     
  ?         cp        echo      ifconfig  mkrd      rm        test      uptime    
  addroute  cmp       exec      insmod    mount     rmdir     time      usleep    
  arp       dirname   exit      kill      mv        rmmod     true      xd        
  basename  dd        false     ls        nslookup  route     truncate  
  break     delroute  free      lsmod     printf    set       uname     

Builtin Apps:
  nsh         publisher   sh          telnetd     
  ping        renew       subscriber  
nsh>
```
After starting the microros agent we can launch
```
nsh> publisher
```
And in the ROS2 docker have to launch
```
ros2 run my_topic listener_nuttx

```

## Devices available on the nucleo-F746ZG board

These are the devices already defined in the card:

```nsh> ls /dev
/dev:
 adc0
 can0
 console
 gpio0
 gpio1
 gpio10
 gpio11
 gpio12
 gpio2
 gpio3
 gpio4
 gpio5
 gpio6
 gpio7
 gpio8
 gpio9
 null
 ptmx
 pwm0
 qe2
 qe3
 telnet
 ttyS0
nsh> 

```

The GPIO are devided between input and output devices.

  * 4 gpio inputs
  * 8 gpio outputs
  * 1 gpio int input

The 2 PWM (/dev/pwm0) have 2 channels with complementary signal.

Other devices:

  * 4 ADC
  * 2 encoders
  * 1 CAN




