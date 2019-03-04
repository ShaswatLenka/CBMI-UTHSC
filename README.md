# CBMI@UTHSC GSoC 2019: Toy Implementation and Data Flow Diagrams for Project 1

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
### Level 1 DFD
![level1DFD](https://github.com/ShaswatLenka/CBMI-UTHSC/blob/master/images/level%201.png)

### Explanation of the toy implementation:
1. `MODELS`: This directory contains the Machine Learning models.
Training should be performed independently.`rfclassifier.py` implements a toy
Random Forest classifier on the iris dataset from scikit-learn. `serializer.py`
contains scripts to byte stream the model object and write it to disk
using `pickle`. 
2. `API`: `api.py` creates a sample api which loads the pickled 
version of the model to perform the prediction and returns the 
result. (in production, a REST model of the API will be developed
along with a local database to read/write as shown in level 1 DFD).
3. `apps`: contains the client(s) that serve the result to the end user.
it sends an api call (in production, the api calls can be time driven
or event driven) and dynamically update its UI. We can use "dash" or 
"plotly" for visualizations of `time_to_sepsis` here.

* To start the API server, run `python3 api.py` in API directory.
* To start the client server, run `python3 index.py` in root directory.

##### NOTE
The aim of this toy implementation is to provide the most simple
implementation of level 1 DFD which is architecturally strong enough
to add layers of complexities and maintain forward compatibility.
This does not focus on "batch processing" and UI components which
will be described in my proposal and implemented after access to database
and model.