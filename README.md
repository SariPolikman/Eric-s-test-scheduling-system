# Eric's-test-scheduling-system
# Distinction:
The long tests create "bubbles" of dead times, if a short slice of time remains the long tasks will not be able to enter it, (and if only long tasks remain there are many bubbles), a relative balance must be maintained between the number of long and short tests in one day,
# My Solution:
##### At each stage we will keep two dictionaries, the dictionary of the ready and the dictionary of the waiting,
##### In each selection we will choose the longest test from the ready ones, 
##### as soon as it is over that the last test does not have enough time to finish before the end of the day,
##### we will systematically choose the shortest task from the waiting list.
##### If the ready-made dictionary is empty, we will take the tasks from the waiting dictionary with the least waiting time left for them.
##### In each iteration we will update the relevant tests to the appropriate dictionaries.
# HOME_PAGE
![home_page](https://user-images.githubusercontent.com/57223094/114956577-d6f2f980-9e67-11eb-91dd-cb0c48541287.PNG)
# CHANGE_DETAILES_PAGE
![image](https://user-images.githubusercontent.com/57223094/114956775-3bae5400-9e68-11eb-9966-9ea2fe170354.png)
# SCHEDULE DAYLEY
![image](https://user-images.githubusercontent.com/57223094/114956658-043fa780-9e68-11eb-953f-c4f8e32e9f0d.png)
# CHANGE experimental data
![image](https://user-images.githubusercontent.com/57223094/114957008-c4c58b00-9e68-11eb-8642-38772d2cde32.png)
# experimental data
![image](https://user-images.githubusercontent.com/57223094/114957112-fd656480-9e68-11eb-9d08-d6cbe7fabeb3.png)
