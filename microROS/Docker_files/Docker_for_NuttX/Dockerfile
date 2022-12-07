FROM debian:bookworm

RUN apt-get -y update
RUN apt-get -y dist-upgrade

RUN apt-get -y install \
     locate \
     less \
     net-tools \
     xfce4-terminal \
     emacs  \
     make \
     cmake \
     python3-pip \
     kconfig-frontends \
     gcc-arm-none-eabi \
     binutils-arm-none-eabi \
     openocd \
     git \
     tio

RUN apt-get -y clean
RUN apt-get -y autoremove

WORKDIR /root
RUN mkdir -p .config/xfce4/terminal
COPY terminalrc .config/xfce4/terminal

RUN pip install catkin_pkg lark-parser empy colcon-common-extensions

WORKDIR /
RUN mkdir NUTTX
WORKDIR /NUTTX
RUN git clone https://github.com/apache/nuttx.git nuttx
RUN git clone https://github.com/apache/nuttx-apps apps
RUN git clone -b galactic https://github.com/robertobucher/micro_ros_nuttx_app apps/microros
COPY colcon.meta apps/microros/micro_ros_lib/

WORKDIR /NUTTX/nuttx
RUN ./tools/configure.sh -l nucleo-144:f746-pysim
RUN kconfig-tweak --enable CONFIG_MICROROSLIB
RUN kconfig-tweak --enable CONFIG_MICROROS_PUBLISHER
RUN kconfig-tweak --enable CONFIG_MICROROS_SUBSCRIBER
RUN make -j$(nproc)

COPY flash_f7 /usr/local/bin

WORKDIR /NUTTX/nuttx
CMD ["xfce4-terminal"]
