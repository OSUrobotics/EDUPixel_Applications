# Computer Vision Education Software

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Installing Environment](#installing-environment)

## Introduction

The purpose of this repository to make the public understand the limitation of computer vision.
In order to achieve this goal, I have designed four unique lessons with its video tutorial of using the code so that the user can fully understand each purpose of the program for each lesson.
At the same time, this research was under [Undergraduate Research, Scholarship and the Arts](https://undergraduate.oregonstate.edu/research/programs/ursa-engage) (URSA Engage) at Oregon State University with [Professor Cindy Grimm](https://mime.oregonstate.edu/people/grimm) and [Professor Bill Smart](https://mime.oregonstate.edu/people/smart). You can also find related Computer Vision materials [here](https://sites.google.com/view/edupixel/home) that contains this repository and other unique programs that make the user easily understand the limitation of Computer Vision.

TODO: Need the updated URL for this program and such: currently it leads to google.com when the user click "here" in the introduction

If you want to run this program by yourself, I would recommend to follow the instructions in the [Installing Environment](#installing-environment) section so that you would not get any conflicts with these code.

## Objectives

- Educate the basic concept of RGB values and Pixels

- Educate Computer Vision the public with layman terms

- Simple enough for K-12 students and non-technical users to understand the concept

- Change the public view point of Computer Vision

## Installing Environment

1. Install Python 3 that can be found [here](https://www.python.org).

2. Download this resposity as a .zip file and unzip the folder where you can easily access to it.

3. Open CMD or Command Terminal that the path is where the repository is located and type the following commend:
```pip3 install -r requirments.txt```

4. Go to the Lessons Folder and follow each lesson to learn and run the code upon it: only run ```.py``` files, not other files.

## Note
1. If you run into the issue written below after entering the command ```pip install -r requirments.txt```: 

ERROR: Could not find a version that satisfies the requirement pyqt5-plugins==5.15.2.2.0.1 (from versions: 5.14.2.2.1, 5.14.2.2.2, 5.15.0.2.1, 5.15.0.2.2, 5.15.1.2.1, 5.15.1.2.2, 5.15.2.2.1, 5.15.2.2.2, 5.15.3.2.1, 5.15.3.2.2, 5.15.4.2.1, 5.15.4.2.2)
ERROR: No matching distribution found for pyqt5-plugins==5.15.2.2.0.1

Run this command: ```pip3 install pyqt5-tools``` to install all the plugins related to pyqt5.

2. If you run into this issue: ModuleNotFoundError: No module named 'sklearn'
Run this command: ```pip3 install scikit-learn```
