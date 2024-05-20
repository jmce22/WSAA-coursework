# Project #
Files relating to the big project for the module 'Web Services and Applications' of the HDip in Data Analytics from ATU.
(Note: files deployed to Pythonanywhere as part of this project can be found on a separate repository https://github.com/jmce22/deploytopythonanywhere.)

---

### **Name: James McEneaney**
### **Course: Higher Diploma in Computing in Data Analytics, ATU Ireland**
### **Semester: Semester 1 2024**

---

## Overview ##

This folder contains my work for the big project for the 'Web Services and Applications' module of the Higher Diploma in Data Analytics from ATU. 

The goal of my project was to create a web application that would allow the user to perform "CRUD" operations on a database I created, containing data about members of a gym. The data I wished to include in this database were *ID*, *name*, *age*, *height*, *weight* and *sex*. I wanted users to be able to view the list of all gym members and their data, update their data, create new members and delete members.

I ran into difficulties trying to get my web app to function properly on my browser; that is, being able to perform CRUD operations on the MySQL database I created. I could update my database using curl commands and Postman but was unable to implement that functionality through the web app at my local address.

I then deployed my code to Pythonanywhere in the hope that by hosting the web app on a third-party site instead of my own machine, it might be easier to link up my web app to a database. I also concluded that this would allow me to avoid having to provide password details in my config file for my local MySQL to enable the lecturer to access the database I had created. However, I ran into difficulties getting the app to run on Pythonanywhere too. As part of my attempt to host the app on Pythonanywhere, I created a MySQL database (jmce24$wsaa) containing a 'gym' table, similar to the one I created earlier on my machine, using the MySQL console on Pythonanywhere to do this. 

Considering the inconvenience of needing to provide a config file for my local MySQL to allow the lecturer to fully test my project code (and agreeing with the lecturer's instruction, I did not do this), it may have been a better option for me to utilise an external database rather than create my own. I came to this realisation at a late stage, however, so I decided to continue and to see if I could get the web app to function properly with the database I had.

My Pythonanywhere link is https://jmce24.pythonanywhere.com/ and the contents of the database I created can be seen at https://jmce24.pythonanywhere.com/gym. My deploytopythonanywhere repository can be viewed on my Github at https://github.com/jmce22/deploytopythonanywhere. In trying to get the app to work on pythonanywhere, I changed the urls in the Ajax functions in my HTML code so that it included my pythonanywhere address instead of my local machine's address.

Included in this folder are files that contain my code for the project, a gitignore file and this README file.

The files containing my code are as follows: 
- *rest_server.py* - my Flask server. Included in this file are curl commands (commented out) which can be used in the Windows command prompt to update the database.
- *gymDAO.py* - my data access object (DAO), which is the interface between my server and the HTML code for the web app. This calls upon my config file to retrieve log-in details to gain access to the SQL database I created. It contains functions to carry out CRUD operations.
- *memberlist.html* - my HTML code for the web app. I made heavy use of the lecturer's code, along with W3-schools and the Bootstrap documentation to attempt to create the app. 
- *testgymDAO.py* - a file I used to test whether my functions for each CRUD operation did what I wanted them to do.

I used Visual Studio Code (VS Code - version 1.89.1), to write my scripts and to upload them to my repository on GitHub for assessment.


### How to execute my script on your machine ###

- Open VSCode. Go to the search bar at the top and type '>'. 

- Search for Git: Clone.

- Select Clone from GitHub and press Enter.

- When prompted for the Repository URL, select clone from GitHub, then press Enter.

- Sign in to Github, if prompted to.

- Enter the URL "https://github.com/WSAA-coursework" into the repository field.

- Select which directory on your machine you would like to clone my repository to.

- Select "Open" when asked if you want to open the cloned repository.

- In the console, carry out the following commands to install packages needed for the code:
pip install flask
pip install mysql-connector-python

- Run the code for the Flask server by typing 'python rest_server.py' and hitting enter. This should set up the server on your machine; however, since the database that I am using in this project was one that I created, possession of my config file is needed to access it. 

- My HTML file can be opened on your browser by right-clicking on it in the file explorer on VS Code and selecting 'Copy Path'. This can then be pasted into the browser.