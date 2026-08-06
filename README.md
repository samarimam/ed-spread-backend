# 🚀 EdSpread – AI-Powered Course Recommendation Platform

**EdSpread** is a full-stack AI-powered EdTech platform that helps users discover relevant courses through an intelligent recommendation system. The platform enables admins to manage courses, users to enroll using referral IDs, and learners to get personalized course recommendations using **semantic search, vector embeddings, machine learning re-ranking, and LLM-generated explanations**.

The project demonstrates practical implementation of **Generative AI applications, vector databases, recommendation systems, and scalable full-stack architecture**.

---

# 🌐 Live Demo

🔗 **Frontend:** https://edspread.netlify.app/

> Backend APIs are deployed on Render.

---

# ✨ Key Features

## 🤖 AI Course Recommendation System

EdSpread implements a multi-stage recommendation pipeline combining **semantic retrieval, machine learning ranking, and LLM reasoning**.

### 1. Semantic Search & Vector Retrieval

- Course information is converted into high-dimensional vector embeddings using an embedding model.
- User queries are transformed into embeddings at runtime.
- **MongoDB Atlas Vector Search** retrieves semantically relevant courses based on similarity rather than keyword matching.

### 2. ML-Based Re-ranking

Retrieved courses are passed through a **Random Forest recommendation model** that improves ranking quality.

The model uses features such as:

| Feature          | Description                            |
| ---------------- | -------------------------------------- |
| Similarity Score | Semantic similarity from vector search |
| Course Price     | Pricing information                    |
| Course Type      | Free or Paid                           |
| Query Length     | Number of words in user query          |
| Title Length     | Course title size                      |

The model generates a recommendation probability score to rank candidate courses.

Example:

```
Course: Node.js Backend Development

Vector Similarity Score: 0.91

ML Recommendation Score: 0.96
```

### 3. LLM-Powered Explanations

The highest-ranked courses are sent to an LLM that generates personalized explanations based on the user's learning objective.

Example:

**User Query:**

> "I want to learn backend development"

**Pipeline:**

User Intent → Vector Retrieval → ML Ranking → LLM Explanation → Personalized Recommendation

---

# 🧠 AI Chatbot

The EdSpread chatbot acts as an intelligent course discovery assistant.

Capabilities:

- Understands natural language user goals
- Performs semantic course discovery
- Provides personalized recommendations
- Explains why a course matches the user's requirements

Powered by:

- Vector embeddings
- MongoDB Atlas Vector Search
- Random Forest ranking model
- Groq LLM API

---

# 🏗️ System Architecture

```
                 React Frontend
                     |
                     |
              Node.js + Express
                     |
        -----------------------------
        |                           |
        v                           v

 MongoDB Atlas              ML Recommendation API
 Course Data                Flask + Random Forest
 Embeddings                       |
        |                          |
        |                          |
        -----------+--------------
                   |
                   v
              Groq LLM Layer
                   |
                   v
       Personalized Recommendations
```

---

# 🔍 Recommendation Workflow

```
User Query
    |
    v
Generate Query Embedding
    |
    v
MongoDB Atlas Vector Search
    |
    v
Retrieve Similar Courses
    |
    v
Random Forest Re-ranking
    |
    v
Select Top Courses
    |
    v
LLM Generates Explanation
    |
    v
Final Recommendation
```

---

# 👨‍💼 Admin Dashboard

Features:

- Secure admin authentication
- Add, update, and delete courses
- Automatically generate course embeddings
- Manage course metadata
- Track enrolled users
- Monitor referral-based registrations

---

# 👤 User Features

- Browse available courses
- Enroll in courses
- Generate unique referral IDs
- Register through referral links
- Receive AI-powered course recommendations

---

# 🔗 Referral System

Implemented a referral management system where:

- Each user receives a unique referral ID
- New users can join using referral codes
- Referral relationships are stored in MongoDB
- Architecture supports future reward and incentive systems

---

# 🧰 Tech Stack

## Frontend

- React.js
- Tailwind CSS
- Netlify

## Backend

- Node.js
- Express.js
- REST APIs
- Render

## Database

- MongoDB Atlas
- MongoDB Atlas Vector Search

## AI / Machine Learning

- Hugging Face Embedding Models
- Vector Embeddings
- Semantic Search
- Random Forest Recommendation Model
- Scikit-learn
- Groq LLM API
- AI Chatbot

## ML Service

- Python
- Flask API
- Joblib

---

# 🧪 AI Pipeline

## Course Ingestion

```
Admin Uploads Course
        |
        v
Generate Embedding
        |
        v
Store Metadata + Vector
        |
        v
MongoDB Vector Index
```

## Recommendation Pipeline

```
User Input
        |
        v
Generate Query Vector
        |
        v
Vector Similarity Search
        |
        v
ML Ranking Model
        |
        v
LLM Explanation
        |
        v
Personalized Courses
```

---

# 📌 Project Impact

✔ Built an end-to-end AI recommendation system combining **LLMs, vector search, and machine learning**

✔ Implemented production-style **retrieval + re-ranking architecture**

✔ Used vector databases for semantic search instead of traditional keyword matching

✔ Integrated classical ML models with modern Generative AI workflows

✔ Demonstrates experience building scalable AI-powered full-stack applications

---

# 🚀 Future Enhancements

- Train ranking models using real user interaction data
- Add collaborative filtering recommendations
- Implement course ratings and reviews
- Add user learning history
- Integrate payment workflows
- Add chatbot memory
- Containerize ML services and deploy on cloud infrastructure

---

# 👋 Author

**Samar Imam**

GenAI Engineer | Full-Stack Developer | AI Enthusiast

This project showcases practical experience building AI applications using **vector databases, LLMs, machine learning models, and modern backend architectures**.

⭐ If you find this project useful, consider giving it a star.
