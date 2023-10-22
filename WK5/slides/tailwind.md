---
marp: true
theme: default
paginate: true
---

<!-- _class: lead -->

# Tailwind CSS: CSS Framework for Styling 

**Hants Williams, PhD, RN**

---

# Question:

What is the traditional way of writing CSS?

---

# Answer:

- Writing CSS classes in a stylesheet
- Linking the stylesheet to the HTML file
- Applying the classes to HTML elements


---

Example: https://jsfiddle.net/ 

```html
<body>
    <header>
        <h1>My Flask App</h1>
    </header>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Services</a>
        <a href="#">Contact</a>
    </nav>
    <main>
        <h2>Welcome to My Flask App</h2>
        <p>This is a simple Flask app with inline CSS.</p>
    </main>
    <footer>
        <p>Copyright © 2023 My Flask App</p>
    </footer>
</body>
```


---

```css

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}
header {
    background-color: #4CAF50;
    color: #ffffff;
    text-align: center;
    padding: 1em 0;
}
nav {
    display: flex;
    justify-content: space-between;
    background-color: #333;
    padding: 0.5em;
}
nav a {
    color: #ffffff;
    text-decoration: none;
    padding: 0.5em 1em;
}
nav a:hover {
    background-color: #ddd;
    color: #333;
}
main {
    padding: 2em;
}
footer {
    text-align: center;
    padding: 1em 0;
    background-color: #4CAF50;
    color: #ffffff;
}


```

---

# Question:

What challenges might you face with traditional CSS?

---

# Answer:

- CSS files can become large and difficult to manage
- Styles can be hard to reuse across projects
- Conflicts can occur when combining multiple stylesheets

---

# What is Tailwind CSS?

Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to build designs directly in your markup.

---

# How Tailwind CSS Works

1. Write utility classes directly in the HTML file
2. Styles are applied in real-time
3. No need for a separate stylesheet

---

# Benefits of Tailwind CSS

- **Simplicity:** Easy to write and understand styles
- **Speed:** Faster development time
- **Consistency:** Consistent styling across your project
- **Customization:** Easily customize styles to fit your design needs

---

# Tailwind CSS in Action

1. Install Tailwind CSS using npm or yarn
2. Configure your settings in the `tailwind.config.js` file
3. Start building your design using utility classes

Live example: [Tailwind CSS Playground](https://play.tailwindcss.com/)

---

Example using our other example:

```html

<body class="bg-gray-100 font-sans">
    <header class="bg-green-500 text-white text-center p-4">
        <h1 class="text-2xl">My Flask App</h1>
    </header>
    <nav class="flex justify-between bg-gray-800 p-2">
        <a href="#" class="text-white px-4 py-2">Home</a>
        <a href="#" class="text-white px-4 py-2">About</a>
        <a href="#" class="text-white px-4 py-2">Services</a>
        <a href="#" class="text-white px-4 py-2">Contact</a>
    </nav>
    <main class="p-8">
        <h2 class="text-xl mb-4">Welcome to My Flask App</h2>
        <p>This is a simple Flask app with inline CSS.</p>
    </main>
    <footer class="text-center p-4 bg-green-500 text-white">
        <p>Copyright © 2023 My Flask App</p>
    </footer>
</body>


```
---

Example with adding video:

```html

<div class="p-8">
    <div class="overflow-hidden rounded-lg bg-black">
    <video controls class="h-full w-full">
        <source src="https://samplelib.com/lib/preview/mp4/sample-5s.mp4" type="video/mp4" />
        Your browser does not support the video tag.
    </video>
    </div>
</div>

```

---

# Resources

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Tailwind CSS GitHub Repository](https://github.com/tailwindlabs/tailwindcss)
- [Tailwind CSS Community](https://tailwindcss.com/community)

