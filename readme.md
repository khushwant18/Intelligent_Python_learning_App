# Intelligent Python Learning App
[![](https://www.python.org/static/community_logos/python-logo.png)]()
>Intelligent Python learning app that provides user the freedom to select the content source (open source book) and generates summarized notes of a book. Further facilitates user to evaluate his learning through MCQs. Performance can be tracked through graph generated after submission of answers.

### How to Use this App:
  1. Run main.py 
  2. Use following credentials for login:
```sh
    Username: admin
    Password: admin
```
  3. Click on a book to select resource, (for sake of simplicity all books links to same text resource)
  4. Click forward and back arrow to navigate in app
  .1. clicking back arrow takes back to login page
   .2. clicking forward arrow will load interactive test screen
    You can also:
    .1. Load questionaire from resource selection screen
    .2. for demo purpose only, limited (4) set of questions are loaded, whereas the full set of questionaire includes more than 100 question

##### Perform test:
1. Select answers and submit to evaluate your score 
2. close the popup evaluation screen to view the answers and explanation

### Software and Libraries required
Intelligent Python Learning App uses a number of open source projects to work properly:

* Kivy- for APP GUI
* KivyMD - Material Theme resources
* python 3.7 IDE - for better support of kivy libraries
* sumy - to implement summarization algorithms 
* Beautiful Soup - to implement the webscarpping
* numpy - to process the data
* csv - to read and write csv file
* matplotlib - to plot the graphs
* sklearn - to implement machine learning
* pandas - to process the data
* urllib.request - to fecth urls