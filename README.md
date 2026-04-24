# 🏋️ AI Gym & Fitness Assistant

## 📌 Overview

The **AI Gym & Fitness Assistant** is a full-stack intelligent fitness system that integrates Computer Vision, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to provide personalized workout guidance, diet planning, habit tracking, and performance analytics.

---

## 🚀 Key Features

### 🎯 1. AI Gym Trainer

* Real-time pose detection using MediaPipe
* Tracks exercise posture and counts repetitions
* Provides visual and textual feedback
* Generates personalized workout suggestions

---

### 🥗 2. AI Dietician

* Calculates BMI and daily calorie requirements
* Generates personalized diet plans
* Uses RAG + Gemini API for intelligent recommendations
* Provides structured meal suggestions and guidelines

---

### 🤖 3. Virtual Gym Buddy

* AI chatbot for fitness-related queries
* Uses RAG + LLM for contextual responses
* Provides motivation and workout advice

---

### 📊 4. Habit Tracker

* Tracks daily habits (done/missed)
* Computes consistency percentage
* Predicts behavioral trends
* Provides AI-based feedback

---

### 📈 5. Admin Dashboard (Analytics)

* Displays consistency metrics
* Visualizes performance using charts
* Shows recent activity logs
* Provides system status overview

---

## 🧠 Technologies Used

### Frontend

* React.js
* Chart.js

### Backend

* Flask (Python)
* REST APIs

### AI/ML

* MediaPipe (Pose Detection)
* LangChain (RAG pipeline)
* FAISS (Vector Database)
* Sentence Transformers (Embeddings)
* Gemini API (LLM)

### Database

* MongoDB

---

## ⚙️ System Architecture

Frontend (React)
↓
Backend (Flask APIs)
↓
AI Modules (RAG + LLM + CV)
↓
MongoDB Database

---

## 🔍 Retrieval-Augmented Generation (RAG) Pipeline

The system uses a **RAG-based approach** to generate accurate and context-aware responses.

### 📌 Step-by-Step Workflow

1. **Data Source**

   * Fitness-related PDFs are stored in the `rag_data/` folder.

2. **Chunking**

   * Documents are split into smaller chunks using a text splitter for better retrieval.

3. **Embeddings**

   * Each chunk is converted into vector representations using **Sentence Transformers**.

4. **Vector Storage**

   * These embeddings are stored in a **FAISS vector database**.

5. **User Query**

   * When a user asks a question (diet/chat), the query is converted into an embedding.

6. **Similarity Search**

   * FAISS retrieves the most relevant document chunks based on semantic similarity.

7. **Context Formation**

   * Retrieved chunks are combined to form a meaningful context.

8. **LLM Integration**

   * The context is passed to the **Gemini API (LLM)**.

9. **Final Response**

   * The LLM generates a structured, human-like response using the retrieved context.

---

### 🎯 Key Advantage of RAG

* Reduces hallucination
* Provides domain-specific answers
* Ensures responses are based on real fitness data

---

## 📂 Project Structure

ai-gym-assistant/
│
├── backend/
│   ├── routes/
│   ├── services/
│   ├── rag_data/
│   ├── vector_store/
│   └── app.py
│
├── frontend/
│   ├── src/pages/
│   └── components/
│
├── README.md
└── requirements.txt

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

cd backend
pip install -r requirements.txt
python app.py

---

### 🔹 Frontend Setup

cd frontend
npm install
npm run dev

---

## ▶️ Usage

1. Open the frontend application
2. Navigate between modules:

   * AI Trainer
   * Diet Planner
   * Gym Buddy
   * Habit Tracker
   * Analytics Dashboard
3. Interact with each module to get AI-powered insights

---

## 📊 Output

* Real-time workout feedback
* Personalized diet plans
* AI chatbot responses
* Habit consistency analysis
* Visual analytics dashboard

---

## ⚠️ Deployment Note

* The **AI Trainer (pose detection)** module requires webcam access and runs locally
* Other modules (Diet, Chat, Habit, Analytics) can be deployed on cloud platforms

---

## 🎯 Objective

To build an intelligent, integrated fitness assistant that improves:

* Physical health
* Habit consistency
* Personalized decision-making using AI

---

## 💡 Future Improvements

* Multi-user authentication system
* Cloud-based model optimization
* Real-time progress tracking
* Mobile application integration

---

## 👩‍💻 Author

**Hrishika R**
B.E. Information Science & Engineering

---

## 📌 Conclusion

This project demonstrates the integration of:

* Artificial Intelligence (LLMs)
* Computer Vision
* Retrieval-Augmented Generation (RAG)
* Full-stack development
* Data analytics

into a unified and practical fitness assistant system.
