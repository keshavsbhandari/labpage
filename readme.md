Assumptions:
    - Operating system is either Mac or Ubuntu
    - Latest Anaconda3 or Miniconda3 is already installed

Step: 
    1. Go to the root folder, labsite/ if root is different name rename to labsite
        should look like this , 
            labsite
            labsite/labsite/
            labsite/labsite/--entire-projects--here
    
    2. Open terminal-> enable base conda environemtn -> fire following commands 
        $ conda env create -f environment.yml
        Note: environment.yml is an environment file in the root folder
    
    3. Activate the installed environment and install additional requirements

    4. "$pip install -r requirements.txt", make sure you are using pip from this new environment
       for safety: "$python -m pip install -r requirements.txt", works just fine
    
    5. lunch the server: "$python manage.py runserver"

    6. head to admin panel: "http://127.0.0.1:8000/admin/", and login using appropriate username and password


* Let me know if there is any issue

