![banner](.images/banner-dark-theme.png#gh-dark-mode-only)
![banner](.images/banner-light-theme.png#gh-light-mode-only)

# micro-ROS app for Nuttx RTOS

These components and applications has been tested in Nuttx 11.0 and works only with ROS2 Huble!

## Dependencies

This component needs `colcon` and other Python 3 packages in order to build micro-ROS packages:

```bash
pip3 install catkin_pkg lark-parser empy colcon-common-extensions
```

## Usage

You can clone this repo directly in the `app` folder of your project.

## Example

<!--
Deps:
apt install git bison flex gettext texinfo libncurses5-dev libncursesw5-dev gperf automake libtool pkg-config build-essential gperf genromfs libgmp-dev libmpc-dev libmpfr-dev libisl-dev binutils-dev libelf-dev libexpat-dev gcc-multilib g++-multilib picocom u-boot-tools util-linux kconfig-frontends gcc-arm-none-eabi binutils-arm-none-eabi python3-pip cmake sudo

pip3 install catkin_pkg lark-parser empy colcon-common-extensions
-->
1. Install all the Nuttx dependencies using the [official documentation](https://nuttx.apache.org/docs/10.0.0/quickstart/install.html)
2. Move this files under the nuttx-apps folder
3. Go to 'nuttx' folder and configure the support for the nucleo-144 board:
```bash
cd nuttx
./tools/configure.sh -l nucleo-144:f746-pysim
```
4. Enable micro-ROS library and the applications:
```bash
kconfig-tweak --enable CONFIG_MICROROSLIB
kconfig-tweak --enable CONFIG_MICROROS_EXAMPLE
kconfig-tweak --enable CONFIG_MICROROS_PUBLISHER
kconfig-tweak --enable CONFIG_MICROROS_SUM_SERVICE
kconfig-tweak --enable CONFIG_MICROROS_SUBSCRIBER
```
5. Build Nuttx:
```bash
make -j$(nproc)
```
6. Flash the board

## License

This repository is open-sourced under the Apache-2.0 license. See the [LICENSE](LICENSE) file for details.

For a list of other open-source components included in ROS 2 system_modes,
see the file [3rd-party-licenses.txt](3rd-party-licenses.txt).

## Known Issues/Limitations

There are no known limitations.
