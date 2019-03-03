# CBMI@UTHSC GSoC 2019 Sample Prototype for Project 1

This repository contains a sample prototype for Project 1 mentioned [here](https://docs.google.com/document/d/1HQCrOy694zVUnhx7xibheohTeonS1OzEKW22RbEUyvU/edit#).

According to the associated [research paper](https://www.sciencedirect.com/science/article/pii/S1386505618309444?via%3Dihub#bib0155), minute by minute, continuous physiological data was measured
using Cerner CareAware iBus platform which uses a SQL database according to [this](https://en.m.wikipedia.org/wiki/Cerner_CCL) link.
Also Apache Spark was used to preprocess and standardise the data due to its high 
frequency nature.<br>

Project 1: React-based web application for sepsis detection
Description: Sepsis is a life-threatening condition with high 
mortality rates. Early detection and treatment are critical to 
improving outcomes. Our goal is to develop an open source artificial 
intelligence based alert system capable of predicting sepsis earlier
using only a minimal set of streaming physiological data in real-time.
Using physiologic data of adult patients from the intensive care unit,
we already developed a Python-based machine learning method and would
like to extend this work and develop an open-source react based 
front-end application. In addition to the sepsis prediction pipeline,
the application would also have a visualization component for 
time_to_sepsis development.

### Level 0 DFD
![level0DFD](https://github.com/ShaswatLenka/CBMI-UTHSC/blob/master/images/level%200.png)