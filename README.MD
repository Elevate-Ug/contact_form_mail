# Contact Form To Mail
A backend to handle sending responses received via contact forms to the emails they should be going to without spamming said emails.

## USAGE 
In order to get started with the project, you well need to follow the five steps to run the project on your local computer. 

**Here are the steps**
- 1.Create a Virtual Environment
- 2.Activate the Virtual Environment
- 3.Install the packages  
- 4.Rename the .env_example file to .env
- 5.Run a django Migrations for the project  
- 6.Run the development server 


**here they are in Details** 
# 1. Creating the Virtual Env
The first you have need to do is to first Install the **virtualenv package**

The virtualenv package is required to create virtual environments. You can install it with pip:

'''
 pip install virtualenv  
'''

Now create a virtual environment
'''
virtualenv venv
'''

**However**
If you are you are using the latest versions of python, all you need to do is run. 
'''
python -m venv venv
'''

# 2. Active your virtual environment:
To activate your vitual env 
'''
source venv/bin/activate
'''

After activating your virtual environment, you need to head to your project folder 
#  3. Install the packages
To install the project packages
'''
pip install -r requirements.txt
'''
this installs all the dependence's to your virtual env 

# 4.Rename the .env_example file to .env
You need to rename the .env_example file to .env file and make sure to provide the values for the variables provided 
to able to be used


# 5.Run a django Migrations for the project 
'''
python manage.py migrate 
'''

# 6.Run the development server 
'''
python manage.py runserver 
''' 