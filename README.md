# many_execute_py_script
Demo project demonstrating running a third-party python script inside the main project.

## Files:

1. `main.py` - main file demo project (run this file)
2. `test.py` - a python script that will run in the `main.py` file. In this example, it writes demo data to a text file.
3. `demo.txt` - a text file in which the result of the `test.py` script is placed to demonstrate its work.
4. `requirements.txt` - a file containing the required libraries for correct operation. These modules should be installed before starting the project. It is recommended to use the venv virtual environment.

## Install

> Step 1. Clone project:

`git clone https://github.com/kubenet/many_execute_py_script.git`

> Step 2. Install library PyQT5:

`pip install -r requirements.txt`

> Step 3. Run demo app:

`python main.py`
