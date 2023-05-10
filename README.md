# Focalise

## About

Focalise is a productivity tool specifically made for adults with ADHD. Our website features a Google Chrome extension for ease of use when not on the main page. The main features of this app aim to solve the biggest challenges adults with ADHD face whilst trying to be productive online - focus, forgetfulness and sensory overload. The task management feature allows users to organise tasks into categories, organised by priority that will be suggested to the user on opening a new tab/entering the website. When a user wants to get to work they can set a work plan in the workspace, keeping the user on task whilst also sending reminders for regular breaks. If the user wants to take a break from their work/regulate after sensory overload, they can take a break in the sensory room. Here the user is able to set the time they wish to take the break and enjoy calm music/guided meditation/watch live animal cam. There's no need to stress about taking too long on your break as the website will keep track of your break left and redirect you to get back to work once the set time is up.

The Google Chrome extension shows your current tasks set with links back to the Focalise app, for easy access to Focalise's main features even while outside the website.

However you spend your time online, Focalise will make your online experience more productive and enjoyable.

** Please note: This repository only includes the backend of the Focalise website, to get the full website up and running please go to the [frontend repository](https://github.com/anawinter53/i-am-the-walrus-client) and follow the instructions **

## Development

The team followed an Agile methodology for the development of Focalise, using wireframing and Kanban boards. 

We streamlined our development process using our Kanban board on Trello. This allowed us to prioritise the demands of the projects whilst ensuring we weren't all working on the same files, helping us avoid Git merge conflicts as much as possible.

<p align="center">
<img src="" width=75% height=75%>
</p>
<br>

Using Figma we were able to plan out the design for our website before coding it, helping with a more consistent design look across all the team's work. Figma enabled us to conceptualise possible features in a way that allowed for joint planning and more discussions on any new design ideas. 

<p align="center">
<img src="" width=75% height=75%>
</p>
<br>

## Site directory

### Server-side

#### User Routes

| Route | Method | Response |
|-------|--------|----------|
| "/users" | GET | Returns all users |
| "/users/register" | POST | Registers new user with username, email and password |
| "/users/login" | POST | Logs user into their account, redirects to _______ |
| "/users/logout" | POST | Logs user out of their account, redirects to _______ |
| "/users/:user_id" | GET | Finds user profile by their id |

#### User Setting Routes

| Route | Method | Response |
|-------|--------|----------|
| "/settings/:user_id" | GET | Shows settings by user id |
| "/settings/:user_id" | PUT | Updates settings by user id |


#### Task Routes

| Route | Method | Response |
|-------|--------|----------|
| "/tasks/user/:user_id" | GET | Gets all tasks by user id |
| "/tasks/user/:user_id/:category" | GET | Gets all tasks by user id and category |
| "/tasks/user/:user_id" | POST | Add a new task by user id |
| "/tasks/:task_id" | GET | Gets a task by task id |
| "/tasks/:task_id" | PUT | Updates task by task id |
| "/tasks/:task_id" | DELETE | Deletes a task by task id |
| "/tasks/user/:user_id/:category" | DELETE | Deletes task by user id and category |

#### Sensory Routes

| Route | Method | Response |
|-------|--------|----------|
| "/sensory" | GET | Shows all sensory links |


#### Message Routes

| Route | Method | Response |
|-------|--------|----------|
| "/messages" | GET | Shows all messages |


## Required software & accounts
- [VSCode](https://code.visualstudio.com/) or any desired IDE
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [PostgreSQL](https://www.elephantsql.com)

## Installation

1. To get the repository set up on your computer, open your terminal and move into your desired directory using the `cd` command.
2. From the Code button copy the HTTPS/SSH key and run the command `git clone` followed by the key you copied.
3. Move into the repistory and run `code .` to open the code in VSCode/your desired IDE.
4. Run `pipenv shell` to enter the virtual environment
4. Run `pipenv install` to install the necessary dependencies.
5. Create a new instance with Elephant SQL (or another PostgreSQL site) and copy the instance link created.
6. In the root folder create a **.env** file and add the following lines: 
- [x] DB_URL=<postgresql_instance_url> (add 'ql' to the postgres url so it starts with 'postgresql')
- [x] SECRET_KEY=<secret_key>
- [x] SALT_ROUNDS=9

- To generate a secret key, enter the python command line on your terminal with `python` or `python3` depending on your python version.
- Run `import secrets`, then run `secrets.token_hex(16)` 
- Copy the generated secret key and paste it in the .env

7. In the root folder create a **.flaskenv** file and add the following lines: 
- [x] FLASK_APP=app
- [x] FLASK_DEBUG=1
- [x] FLASK_RUN_PORT=<port_number>

Make sure there are no spaces between the content on each line for both .env and .flaskenv files and ensure you don't add any commas or any other punctuation at the end of each line.

8. Set up the database connection by running `pipenv run python create_db.py` or `pipenv run python3 create_db.py`
9. To get the server running, run `pipenv run dev`

