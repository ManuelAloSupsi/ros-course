<p align="center">
  <img src="Public/Image/logo-SUPSI-black.png" style="width: 300px;">
  <img src="Public/Image/ros-logo-black.png" style="width: 300px;">
</p>

# Description

  ## Table of Contents  
  * [Homework before the course](#homework)  
  * [The course](#course)     
    * [Publiscer - Subscriber](#pub)  
    * [Service - Client](#service)  
    * [Actions](#action)  

  
<a name="homework"/>

# Homework before the course
Before the course it would be preferable to perform the following steps:
  * [Installl WLS](#wls)
  * [Install Docker Desktop](#dockerDesktop)
  * [Download of ros-course image](#image)
  * [Instantiate the image](#instImage)

  <a name="wls"/>
  
  ## Install WLS

  Open PowerShell with administrator privileges and run the follow command:
  ```bash
  wls --intall
  ```
  Restart your computer to finish the WSL installation on Windows.

  Always usign PowerShell as administrator update the wls
  ```bash
  wsl --update
  ```
  install the Debian distribution
  ```bash
  wsl --install -d Debian
  ```
  and move the distribution to distro 2
  ```bash
  wsl --set-vertion Debian 2
  ```
  To check to the success of the installation type the following command to verify the version of the distro:
  ```bash
  wsl -l -v
  ```
  Confirm that the distribution is Debian with distro version 2.
  
  <a name="dockerDesktop"/>
  
  ## Installazione Docker Desktop
  Install Docker Desktoo from the official Website :point_right:
  <a href="https://www.docker.com/products/docker-desktop/">
  <img src="Public/Image/vertical-logo-monochromatic.webp" style="width: 50px">
  </a>

  :warning: **Remember to run Docker Desktop as Amministrator every time** :warning:

  <a name="image"/>
  
  ## Download of ros-course image
  Launch the PowerShell as administrator and execute the following command to pull the image from the Docker Hub
  ```bash
  docker pull manuelalosupsi/ros-course
  ```
  <p align="center">
  <img src="Public/Image/pull.png" style="width: 80%;">
  </p>
  If the operation was successful you can find the <b>manuelalosupsi/ros-course</b> under <em>Image</em> tab of the Docker Desktop
  <p align="center">
  <img src="Public/Image/sull2.png" style="width: 80%;">
  </p>
  
  <a name="instImage"/>
  
  ## Instantiate the image
  To instantiate the image click on the play/run button :arrow_forward: (Actions column) under <em>Image</em> tab of the Docker Desktop
  <p align="center">
  <img src="Public/Image/sull3.png" style="width: 80%;">
  </p>
  The <b> Run a new container</b> windows appears. Expand the <b>Optional settings</b> menu and compile it as follows:
  
  * <b>Container name</b>: RosCourse
  * <b>Host port</b>: 8080 

  and the press run
  <p align="center">
  <img src="Public/Image/ImageInstant.png" style="width: 80%;">
  </p>
  
  Now the image has been instantiate in a container and it is on execution :horse_racing:
  <p align="center">
  <img src="Public/Image/contInst.png" style="width: 80%;">
  </p>
 
  If it doesn't work? :tired_face: You can try to pull again the image and instantiate it by using the following command:
  ```bash
  docker run -it --rm -p 8080:8080 manuelalosupsi/ros-course
  ```
  
  ### noVNC to visualize the container
  To visualize the container in execution can be used the noVNC tool, which we can access via the following link 
  http://localhost:8080/vnc.html
  <p align="center">
  <img src="Public/Image/vnc.png" style="width: 80%;">
  </p>
  
  <div align="center"><h3>:muscle::muscle:Now you are ready for the course:muscle::muscle:</h3></div>
  
<a name="course"/>

# The Course

  <a name="pub"/>
  
  ## Instantiate the image
  
  <a name="service"/>
  
  ## Instantiate the image
  
  <a name="action"/>
  
  ## Instantiate the image


    
    
  
