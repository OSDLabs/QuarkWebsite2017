# Quark Website 2017


##About
The official repository of the site of Quark, the annual cultural fest of BITS Pilani, Goa. 
Made using Django Framework of Python for server side. 

##Link
Hosted live on [bits-quark.org](http://bits-quark.org). The changes will be pushed thrice a week (or as and when necessary).

## Contribution

### Installation

If you are new to github, follow [git-task](https://github.com/OSDLabs/git-task) repository for basic knowledge on how to contribute.

* Make a fork of this repository on your account.

* Assuming you have python 3.4 already installed, go to the desired folder on your machine and follow these commands to clone the repository and install dependencies in a virtual environment:

```
$ virtualenv quark
$ cd quark
$ source bin/activate
$ git clone https://github.com/[USERNAME]/QuarkWebsite2017 src
$ cd src
$ pip install -r requirements.txt
```
NOTE for windows in the 3rd line use:
```
$ quark\Scripts\activate
```

* db.sqlite3 is the database for this repository, you can delete that if you want to start with a fresh database and follow: (But not required and can skip this step)

```
$ python manage.py migrate
```

* Create a superuser for admin controls (accessible at localhost:8000/admin)

```
$ python manage.py createsuperuser
```

* Run the server and access at localhost:8000

```
$ python manage.py runserver
```


### Contributing Guidelines

If you have any issues with the code or anything, put in one at the issues section of the repository before giving in a pull request. 

##Authors

* Sebastin Santy
* Ayush Sharma