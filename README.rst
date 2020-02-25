Health Research Portal
======================
This is a project that scrapes various health research portals to retrieve useful data.

How to install the project
--------------------------
Prerequisites
~~~~~~~~~~~~~
Make sure you have the following before beginning:

	- python3-dev
	- git
	- pip
	- virtualenv
	- postgresql

Cloning from Github
~~~~~~~~~~~~~~~~~~~
From your terminal got to the directory you want to clone your project into.

.. code:: bash

	$ cd path/to/your/directory

Clone the project

.. code:: bash

	$ cd git clone git@github.com:health_research_portal/health_research_portal.git

Set up the environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a env.sh file in your parent project directory

.. code:: bash

	$ cd path/to/your/directory/health_research_portal
	$ touch env.sh

Add these environment variables to your ``env.sh`` file:

.. code:: bash

    #!/usr/bin/env bash
    export SECRET_KEY="your-secret-key"
    export DEBUG="true"
    export DB_NAME="name_of_db"
    export DB_USER="name_of_user"
    export DB_PASS="password"
    export DB_HOST=""
    export DB_PORT=""
	
Setting up the projects dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Navigate into the projects directory from the terminal.

.. code:: bash

	$ cd path/to/your/directory/health_research_portal

Create a virtual environment for your project

.. code:: bash

	$ python3 -m venv name-of-your-virtualenv

Activate your virtual environment.

.. code:: bash

	$ source name-of-your-virtualenv/bin/activate

Install the requirements.

.. code:: bash

	(name-of-your-virtualenv)$ pip3 install -r requirements.txt

Running and testing the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run the project:

.. code:: bash
	
	(name-of-your-virtualenv)$ ./manage.py runserver # the information below will be displayed if everything is okay
	Performing system checks...

	System check identified no issues (0 silenced).
	January 18, 2020 - 18:55:56
	Django version 3.0, using settings 'config.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.
	
To test the project:

.. code:: bash

	(name-of-your-virtualenv)$ pytest # This will run all the tests in the project

Credits
-------
Developed by **Kenneth Mathenge**
