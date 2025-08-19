# OpthaBot Development Repository

**Project for A-Level Computer Science 2021**

## Notice
This project is __VERY__ old now, over 4 years. It was initially just a project for A-Levels. Machine Learning has advanced significantly since this time. I would not think this project is a good framework for any machine learning anymore. 

## What is OpthaBot?
__OpthaBot__ is a tool that will help Optomometrists make diagnoses faster. It will utlises machine learning algorithms to make predictions based on fundus imagery. Alongside the ability to take in fundus scans and analyze them, OpthaBot also provides databasing options to manage patients, scans, diagnoses and users. 

## Installation Instructions

This project is still in development, and this repo contains the most up to date code. If you would like a single executable, wait for the official OpthaBot release repository. You can download version 1.4 of OpthaBot from [here](https://drive.google.com/file/d/1MEfIRiECeZk5osR9JVXSc57sRxra4Uaj/view)

First, you will need Python, any version above 3.7 should work.
>__*We recommend using the latest version of Python 3.8 as its the most stable for this program*__ 

You can download Python [here](https://www.python.org/downloads/) 

You may also need to install Git if you've not previously done so, that can be found [here](https://git-scm.com/download/win)

> *__Note: when installing Python or Git make sure that they are added to PATH during install, you should see an option for this when installing__*


Next, you will need to download the repository to your local machine. Create the folder you want to clone the repo to and open a command prompt *inside* that folder. Run the following command- 

    git clone https://github.com/spades1404/OpthaBotDevelopment opthabot
    
So you can take two routes now, an automatic install or the manual one. 

### Automatic Install

Go into the new opthabot folder and run the __install.bat__ script. Thats it. :kissing_closed_eyes:

Whenever you want to run the program after you can just use __run.bat__

Now that you've got the program running (hopefully) open the example folder so you have a full walkthrough of what to do.

### Manual Install
    
Now we need to get to the root directory:

    cd opthabot
    
Now you will need to setup the venv to run the program in. Run these commands to install your venv:

    python -m pip install --upgrade pip setuptools wheel virtualenv
    python -m virtualenv kivy_venv
    
Now open the venv:

    kivy_venv\Scripts\activate
    
Now we just need to install all the python dependencies that are needed:

    pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre
    pip install -r requirements.txt
    
Finally, run the program!

    python main.pyw
    

Whenever you want to run the program again all you need to do is run the command to open the venv and then run the file.

    kivy_venv\Scripts\activate
    python main.pyw
    
Enjoy!

Now that you've got the program running (hopefully) open the example folder so you have a full walkthrough of what to do.


