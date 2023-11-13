## **Week 8 Homework Assignment: Application Deployment & CI/CD Integration**

### **Objective**:
As developers, not only do we build, but we also deploy. This week is all about taking your Hospital Priceline application to the internet across various platforms and automating your deployment process. You'll be using platforms like Vercel, Google Cloud, Azure, and tools like GitHub Actions and Docker.

### **Instructions**:

#### **1. Deploying to Vercel**:
- Deploy your Hospital Priceline application on Vercel.
  - Document the steps taken and any configurations you needed to set up.
  - Share the live link to your deployed application.
  - (Optional) Acquire and set up a custom domain for your deployed Vercel application.

#### **2. Multicloud Deployment**:
- Deploy your Hospital Priceline application to:
  - Google Cloud Run
  - Azure App Service
- Document any differences observed during the deployment process on both platforms.
- Share the live links to your deployed applications on both platforms.

#### **3. CI/CD Automation with GitHub Actions**:
- Set up a CI/CD pipeline using GitHub Actions for your application.
  - Ensure the pipeline is triggered whenever you push to a specific branch (e.g., `main` or `deploy`).
  - The pipeline should automate deployment to the Azure App Service.
  - Document the steps to set up the CI/CD pipeline, including any `.yml` configuration files used.
  - Share evidence (e.g., screenshots or logs) of successful pipeline runs and application deployments.

#### **4. (Optional) Containerization and Deployment**:
- Containerize your Flask/FastAPI application using Docker.
  - Write and document a Dockerfile for your application.
  - Push your containerized app to Docker Hub.
- Deploy the containerized application to Azure Container Apps.
  - Document the deployment process and any challenges faced during containerization and deployment.
  - Share the live link to your containerized application running on Azure Container Apps.

### **Submission**:
- Create a new GitHub repository named `flask_8_deployment` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- The GitHub repository should contain:
  - All source code and configuration files related to deployments.
  - Screenshots or video recordings highlighting successful deployments and CI/CD pipeline runs.
  - A comprehensive README.md file detailing:
    - Your deployment processes for each platform.
    - Observations, challenges, and your CI/CD setup.
- Provide the link to your repository as your assignment submission.
- Make sure your repository is set to public for ease of review.

**Tip**: Deployment can be tricky, and it's not uncommon to face issues. Document your process thoroughly. It not only helps in troubleshooting but also serves as a guide for future projects.
