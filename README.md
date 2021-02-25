# OpthaBot Development Repository

### What is OpthaBot?
__OpthaBot__ is a tool that will help Optomometrists make diagnoses faster. It will utlises machine learning algorithms to make predictions based on fundus imagery. Alongside the ability to take in fundus scans and analyze them, OpthaBot also provides databasing options to manage patients, scans, diagnoses and users. 

### Installation Instructions

This project is still in development, and this repo contains the most up to date code. If you would like a single executable, wait for the official OpthaBot release repository.

However, if youre a baller heres how to install and run the source code.

First, you will need Python, any version above 3.7 should work. You can download python [here](https://www.python.org/downloads/). 

Next, you will need to download the repository to your local machine. Create the folder you want to clone the repo to and open a command prompt. Run the following command - 

    git clone https://github.com/spades1404/OpthaBotDevelopment opthabot
    
Then open up a command prompt in the root directory of the clone (inside the folder called opthabot), now you will need to setup the venv to run the program in. Run these commands to install your venv:

    python -m pip install --upgrade pip setuptools wheel virtualenv
    python -m virtualenv kivy_venv
    
Now open the venv:

    kivy_venv\Scripts\activate
    
Now we just need to install all the python dependencies that are needed:

    pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre
    pip install -r requirements.txt
    pip install kivymd
    
Finally, run the program!

    python main.py
    

Whenever you want to run the program again all you need to do is run the command to open the venv and then run the file.

    kivy_venv\Scripts\activate
    python main.py
    
Enjoy!

(I promise there will be an exe soon!)  :smiling_face_with_three_hearts:
