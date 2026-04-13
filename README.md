# Intention <img src="./ts/public/logo.webp" alt="Logo" width="27" height="27" />

This is **Team Dhurandar**'s project for **Solution Challenge 2026 - Build with AI** choosing the theme **Smart Resource Allocation**

## Team members
- [@17anirudh](https://github.com/17anirudh)
- [@yashanchan](https://github.com/yashanchan)

## Problem Statement and Objective
- Data-Driven Volunteer Coordination for Social Impact:
    Local social groups and NGOs collect a lot of important information about community needs through paper surveys and field reports. However, this valuable data is often scattered across different places, making it hard to see the biggest problems clearly.

- Objective:
    Design a powerful system that gathers scattered community information to clearly show the most urgent local needs. Build a smart way to quickly match and connect available volunteers with the specific tasks and areas where they are needed most.

## Our Approach (till Prototype)

1. Build a dedicated web application for NGOs and social groups to manage their volunteer coordination
2. Integrate AI-powered data processing to analyze scattered community information from specific document formats (.pdf, .docx, .xlsx, .csv and images)
3. Push the extracted data to RAG and use AI to derive insights and actionable steps

## Full Product (post prototype)
1. Optimize and secure the existing prototype data handling (Data Anonymization)
2. Implement authentication and RBAC
3. Match existing users(NGOs) with similar organizations and volunteers and facilitate collaboration

## Tech stack
- AI & Data:
    - **Gemini**: Primary Cloud LLM used for inference and RAG
    - **gemini-embedding-001**: Matryoshka Representation Learning (MRL) trained google's embedding model
    - SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for database operations
    - Postgresql: Relational database management system for storing application data and vector checkpoints
    - ChromaDB: Vector database for storing and retrieving vector embeddings

- Frontend:
    - Next.js: React Framework with many built-in features, SEO optimization and rendering strategies for production.
    - Tanstack Query: Enterprise grade data fetching and server side state mangement library
    - Shadcn: Tailwind and Base UI components library with huge registry of open source components and providers
    - Tailwind CSS: Utility-first CSS framework for rapid UI development
    - TypeScript: Typed superset of JavaScript for better code quality and developer experience
    - Zod: Schema validation library for runtime type checking
    - React Dropzone: File upload component for drag and drop file uploads

- Backend:
    - FastAPI: Asynchronous Web Framework for building scalable and high-performance APIs
    - Gunicorn: Production-grade WSGI server for serving FastAPI applications with uvicorn parallel workers
    - Langchain: Orchestration framework for building AI applications
    - Pymupdf: PDF processing library for extracting text and images from PDF files
    - Python-docx: Word document processing library for extracting text from .docx files
    - Python-xlrd: Excel file processing library for extracting data from .xlsx files
    - Pandas: Data manipulation and analysis library used only for processing .csv files
    - Pydantic: Data validation and settings management using Python type annotations