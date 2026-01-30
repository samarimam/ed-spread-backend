# 🚀 EdSpread – AI-Powered Course Recommendation Platform

**EdSpread** is a full-stack EdTech platform where admins can upload and manage courses, users can enroll using referral IDs, and an **AI-powered chatbot** recommends the most relevant courses using **semantic search over vector embeddings**.

This project is designed to showcase **modern full-stack engineering**, **AI integration (vector search)**, and **real-world product thinking**, making it ideal for recruiters reviewing practical GenAI projects.

---

## 🌐 Live Demo

🔗 **Frontend (Netlify):** [https://edspread.netlify.app/](https://edspread.netlify.app/)

> Backend APIs are hosted on **Render**.

---

## ✨ Key Highlights

### 🤖 AI-Powered Course Recommendation

* Courses are stored as **vector embeddings in MongoDB**
* User queries are converted into embeddings
* **Semantic similarity search** recommends the most relevant courses
* Works even when keywords don’t exactly match (true meaning-based search)

Example:

> Searching for *"cooking"* may recommend a *Python course* if the course description emphasizes *"hands-on practical learning"* and *"step-by-step mastery"*

This demonstrates **real-world semantic retrieval**, not simple keyword matching.

---

## 🧠 AI Chatbot Capabilities

* Conversational chatbot to assist users
* Suggests courses based on intent, interests, and queries
* Uses **vector search + LLM reasoning**
* Integrated directly into the platform UI

---

## 🏗️ System Architecture

```
Frontend (React + Netlify)
        |
        v
Backend (Node.js + Express – Render)
        |
        v
MongoDB Atlas
  ├── Course Metadata
  └── Vector Embeddings (Semantic Search)
```

---

## 👨‍💼 Admin Features

* Secure admin dashboard
* Add / update / delete courses
* View enrolled users per course
* Track course popularity
* Monitor referral-based signups

---

## 👤 User Features

* Browse available courses
* Enroll in courses
* Unique **referral ID** assigned to each user
* Use referral ID during signup
* Chat with AI assistant for personalized course suggestions

---

## 🔗 Referral System

* Every user gets a unique referral ID
* New users can sign up using an existing referral ID
* Referral mapping stored in the database
* Designed to be extensible for reward systems (points, discounts, etc.)

---

## 🧰 Tech Stack

### Frontend

* React.js
* CSS / Tailwind (if applicable)
* Hosted on **Netlify**

### Backend

* Node.js
* Express.js
* Hosted on **Render**

### Database & AI

* MongoDB Atlas
* MongoDB Vector Search
* Embedding generation for semantic retrieval
* LLM-powered chatbot

---

## 🧪 AI & Vector Search Flow

1. Admin uploads a course
2. Course description → converted into vector embedding
3. Embedding stored in MongoDB
4. User enters a query
5. Query converted into embedding
6. Vector similarity search retrieves best-matching courses
7. AI chatbot explains and recommends courses

---

## 📌 Why This Project Matters

✔ Demonstrates **GenAI + Full-Stack Integration**
✔ Uses **real vector databases**, not mock AI
✔ Shows **production-ready architecture**
✔ Solves a **real business problem** (course discovery)
✔ Resume-ready project with live demo

---

## 🚀 Future Improvements

* Authentication & role-based access control
* Payment gateway integration
* Referral reward system
* User learning progress tracking
* Advanced chatbot memory per user

---

## 📄 License

This project is for educational and portfolio purposes.

---

## 👋 Author

**Samar Imam**
GenAI | Full-Stack Developer | AI Enthusiast

> If you’re a recruiter: this project highlights **AI-driven search, scalable backend design, and real-world product thinking**.

---

⭐ If you like this project, consider giving it a star!
