## **Week 9 Homework Assignment: Monitoring, Logging & Tracing**

### **Objective**:
This week focuses on the crucial aspects of monitoring and logging to understand and diagnose application behaviors. By integrating appropriate tools and deliberately inducing errors, you'll gain firsthand experience in troubleshooting and optimizing application performance.

### **Instructions**:

#### **1. Logging with Python**:
- Integrate Python's built-in logging module into your Flask or FastAPI application.
  - Ensure logs are captured at different severity levels: INFO, WARNING, and ERROR.
  - Document your logging configuration and showcase sample logs from each severity level.

#### **2. Distributed Tracing**:
- Implement distributed tracing for your application.
  - You may use OpenCensus or a similar platform of your choice.
  - Provide a brief overview of your tracing setup, and share screenshots or outputs showing traced requests or processes within your application.

#### **3. Cloud-based Monitoring**:
- Integrate your application with either:
  - Azure Monitor 
  - Or, Google Cloud Monitoring.
- Set up basic performance metrics monitoring for your application, such as:
  - Server response times.
  - Number of active users or sessions.
  - Error rates.
  - Document the steps taken to integrate cloud monitoring and share relevant screenshots or visualizations of your monitored metrics.

#### **4. Diagnosing Issues with Logging**:
- Intentionally trigger an error or exception within your application.
  - Utilize your logging setup to diagnose the issue and determine its cause.
  - Document the error you triggered, how it manifested in your logs, and your diagnosis based on the logs.

#### **5. (Optional) Proactive Monitoring with Alerts**:
- Set up alerts or notifications in either Azure Monitor or Google Cloud Monitoring.
  - Define specific conditions for the alerts, such as server response time exceeding a certain threshold or error rates spiking.
  - Document your alert configuration and, if possible, showcase the alert in action, either through a screenshot of the notification or the platform's alert dashboard.

### **Submission**:
- Create a new GitHub repository named `flask_9_monitoring` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- The GitHub repository should contain:
  - All relevant source code, configuration files, and scripts.
  - Screenshots, video recordings, or any visual evidence supporting your monitoring, logging, and tracing setups.
  - A comprehensive README.md file detailing:
    - Your setups for logging, tracing, and monitoring.
    - Observations, triggered errors, and diagnostics.
- Provide the link to your repository as your assignment submission.
- Make sure your repository is set to public for ease of review.

**Tip**: Effective logging and monitoring are about more than just setup – they are about understanding. Ensure you grasp the significance of the data you're capturing and how it can inform your actions as a developer.
