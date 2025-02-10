<!-- ---
title: "Introducing Sugo: A Minimal Static Site Generator"
date: "2025-02-10"
author: "Mukul Singh"
description: "Learn how to use Sugo, a simple and fast static site generator for your projects."
--- -->

# **Introducing Sugo: A Minimal Static Site Generator**

Static site generators (SSGs) have gained popularity for their simplicity, speed, and security. Meet **Sugo**, a lightweight and developer-friendly static site generator designed to help you build blazing-fast websites with minimal effort. Whether you're creating a blog, documentation site, or personal portfolio, Sugo makes the process seamless.

## **Why Use Sugo?**
- **Minimal and Fast** – No unnecessary bloat, just what you need.
- **Markdown-Based** – Write content in Markdown and generate beautiful static pages.
- **Easy to Use** – Simple CLI commands to generate and deploy sites.
- **Customizable Themes** – Modify styles and layouts effortlessly.

## **Getting Started**

### **1. Installation**
To install Sugo, simply run:
```sh
pip install sugo  
```


### **2. Creating a New Project**
Once installed, create a new Sugo project:
```sh
sugo init my-site
cd my-site
```
This will set up the basic folder structure for your site.

### **3. Writing Your First Blog Post**
Navigate to the `content/` directory and create a Markdown file:
```sh
mkdir content
nano content/my-first-post.md
```
Inside the file, add:
```md
---
title: "My First Blog Post"
date: "2025-02-10"
author: "Mukul Singh"
---

Welcome to my first post using Sugo! This is a simple static site generator.
```

### **4. Generating the Site**
To generate the static site, run:
```sh
sugo build
```
This will process your Markdown files and generate HTML in the `output/` directory.

### **5. Previewing the Site**
Run the local development server:
```sh
sugo serve
```
Open your browser and go to `http://localhost:8000` to see your site in action!

### **6. Deploying Your Site**
You can deploy the `output/` folder to GitHub Pages, Netlify, Vercel, or any static hosting service.
For example, using GitHub Pages:
```sh
git init
git add .
git commit -m "Deploy my Sugo site"
git push origin main
```

## **Conclusion**
Sugo is a simple yet powerful tool for generating static websites. Whether you're a beginner or an advanced developer, its minimalistic approach makes it easy to use and extend. Try it out today and start building your own static websites effortlessly!

Follow us on our social pages to stay updated!
### [X](https://twitter.com/mukulownsyou)
### [Instagram](https://instagram.com/mukulownsyou)
