## **Week 11 Homework Assignment: Cloud Storage Integration**

### **Objective**:
In this week's assignment, you'll be focusing on integrating cloud storage solutions into the Hospital Priceline application. As data grows, especially unstructured data like images and documents, leveraging cloud storage becomes essential. This assignment will expose you to handling file uploads and understanding the cost models associated with cloud storage.

### **Instructions**:

#### **1. Local File Upload**:
- Modify your Hospital Priceline application to allow users to upload their proof of pricing, such as a bill or a receipt.
  - Initially, store this uploaded file locally within your Flask or FastAPI application.
  - Ensure appropriate security measures are in place to sanitize uploaded files and prevent malicious activities.

#### **2. Cloud Storage Integration**:
- Choose either Azure Blob Storage or Google Cloud Storage as your cloud storage solution.
  - Transition from your local storage solution to your chosen cloud storage platform.
  - Adjust your application to read and write the uploaded files directly from/to this cloud storage.
  - Document the necessary configuration, setup, and changes made to your application for this transition.

#### **3. Cloud Storage Cost Analysis**:
- Research the pricing model of the cloud storage solution you've chosen.
  - Write a brief report detailing:
    - The specific pricing model of your chosen cloud storage.
    - How its costs compare to traditional hosting or databases.
    - Insights on how to optimize storage costs without compromising on functionality or security.

### **Submission**:
- Create a new GitHub repository named `flask_11_storage` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- The GitHub repository should contain:  
  - All relevant source code, configuration files, and scripts.
  - Visual evidence like screenshots or video recordings showcasing the file upload functionality and storage transition.
  - Your cloud storage cost analysis report.
  - A detailed README.md file that:
    - Explains your setups, integrations, and observations.
    - Contains reflections on the challenges faced during cloud storage integration and the advantages it brings.
- Provide the link to your repository as your assignment submission.
- Ensure your repository is set to public for ease of review.

**Tip**: While cloud storage solutions offer scalability and performance, they come with their own sets of challenges like latency and costs. Always balance the needs of the application with the advantages and limitations of the storage solution.
