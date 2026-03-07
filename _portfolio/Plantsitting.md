---
title: "PlantBuddy – Full-Stack Mobile Application  (Personal Engineering Project)"
collection: portfolio
category: software
permalink: /software/plantbuddy/
excerpt: "Full-stack Android application with REST API backend and PostgreSQL database for managing plant sitting, exchanges and sales."
---

A collaborative software engineering project focused on designing a full-stack application for connecting plant owners, plant sitters and plant stores through a unified platform.
This project reflects ongoing development of production-oriented system design skills beyond academic research contexts. 

The system enables users to request plant care, exchange plants with other enthusiasts, donate plants or purchase plants from approved stores.

The project was developed as a portfolio project to explore mobile application development, backend architecture and relational database design.

The system follows a **three-tier architecture** consisting of:

• Android mobile application  
• REST API backend  
• PostgreSQL relational database  

The mobile client communicates with the backend through RESTful APIs, while the backend handles authentication, business logic and database operations. :contentReference[oaicite:0]{index=0}

---

## Key Features

The platform supports multiple user roles:

• plant owners  
• plant sitters  
• plant store owners  

Users can create and interact with several types of plant listings including:

• plant sitting requests  
• plant donations  
• plant swaps  
• plant sales  

Each plant listing can lead to structured agreements between users, including plant sitting contracts that define responsibilities, timeframes and payments.

---

## System Architecture

The backend is built using a layered architecture:

Client → REST API → Service Layer → Repository Layer → Database

This design separates application logic, API endpoints and database access, improving maintainability and scalability. :contentReference[oaicite:1]{index=1}

---

## Technology Stack

Mobile

• Android  
• Java  
• MVVM architecture  
• Retrofit networking  

Backend

• Java Servlets  
• Maven  
• JWT authentication  
• REST API endpoints  

Database

• PostgreSQL  
• relational schema design  
• trigger-based business rules  

---

## What This Project Demonstrates

This project demonstrates several engineering skills:

• REST API design  
• relational database modelling  
• backend authentication and security  
• mobile client architecture  
• full-stack system design

---

## Repository

GitHub repository:

github.com/Alieyeh/plantbuddy

Tags: Java · Android · RESTful API · ER diagram · SQL · Servlet · UML diagram · Maven · PostgreSQL
