## **Week 5 Homework Assignment: Design, Cloud CDN & Asset Optimization**

### **Objective**:
This assignment will have you wearing the hat of a front-end developer, introducing you to Tailwind CSS, a utility-first CSS framework. Not only will you design a user-friendly interface but you'll also leverage Google Cloud CDN to serve static assets, ensuring your application is performant and optimized for users worldwide.

### **Instructions**:

#### **1. Responsive Design with Tailwind CSS**:
- Use Tailwind CSS to design a search page for the Hospital Priceline application.
  - Your design should be clean, intuitive, and responsive, ensuring a consistent look and feel across various device sizes.
  - If you're new to Tailwind, explore their [documentation](https://v2.tailwindcss.com/docs) for guidance.

#### **2. Incorporate Thematic Imagery**:
- Integrate at least two static images that resonate with the Hospital Priceline theme. 
  - Suggestions include hospital emblems, medical symbols, price tags, or currency icons.
  - Ensure images are of high quality but optimized for the web (avoid very large file sizes).

#### **3. Google Cloud CDN & Asset Hosting**:
- Host Tailwind CSS library, your chosen static images, and any other relevant assets on Google Cloud CDN.
  - Refer to Google's official [documentation](https://cloud.google.com/cdn) on how to set up and use Cloud CDN.
  - For integrating with Flask, this [guide](https://cloud.google.com/appengine/docs/flexible/serving-static-files?tab=python) may be beneficial.
  - Ensure all assets (CSS, JS, images) in your Flask application are linked to their CDN URLs.

#### **4. Validate Asset Delivery**:
- Confirm and validate that your assets (like images, CSS) are indeed being served from the Google Cloud CDN.
  - This can be checked using browser developer tools or services like GTmetrix.
  - Provide screenshots or other evidence showcasing the CDN's URL and the faster load times as a result of using the CDN.

#### **5. Delve Deeper with Caching** *(Optional)*:
- Delve into Google Cloud CDN's caching configurations.
  - Implement a custom caching rule for one of your static assets.
  - Document the configuration you set up, its purpose, and expected outcomes. Highlight any noticeable performance differences or changes in asset delivery behavior.

### **Submission**:
- Create a new GitHub repository named `flask_5_tailwind` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
- Prepare your GitHub repository:
  - Your Flask application with integrated Tailwind CSS design.
  - Screenshots or videos showcasing the responsive design across different device sizes.
  - Screenshots confirming assets are being served from Google Cloud CDN.
  - Any optional task documentation, especially regarding caching configurations.
  - A detailed README.md file, outlining:
    - Your design rationale and principles followed.
    - Steps for setting up and using Google Cloud CDN with Flask.
    - Your observations and benefits of using a CDN.
    - Any challenges encountered and how you addressed them.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Performance matters! The more optimized your assets are and the better they're served (e.g., via CDN), the better the user experience.
