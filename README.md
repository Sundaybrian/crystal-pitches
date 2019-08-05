# Crystal Pitches

### 02/08/2019

## By **[Brian Sunday](https://github.com/Sundaybrian/crystal-pitches)**

## Description

This is a flask web app that allows users to post pitches and comment on other users' pitches

## User Stories

As a user I would like:
* to sign Up for a pitch account
* to create pitches
* to comment on pitches
* to view pitches of other users


## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : john@doe.com  Username : jonDoo  Password : doe | New user is registered |
| User Log in | Your email : john@doe.com  Password : doe | Logged in |
| Create a Pitch | Click New Pitch |Authenticated User is redirected to a form page to create a pitch |
| View a pitch | Click on a pitch's title | Redirected to a page that has the the pitch|
| Comment on a pitch | Click Comment | Authenticated user is redirected to a form to comment about that pitch|
| Update profile | click your name while logged in | Redirected to a profile page to set your details |


## Setup/Installation Requirements

* `$ git clone` [crystal pitches](https://github.com/Sundaybrian/crystal-pitches)
* `$ cd crystal-pitches`
* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* In the manage.py change app = create_app('production') to app = create_app('development')
* run `$ chmod +x start.sh` (make the program executable)
* `$ ./start.sh` to start the application

## Known Bugs

Profile pictures fail to display


## Technologies Used

* Python3.6
* Flask
* Bootstrap
* Postgres Database
* CSS
* HTML

### License

MIT (c) 2019 **[Brian Sunday](https://github.com/Sundaybrian/crystal-pitches)**


