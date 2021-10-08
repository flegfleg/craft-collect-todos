

# Craft Collect Todos

![](.github/screenshot.png)

A simple script and Alfred.app worklflow for the [Craft](https://www.craft.do/) notes app that collects open todos from all documents. 

Works only with [External storage](https://www.craft.do/getting-started/b/A9629D59-881C-4785-822F-15BC6FAEEAEF/💻_Using_Local_Storage) (iCloud drive) libraries. 


## Requirements

* Python 3.9.5+
* [pync](https://pypi.org/project/pync/) : `$ pip install pync` or, if you do not need a notification, remove the call. 

## Stand-alone script

1. Download the script
2. Set the library path in **craft-collect-todos.py** 
* Run `$ python craft-collect-todos.py` to create a new collection of todos

## Alfred workflow

1. Download and open "Craft Collect Todos.alfredworkflow" 
2. In the Alfred window, set the library path to your local Craft Library  
3. Type "cctodos" to run the script


## Caveats

* Craft does not have an API, so i am parsing the json files. Changes to their format will probably break the parser.
* Not tested with huge Craft libraries 

