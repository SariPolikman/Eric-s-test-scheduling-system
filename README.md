# Eric's test scheduling system
## How to run the solution:
To run the solution make sure that:
* Python packages are installed for you: tkinter, xlsxwriter, filedialog, pandas
* In the controller / project_path file the path variable contains the strip of the computer folder where you saved the project.
* Now you can run the main file.
#### Successfully !
## Distinction:
The long tests create "bubbles" of dead times,\
if a short slice of time remains the long tasks will not be able to enter it,\
(and if only long tasks remain there are many bubbles), \
a relative balance must be maintained between the number of long and short tests in one day.
## My Solution:
At each stage we will keep two dictionaries, the dictionary of the ready and the dictionary of the waiting,\
In each selection we will choose the longest test from the ready ones, \
as soon as it is over that the last test does not have enough time to finish before the end of the day,\
we will systematically choose the shortest task from the waiting list.\
If the ready-made dictionary is empty, we will take the tasks from the waiting dictionary with the least waiting time left for them.\
In each iteration we will update the relevant tests to the appropriate dictionaries.
## HOME_PAGE
Home page, where there are two buttons,\
edit the data or immediately start with the daily scheduling with default values.
##
![home_page](https://user-images.githubusercontent.com/57223094/114956577-d6f2f980-9e67-11eb-91dd-cb0c48541287.PNG)

## CHANGE_DETAILES_PAGE
Data change page, where you can wake up each of the fields and save, \
you can also edit the experiment file where all the experiment values are stored (test times and standby times), \
from the moment the data is saved - the timing calculation will be according to the new values
##
![image](https://user-images.githubusercontent.com/57223094/114956775-3bae5400-9e68-11eb-9966-9ea2fe170354.png)

## Daily scheduling
Daily scheduling, submission of effective daily scheduling, on weekdays between the set times,\
at any stage you can access the home page and change the values for the next day
## 
![image](https://user-images.githubusercontent.com/57223094/115002006-e9dbed00-9eac-11eb-8610-c4a6cce3dc19.png)

## CHANGE experimental data
Select a file with the experiment data
##
![image](https://user-images.githubusercontent.com/57223094/114957008-c4c58b00-9e68-11eb-8642-38772d2cde32.png)

## experimental data
The file must be saved, closed, and tomorrow we will refer to the new data
##
![image](https://user-images.githubusercontent.com/57223094/114957112-fd656480-9e68-11eb-9d08-d6cbe7fabeb3.png)

