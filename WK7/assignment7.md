## **Week 7 Homework Assignment: Session Management and User Authentication**

### **Objective**:
This week, you'll be delving into the core of application security: user sessions and authentication. Utilizing Flask and an external identity provider like Google Cloud, ensure your Hospital Priceline application is both user-friendly and secure.

### **Instructions**:

#### **1. Session Management with Flask-Session**:
- Integrate Flask-Session into your Hospital Priceline application.
  - Document how you set it up and how it works in managing user sessions.
  - Highlight the benefits of using Flask-Session and any challenges encountered.

#### **2. User Authentication with Flask**:
- Build a robust user authentication system utilizing OAuth 2.0 and Google as the identity provider. This system should cater to:
  - User registration: Automatically register users into your system upon successful authentication with Google.
  - User login: Create a user session upon successful authentication with Google.
  - User logout: Properly terminate and destroy user sessions upon logout.
- Document the security precautions you've taken, such as preventing SQL injection, using secure authentication flows, and ensuring secure session management.

#### **3. Cloud-based Authentication System**:
- Integrate Google Cloud Identity Platform with your application.
- Add functionalities like:
  - Sign-in and Sign-out buttons on your app's user interface.
  - Secure redirecting to and from the Google identity provider.
- Discuss the benefits of using cloud-based identity solutions and their advantages over traditional authentication methods.

### **Submission**:
- Create a new GitHub repository named `flask_7_auth` in your GitHub account.
- Organize your GitHub repository with:
  - Source code reflecting all the changes and integrations made during this assignment.
  - Screenshots or video recordings showcasing the new authentication functionalities.
  - A comprehensive README.md file with:
    - A detailed walkthrough of your user authentication system.
    - Observations on session management and cloud-based authentication.
    - Challenges faced, measures taken to overcome them, and lessons learned.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public for ease of review.

**Tip**: Remember, user data and identity are paramount. Implementing robust authentication and session management systems is not just about functionality but also ensuring the trustworthiness and compliance of your application.