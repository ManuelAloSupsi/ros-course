<p align="center">
  <img src="Public/Image/logo-SUPSI.png" style="width: 300px;">
  <img src="Public/Image/ros-logo-white.png" style="width: 300px;">
</p>

# Description

Requirements:
* WLS
* Docker Desktop
* Dowload image

# Preparazioni corso ROS

## Docker

### Installazione wls

Open PowerShell with administrator privileges and run the follow command:
```bash
wls –intall
```
Restart your computer to finish the WSL installation on Windows.

Always usign PowerShell as administrator update the wls
```bash
wsl --update
```
and install the Debian distribution
```bash
wsl –install -d Debian
```
To check to the success of the installation type the following command to verify the version of the distro:
```bash
wsl -l -v
```
Confirm Debian with distro version is 2.

### Installazione Docker Desktop
Installa Docker Desktop dal sito ufficiale 
<a href="https://www.docker.com/products/docker-desktop/">
<img src="Public/Image/vertical-logo-monochromatic.webp" style="width: 50px;">
</a>


http://localhost:8080/vnc.html

cliccare sul bottone "Connect"

### Download of ros-course image

docker pull manuelalosupsi/ros-course

# Course

# Execute the image


```bash
docker run -it --rm -p 8080:8080 manuelalosupsi/ros-course
```

