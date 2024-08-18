# MIL Software Team 2024 Application
This application assignment is designed to equip you with a very basic understanding of the systems in place at MIL before admission into the lab. By emulating how ROS works without the constraints of your OS, applicants will have an understanding of what a publisher, subscriber, and topic are as well as how to construct a simple simulation with ```pygame```.

## Setup Requirements
Before you start working on this project, make sure you have the following:
- Python 3.7 or higher
- Git Installed

## Getting Started
1. Clone this repository
```
git clone https://github.com/uf-mil/sw_2024_application.git
cd sw_2024_application
```
2. Create your own branch and switch to that branch using the following naming convention:
```
git branch <first_name>_<last_name>
git switch <first_name>_<last_name>
```
3. (Optional but HIGHLY RECOMMENDED) Create a virtual environment and activate your virtual environment
4. Install the required packages into your project. You are free to install any other packages to aid you with your project.
```
pip install asyncio pygame numpy
```

## Requirements
We are looking for two files: ```classes.py``` and ```sim.py```. 

### classes.py
Three classes must be clearly defined and commented in this file.
- Topic: _A topic should be initialized with a string (the name of the topic). In addition it should hold an array of subscriber objects whose callback function is called every time data is published to the topic_
   - Attributes
     - name : string
     - subscribers : Subscriber[]
   - Methods
     - _async_ publish(data)
     - subscribe(callback)

- Subscriber: _A subscriber should be initialized by passing in a Topic and a callback function. A subscriber listens for new data published to a topic that triggers its call back function._
    - Attributes
      - callback_func _*_ Stores the asynchronous call back function attributed to this subscriber.
    - Methods
      - _async_ callback(data) _*_ Calls the callback_func and passes data as an argument into callback_func

- Publisher: _A publisher should be initialized with a topic. The purpose of a publisher is to push new data into a Topic to trigger all the callback functions from the subscribers stored in the Topic._
  - Attributes
    - topic: Topic
  - Methods
    - _async_ publish(data)

### sim.py
For your simulation, we will provide you with the pygame loop to test out your code. Your assignment will require you to fill in the ```main()``` function with the expected mechanisms:
- Topic "/robot/position"

  - Update topic by publishing the next movements of the robot

- Utilize Topic "/robot/camera" to guide robot movement

_You may create any necessary helper files, classes, and methods if necessary._

### Evaluation

We will provide you with ONE sample course to test your code, but upon submission your code will be tested against a number of hidden test cases to evaluate the robustness of your path following algorithm (in addition to the aforementioned conditions for each file).
