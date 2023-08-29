## **Week 10 Homework Assignment: Scaling and Load Balancing**

### **Objective**:
As web applications grow, they need to accommodate larger user bases, withstand peak traffic moments, and still offer a seamless user experience. This week, you'll dive deep into the concepts of scaling, load balancing, caching, and containerization to ensure your application performs optimally under varied loads.

### **Instructions**:

#### **1. Load Balancing**:
- Set up a basic load balancer for your Flask or FastAPI application on either Azure or Google Cloud.
  - Ensure it effectively routes traffic to multiple instances of your application.
  - Document the steps taken for the setup and provide evidence (like screenshots) showcasing the traffic distribution among multiple instances.

#### **2. Caching for Performance**:
- Integrate a caching solution, like Redis, into your application.
  - Focus on caching frequently accessed database queries or static assets.
  - Document your caching strategy: What did you decide to cache and why? 

#### **3. Simulating Traffic and Monitoring**:
- Use tools such as locust.io to simulate high traffic directed at your application.
  - Monitor your application's behavior under this load.
  - Identify and document potential bottlenecks and areas for improvement.

#### **4. Auto-scaling**:
- Implement auto-scaling rules for your application based on specific metrics like CPU or memory usage.
  - Share the configuration and reason behind choosing specific thresholds for scaling up or down.

#### **5. Case Study on High-Traffic Applications**:
- Research a popular high-traffic web application (e.g., Twitter, Netflix).
  - Write a brief report detailing:
    - How the application manages scaling.
    - Strategies employed to handle large user bases and peak traffic moments.
    - CDN usage, database scaling techniques, and challenges during major events.
  - Ensure your report is concise, well-referenced, and illuminating.

#### **6. (Optional) Containerization and Orchestration**:
- Consider containerizing your application using Docker.
  - Then deploy it on an orchestration platform like Azure Kubernetes Service (AKS) or Google Kubernetes Engine (GKE).
  - Discuss potential benefits of containerization and orchestration in terms of scaling and application management.

### **Submission**:
- Create a new GitHub repository named `flask_10_scaling` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- The GitHub repository should contain:
  - All relevant source code, configuration files, and scripts.
  - Visual evidence like screenshots or video recordings showcasing your setups, traffic simulations, and cache hits/misses.
  - Your high-traffic application case study report.
  - A detailed README.md file that:
    - Explains your setups, strategies, and observations.
    - Contains reflections on bottlenecks, improvements, and auto-scaling strategies.
- Provide the link to your repository as your assignment submission.
- Ensure your repository is set to public for ease of review.

**Tip**: Scaling an application requires a mix of technical implementations and strategic decisions. Reflect on why specific strategies are suitable for certain scenarios.
