# Schedule

This is an App for creating employee schedules based on their availability.

The company employs around 50 people (mainly part-time) and has 4 to 6 workplaces with 2 work shifts each.
Every employee lists availability and preferred workplace for each month.
The App creates a ready schedule after receiving all availabilities from employees by pressing 1 or 2 buttons.

This app is an attempt to recreate the existing program used at Tri-City swimming pools.
The names of classes and variables are based on the original demand - water lifeguards assigned to their swimming pools.

The App works with a local mini-database in the folder "data", which should be downloaded in the same direction as the main script file.
Without downloading this folder the App will work, but the user will have to add manually all objects (employees and workplaces) which is time-consuming.

In the attached sample database are 3 months with schedules:
1) 01_2022 - ready schedule with some gaps (not enough volunteers)
2) 02_2022 - fully complete schedule with forcing employees to take shifts, which weren't in their availabilities
3) 03_2022 - an empty schedule that is ready to create - all availabilities were sent.

In an excel-file named "LOGIN_data" are written all logins and passwords to fully use the App.
In the case of creating a new employee's account default password is the employee's PESEL (PESEL needs to be unique).

Best Regards

Grzegorz Romanowski
