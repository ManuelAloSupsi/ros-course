FROM osrf/ros:galactic-desktop

RUN apt-get -y update
RUN apt-get -y dist-upgrade

RUN apt-get -y install \
     python3-pip \
     locate \
     less \
     net-tools \
     xfce4-terminal \
     emacs 

RUN apt-get -y clean
RUN apt-get -y autoremove

WORKDIR /
RUN mkdir user

WORKDIR /root
RUN mkdir -p .config/xfce4/terminal
COPY terminalrc .config/xfce4/terminal
RUN echo "source /opt/ros/galactic/setup.bash" >> .bashrc
RUN echo "cd /user/microros_ws;. install/setup.bash" >> .bashrc
RUN echo "alias inst='. install/setup.bash'" >> .bashrc

ENV PYTHONPATH /opt/ros/galactic/lib/python3.8/site-packages
ENV AMENT_PREFIX_PATH /opt/ros/galactic

WORKDIR /user
RUN mkdir -p ros2_ws/src
WORKDIR /user/ros2_ws
RUN colcon build --symlink-install

WORKDIR /user
RUN mkdir -p microros_ws/src

WORKDIR /user/microros_ws
RUN git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup

RUN  apt update && rosdep update
RUN rosdep install --from-paths src --ignore-src -y
RUN colcon build

WORKDIR /user/microros_ws
CMD ["xfce4-terminal"]
