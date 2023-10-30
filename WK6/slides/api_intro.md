---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# APIs: Application Programmable Interfaces 

**Hants Williams, PhD, RN**

---

# Questions to Consider

As we delve into the world of APIs, let's consider some fundamental questions:

1. How do computers communicate with each other?
2. What methods do software applications use to exchange information?
3. How is data transferred securely between different platforms?
4. What role do protocols play in facilitating communication between devices?

These questions will guide our exploration of APIs and their significance in the digital world.

---

# What is an API?

An API, or Application Programming Interface, is a set of rules and protocols that allows one software application to interact with another.

- **Functionality:** APIs define the methods and data formats that applications can use to request and exchange information.
- **Interoperability:** They allow different software systems to communicate with each other, regardless of their underlying technology or platform.
- **Use Cases:** Common use cases include integrating third-party services, accessing web services, and facilitating communication between microservices.

---

# How Can APIs Help Patients?

APIs in health care centralize and share vital patient information, similar to how travel search engines centralize flight information.

- **Example 1:** Mobile apps use APIs to gather data from fitness trackers and add it to a patient's personal health record.
- **Example 2:** In the future, patients could use APIs to share diagnostic information with their doctors in real-time, such as blood pressure or blood sugar levels.

---

# The Importance of APIs in Healthcare

With the advent of certified electronic health records, APIs have become more crucial in healthcare.

- **Certified Electronic Health Records:** These records are required to provide APIs to help patients connect and share health information.
- **Patient Portals:** Patients can use APIs to gather and share health information from healthcare providers' patient portals, improving the overall healthcare experience.

---

# Federal Rules for Data Transfer in Healthcare

There are several federal rules and regulations that healthcare providers must comply with when using apps to transmit data.

- **Health IT Certification Criteria (2015):** This regulation requires certified health IT to provide access to health information using APIs.
- **HIPAA (1996):** Providers must release certain requested data to patients and provide security and privacy technical safeguards.

---

# Regulatory Bodies and Additional Regulations

Various federal agencies are responsible for enforcing these rules and regulations.

- **Office for Civil Rights:** Enforces HIPAA privacy and security rules.
- **Federal Trade Commission (FTC):** Prohibits unfair or deceptive acts or practices and requires reasonable and appropriate data security.
- **Food and Drug Administration (FDA):** Requires that apps protect information accessed or transferred from medical devices.

---

# The Structure of an API

An API consists of several key components that work together to facilitate communication between software applications.

- **Endpoints:** Specific URLs where API requests can be made.
- **Methods:** Define the actions that can be performed, such as GET, POST, PUT, and DELETE.
- **Request:** The data sent to the API, which may include parameters, headers, and body content.
- **Response:** The data returned by the API, usually in JSON or XML format.
- **Authentication & Authorization:** Mechanisms to verify the identity of the requestor and their permissions.
- **Rate Limiting:** Restrictions on the number of requests that can be made in a given time period.

---

# API Endpoints

An endpoint is a specific URL where an API can receive requests and send responses. It acts as a point of communication between the client and the server.

- **Structure:** Typically consists of a base URL followed by a path that identifies the specific resource or operation.
- **Example:** `https://api.example.com/v1/users`
- **Resource:** The data or service that the endpoint provides access to.
- **Operations:** The actions (methods) that can be performed on the resource, such as retrieving, updating, or deleting data.
- **Parameters:** Additional information that can be included in the request to further specify the desired operation or data.

Endpoints are the building blocks of an API, and each endpoint corresponds to a specific function or feature of the application.

---

# API Methods

API methods define the actions that can be performed on the resources exposed by an API. Common HTTP methods used in APIs include:

- **GET:** Retrieve information about a resource.
- **POST:** Create a new resource or perform an action.
- **PUT:** Update an existing resource with new data.
- **PATCH:** Partially update an existing resource with new data.
- **DELETE:** Remove a resource.

Each method serves a specific purpose in the interaction between the client and the server, and the choice of method depends on the desired operation and the API's design.

---

# API Requests

An API request is made by the client to the server to retrieve or send data. It consists of the endpoint, method, headers, parameters, and body.

**Examples:**

1. GET Request without Parameter
   - Endpoint: `https://api.example.com/users`
   - Method: GET

2. GET Request with Parameter
   - Endpoint: `https://api.example.com/users`
   - Method: GET
   - Parameter: `?name=John`

---

3. POST Request with Body
   - Endpoint: `https://api.example.com/users`
   - Method: POST
   - Body: `{"name": "John", "age": 30}`

These examples illustrate how different types of requests are constructed to interact with an API.


--- 

# Focusing on HTTP Requests

In this presentation, we will be focusing on HTTP requests, specifically those accessible via the web.

- **HTTP Requests:**
  - Utilize the HTTP protocol to send and receive data over the web.
  - Can be accessed via URLs.

---

# Focusing on HTTP Requests


- **Inputs:**
  - **URL Arguments:**
    - Inputs can be included in the URL as arguments, using the `?` character.
    - Example: `https://api.example.com/users?name=John`
  
  - **POST Requests with JSON Body:**
    - Inputs can also be included in the body of a POST request, usually in JSON format.
    - Example:
      ```sh
      curl -X POST https://api.example.com/users -H "Content-Type: application/json" -d '{"name": "John"}'
      ```

---

# API Responses

An API response is the data returned by the server in response to a client's request. It consists of a status code, headers, and body.

- **Status Code:** Indicates the result of the request (e.g., 200 for success, 404 for not found).
- **Headers:** Provide additional information about the response, such as content type.
- **Body:** Contains the actual data returned by the API, usually in JSON or XML format.

---

**Response Examples:**

1. Successful Response
   - Status Code: 200 OK
   - Body: `{"message": "User created successfully"}`

2. Not Found Response
   - Status Code: 404 Not Found
   - Body: `{"error": "User not found"}`

Understanding the structure and content of API responses is crucial for effectively handling the data returned by the API.


---

# Common API Responses

Here are some of the most common HTTP status codes you might encounter when working with APIs:

- **200 OK:** The request was successful, and the server has returned the requested data.
- **201 Created:** A new resource has been successfully created as a result of the request.
- **400 Bad Request:** The server could not understand the request due to invalid syntax.
- **401 Unauthorized:** The request lacks valid authentication credentials.
- **403 Forbidden:** The client does not have the necessary permissions for the requested operation.
- **404 Not Found:** The server could not find the requested resource.
- **500 Internal Server Error:** The server encountered an unexpected condition that prevented it from fulfilling the request.


---

# API Authentication

Authentication is the process of verifying the identity of the client making the API request.

- **API Key:** A unique identifier passed in the request headers to authenticate the client.
- **OAuth:** A protocol that allows secure authorization from web, mobile, and desktop applications.
- **JWT (JSON Web Tokens):** A compact, URL-safe means of representing claims to be transferred between two parties.

Each authentication method has its own advantages and is suitable for different use cases.


---

# API Authorization

Authorization is the process of verifying that the authenticated client has the necessary permissions to access the requested resource.

- **Roles and Permissions:** Define what actions an authenticated client can perform.
- **Scope:** Specifies the extent of access granted to the client.
- **Access Control Lists (ACLs):** A list of permissions attached to an object that specifies which users or system processes can access that object.

Authorization ensures that clients can only access the data and perform the actions they are allowed to.


--- 

# Testing APIs with CURL

`curl` is a command-line tool that can be used to send HTTP requests and test APIs directly from the Command Prompt.

**Examples using JSONPlaceholder:**

1. GET Request
   ```sh
   curl https://jsonplaceholder.typicode.com/posts/1
   ```
   
2. POST Request
   ```sh
   curl -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d '{"title": "foo", "body": "bar", "userId": 1}'
   ```
---

3. PUT Request
   ```sh
   curl -X PUT https://jsonplaceholder.typicode.com/posts/1 -H "Content-Type: application/json" -d '{"id": 1, "title": "foo", "body": "bar", "userId": 1}'
   ```

4. DELETE Request
   ```sh
   curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
   ```

These examples show how to use `curl` to test different types of API requests with JSONPlaceholder and see the responses returned by the server.


---

# The Importance of API Documentation

API documentation is crucial for developers and users to understand how to interact with an API effectively.

- **Clarity:** Provides clear and concise information about the API's functionality, including endpoints, methods, parameters, and responses.
- **Ease of Use:** Helps developers quickly learn how to use the API and integrate it into their applications.
- **Testing:** Offers examples and guidelines for testing the API, ensuring it works as expected.
- **Maintenance:** Facilitates easier maintenance and updates by documenting the API's structure and behavior.
- **Community:** Fosters a community of developers who can contribute to and improve the API.

Proper documentation is the key to a successful API and a positive developer experience.

---

# The Importance of Detailed API Documentation

- **Example: Stripe API Documentation**
  - **Complexity:** Stripe's API is complex and feature-rich, supporting a wide range of payment and financial operations.
  - **Documentation:** Despite its complexity, Stripe's API documentation is detailed, clear, and user-friendly, with interactive examples, clear explanations, and a well-organized structure.
  - **Developer Experience:** This level of detail and organization makes it easier for developers to integrate Stripe's services into their applications, leading to a positive developer experience.

Just like Stripe, companies like Zoom, Uber, Netflix, etc... invest in detailed API documentation to ensure a smooth and positive experience for developers who use their APIs.

---

# Swagger, OpenAPI, and Flasgger

Swagger and the OpenAPI Standard are tools and specifications that help to design, build, document, and consume REST APIs.

- **Swagger:**
  - A set of tools for designing, building, and documenting REST APIs.
  - Includes a UI for visualizing and interacting with the API's resources.

- **OpenAPI Standard:**
  - A specification for building APIs that is used by Swagger tools.
  - Defines a standard, programming language-agnostic interface description for HTTP APIs.

---

# ...continued

- **Flasgger:**
  - A tool we will use in our Flask example to utilize Swagger for API documentation.

Together, Swagger, OpenAPI, and Flasgger provide a powerful and standardized way to create and document REST APIs, making them easier to understand and use.

---

# Deploying API Endpoints as Azure Functions

Azure Functions is a serverless compute service that lets you run event-triggered code without having to provision or manage infrastructure.

- **Single API Endpoint:**
  - You can deploy a single API endpoint as an Azure Function.
  - The function is triggered by an HTTP request and can return a response.
```text
- Benefits: 
  - Scalability: Azure handles the scaling of the function as needed.
  - Cost-Effective: You only pay for the compute time you use.
  - Quick Deployment: Deploy and update your API endpoint easily.
```

https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators 

---

# Deploying API Endpoints as Google Cloud Functions

Google Cloud Functions is a lightweight, event-driven, serverless computing platform that allows you to create small, single-purpose functions.

- **Single API Endpoint:**
  - A single API endpoint can be deployed as a Google Cloud Function.
  - The function responds to HTTP requests and returns the desired response.

- **Benefits:**
  - Same as Azure benefits 

https://cloud.google.com/functions/docs/create-deploy-http-python 

---

# Practical Examples

Now that we've covered the basics, let's dive into some practical examples to see how these concepts are applied in real-world scenarios.

1. **Traditional Flask Application:**
   - We will first look at the manual way of creating a Flask application and understand how the endpoints are defined and interacted with.

2. **Google Cloud Platform (GCP):**
   - Next, we will explore how to deploy a single API endpoint as a Google Cloud Function and see how it simplifies the process.

3. **Azure (Self-Study):**
   - Lastly, I encourage you to explore deploying an API endpoint as an Azure Function on your own to compare and contrast with GCP.
