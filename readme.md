# pharmacy project

this project is about pharmacies managament system for 
manage operations between many pharmacies in one group



# Prerequisites

# internet for connect to database
you can run this project one of two methods 
## python version 3.9
or
## docker 

### lets take the first one 

after install python version 
- enter inside project and run the next command
` virtualenv project-env `
- after create environment we will activate this env by next command
 ` source env/bin/activate ` if lunix
 ` venv\Scripts\activate ` if window
- after activate env we will install our packages by run 
 ` pip install -r requirements.txt `
- after that we will run the project by command 
 ` python setup/manage.py runserver `

### lets take the second 

after install docker we will 
- install docker-compose make sure is exist
- enter inside project and run the next command
` docker-compose up --build `