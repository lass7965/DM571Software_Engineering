# DM571 Software Engineering - Part 2

## Description
This is a piece of software which will function as an online roster 
for a small community-driven cinema. It is created to make daily operations
easier for volunteers at the cinema. 
We've chosen to have all our data on an external database, instead of e.g.
implementing it in memory, so all volunteers can access the updated roster from home.
To view the database, you can simply login with the database credentials given below. 

## Requirements
A needed module to run the code is mysql-connector 
which can be downloaded through pip, or through your chosen IDE.
```bash
pip install mysql-connector-python
```
## Guide
When running the code, simply just run the "main.py" file. 

There is mainly 2 phases in the code:
### Part 1 - Login phase
Here you have to say if you want to login, or create a user.
Press "y" to login, and "n" to create a user. 
When you press y, you'll be redirected to the authentication checker,
where we'll be checking if your credentials fits with the users in the database. 
If you've given a wrong username / password combination, you'll be asked to try again.
Otherwise you'll be redirected to the next phase which we'll be calling "Active Session"
### Part 2 - Active session
When you've given correct credentials, you'll be able to enter commands. 
There is a lot of commands, but to make it easy for the user we've created a help function.
Simply type "help" and you'll get all the possible commands you can use, and how to use them. 


[Link for mySQL:](https://www.unoeuro.com/en/mysql/?login)

**Username:** *lkis_dk*

**Password:** *DM571Software*