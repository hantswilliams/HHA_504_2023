## **Week 7 Homework Assignment: Session Management and User Authentication**

### **Objective**:
This week, you'll be delving into the core of application security: user sessions and authentication. Utilizing Flask, and external identity providers like Azure and Google Cloud, ensure your Hospital Priceline application is both user-friendly and secure.

### **Instructions**:

#### **1. Session Management with Flask-Session**:
- Integrate Flask-Session into your Hospital Priceline application.
  - Document how you set it up and how it works in managing user sessions.
  - Highlight the benefits of using Flask-Session and any challenges encountered.

#### **2. User Authentication with Flask**:
- Using the `identity` and `identity.web` modules, build a robust user authentication system. This system should cater to:
  - User registration: Ensure passwords are hashed securely before storing.
  - User login: Create a user session upon successful login.
  - User logout: Properly terminate and destroy user sessions upon logout.
- Document the security precautions you've taken, such as preventing SQL injection, using password hashing, and ensuring secure session management.

#### **3. Cloud-based Authentication System**:
- Integrate a cloud-based identity provider with your application. You can choose between:
  - Azure Active Directory B2C
  - Google Cloud Identity Platform
- Add functionalities like:
  - Sign-in and Sign-out buttons on your app's user interface.
  - Secure redirecting to and from the cloud identity provider.
- Discuss the benefits of using cloud-based identity solutions and their advantages over traditional authentication methods.

#### **4. Advanced Authentication with Azure Managed Identity**:
- Dive deeper into authentication by following the [Azure Managed Identity with Python](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-overview?tabs=python) tutorial.
  - Enhance the security and user experience of your app's authentication flow.
  - Document key takeaways, benefits, and any challenges faced during this integration.

### **Submission**:
- Create a new GitHub repository named `flask_7_auth` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- Organize your GitHub repository with:
  - Source code reflecting all the changes and integrations made during this assignment.
  - Screenshots or video recordings showcasing the new authentication functionalities.
  - A comprehensive README.md file with:
    - A detailed walkthrough of your user authentication system.
    - Observations on session management, traditional vs. cloud-based authentication, and advanced authentication measures.
    - Challenges faced, measures taken to overcome them, and lessons learned.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public for ease of review.

**Tip**: Always remember, user data and identity are critical. Implementing robust authentication and session management systems isn't just about functionality but ensuring the trustworthiness of your application.
