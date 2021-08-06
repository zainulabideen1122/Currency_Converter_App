#Currency_Converter_App

![1](https://user-images.githubusercontent.com/59528492/128490522-2bf4635b-74a3-498a-b6d4-0d2923553e2f.JPG)



##ABOUT PROJECT:

Now a days conversion of currency is a major issue faced by foreigners. We build a software, which will convert currencies into desired currencies. But the most important thing is: Everyone wants an updated result, so in this software we use currency API's from free API providers to provide updated results to the users. In this project, we will make logics/functions and classes in python and Graphical User Interface in python library named as tkinter.

##IMPORTANT TERMS, Which we use in this projet:
###Request Module: Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT, PATCH or HEAD requests. A Http request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request. It has features of passing parameters and passing URL. It is human friendly HTPP (that allows users to communicate data on the World Wide Web) library. In our case, we use only GET method because we want to retrieve data from server only.**The first step is to install request by typing this command on terminal : pip install requests.**

###API: An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices.
**OR**
In simple wording, we can say that API is used to transfer or use data on different devices.
In this project, we are using free version of API, which is made by some-one. In this API, the data is stored in dictionaries in **JSON** format. We access data through accessing key, value pairs.

###Offline Mode: We are also using offline mode in this project, for example: If your machine is not connected to the internet, it will not affect the program, because we stored all the values in the program. But in offline mode, you will not get the updated values.

###Our python logic: In API, the values of 1 USD dollar to any currency is stored, If user want to convert any currency except USD to any Currency, then first, program will convert the given currency to dollars and then dollars to required currency, this is the main logic. Means our base currency in API is USD. Moreover, we use different functions to get values from user.

###Using Tkinter: Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit. Import the Tkinter module.

###Widgets in Tkinter:  **root = Tk(): , Use of Combo Box: , Use of message box: , root.geometry() , root.resizable() , Place(): , Pg , Fg , Pady etc** 
