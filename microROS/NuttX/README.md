# Installation under NuttX

It is possible to generate a Docker image specific to generate the microROS applications for microROS on NuttX boards. In this case it is possible to skip the next section.

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



