## **Week 13 Homework Assignment: Serverless Functions**

### **Objective**:
Embrace the power of serverless computing in this week's assignment. Serverless computing enables you to build and run applications without thinking about the underlying infrastructure. This can result in more efficient resource utilization, scalability, and reduced operational complexities. 

### **Instructions**:

#### **1. Analytical Serverless Function**:
- Develop a serverless function (e.g., using Azure Functions or Google Cloud Functions) that:
  - Takes in hospital pricing data as input.
  - Computes the average price for a specified medical procedure across all hospitals.
  - Returns the calculated average price as the output.
- This function will offload the analytical processing from the main application, helping maintain application responsiveness.

#### **2. Notification Serverless Function**:
- Design another serverless function that:
  - Can be triggered when new hospital pricing data is available or when there are significant fluctuations in pricing.
  - Sends an email notification to users informing them about the updates or changes.
  - Consider using services like SendGrid or similar for the email notifications.

#### **3. Integration with Hospital Priceline**:
- Integrate both the serverless functions into the Hospital Priceline application.
  - Ensure the analytical function is invoked whenever relevant analytical data is requested.
  - The notification function should be triggered under the defined conditions (new data or significant price changes).
  
#### **4. Performance Analysis**:
- After integrating the serverless functions:
  - Measure and document the performance and latency of the main application, especially during heavy analytical processing.
  - Compare this to the performance observed when such processing was handled directly by the application.
  - Discuss the benefits, both in terms of application responsiveness and potential cost savings, when offloading tasks to serverless functions.

### **Submission**:
- Create a new GitHub repository named `flask_13_security` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- The GitHub repository should contain:   
  - All the updated source code and configuration files.
  - Serverless function definitions and deployment configurations.
  - Visual evidence like screenshots or video recordings, demonstrating the functions in action and their impact on application performance.
  - Your performance analysis documentation.
  - A detailed README.md file that:
    - Summarizes the purpose, functionality, and triggers of each serverless function.
    - Provides insights into the challenges faced and the benefits realized from serverless computing.
- Provide the link to your repository as your assignment submission.
- Make sure your repository is public for easier access and evaluation.

**Tip**: Serverless computing offers a unique advantage by only charging for the actual amount of resources consumed by executions, rather than pre-purchased capacity. This can be particularly cost-effective for sporadic or unpredictable workloads.
