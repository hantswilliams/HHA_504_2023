# Final Assignment (Product / Web Service)

## Technologies (approaches) that will be used for final assignment:  
- Github (Version Control)
- Flask (Python; Frotend & Backend)
- MySQL (Database via GCP or Azure)
- SQLAlchemy (ORM)
- .ENV (Environment Variables)
- Tailwind (Frontend Styling)
- Authorization (Google OAuth)
- API Service (Flask Backend)
- Logger and or Sentry.io (Debugging & Logging)
- Docker (Containerization)
- GCP or Azure (Deployment) 

## Product (Web Service) Description
For this final project, you will combine many of the tools and services explored over the semester. 

There are 11 section (requirements) below, each worth 10 points. You will need to complete 10 of the 11 sections to get full credit for the assignment. You can choose which 10 sections you want to complete. 

If you complete all 11, you have the opportunity to earn 10 extra credit points - potentially receive 110/100 points for the assignment.

## Web Service Requirements
- [ ] Create a product that uses a version control system (Github): 10 points
- [ ] Create a product that uses a environment variables (.env): 10 points
- [ ] Create a product that uses a backend framework (Flask): 10 points
- [ ] Create a product that uses a frontend framework (Tailwind): 10 points
- [ ] Create a product that uses a database (MySQL): 10 points
    - Option 1: Azure 
    - Option 2: GCP
- [ ] Create a product that uses a ORM (SQLAlchemy): 10 points
- [ ] Create a product that uses an API or offers an API service (Flask): 10 points
    - Option 1: the API service can be a single endpoint that is hosted on GCP or Azure and connects to your Flask backend
    - Option 2: or the API service can be a single endpoint that is within your Flask backend
- [ ] Create a product that uses authorization (Google OAuth): 10 points
- [ ] Create a product that uses a logger (Logger or Sentry.io): 10 points
    - Option 1: built in Logger
    - Option 2: Sentry.io
- [ ] Create a product that is containerized (Docker): 10 points
- [ ] Create a product that is deployed to the cloud (GCP or Azure): 10 points
    - Option 1: GCP
    - Option 2: Azure

## Web Service Description
You can create any web product (service) you want. It should be:
- Be healthcare oriented 
- Be something of interest to you
- Be something you can complete in 2 weeks
- Be something you can demo to the class
- Require the use of the technologies listed above
- It should do something: either display some type of data, allow users to enter data and get a result, or allow users to enter data and store it in a database and then display it
- Data Requirement: 
    - Option 1: Involve the use of external data that can be cleaned, brought into a database, and used in your product
    - Option 2: Involve the use of fake data that you create and store in a database and use in your product
    - Option 3: Involve a form that allows users to enter data that is stored in a database and used in your product (e.g., a form that allows a user to enter in healthcare data that is stored in a database and used in your product/service) 

## Github Repository Requirements
- [ ] Create a Github repository for your project called `flask_e2e_project`
- [ ] Folder structure: 
    - A `readme.md` file that contains all of your documentation and references all of your screenshots and videos
        - It should contain a brief explanation of 
            - The web service you created (what is it and what does it do)
            - The technologies you used
            - The steps to run your web service if someone wanted to either run locally or deploy to the cloud
                - How could they run it without Docker locally? 
                - How could they run it with Docker locally?
                - How could they deploy it to the cloud?
        - A template of the .env file structure you used, which should include all of the environment variables you used like below. Please be sure to NOT include your actual API keys in the github repo.:
            - Database connection string
            - API keys
            - etc.
    - A folder called `app` that contains all of your Flask code
        - At a minimum, inside of this folder you should have:
            - A file called `app.py` that contains all of your Flask code
            - A folder called `templates` that contains all of your HTML templates
            - A folder called `static` that contains all of your static files (e.g., CSS, JS, images, etc.) if you use any
    - A folder called `db` that contains all of your database code (e.g., python/SQL scripts for creating tables, inserting data, etc.)
    - A folder called `data` that contains any data you use in your project; if you use fake data, you can create it in this folder. If your data is too big (e.g., > 100 MB), you can store it in a cloud storage bucket and provide a link to it in your README.md file OR create a smaller version of the data and store it in this folder
    - A folder called `docs` that contains all of your documentation (e.g., README.md, screenshots, etc.)
    - A folder called `logs` that contains all of your logs if you use the built in logger
        - If you use Sentry.io, you can store your logs in this folder or in your Sentry.io account and take screenshots of a few of them and place it into the `docs` folder
    - A file called `.gitignore` that contains all of the files you want to ignore in your repository
    - A file called `requirements.txt` that contains all of your dependencies
    - A file called `Dockerfile` that contains all of your Docker commands
        - Or a file called `docker-compose.yml` that contains all of your Docker Compose commands if you use Docker Compose
        




