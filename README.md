# 🧠 BrainGraph AI

**BrainGraph AI** is an advanced AI-powered study assistant that converts your handwritten or printed study notes into an interactive learning system. Using **Gemini Vision API** and Python, BrainGraph extracts key concepts and turns them into **knowledge graphs, quizzes, flashcards, voice explanations, and structured study plans** to make learning fast, smart, and engaging.

---

## 🔥 Features

### 1. Image Upload
- Upload images of your study notes (handwritten or printed)
- AI reads and extracts content automatically

### 2. AI Vision Analysis
- Uses **Gemini Vision API** to analyze the uploaded notes
- Extracts main topics, subtopics, and relationships

### 3. BrainGraph Knowledge Graph
- Converts extracted concepts into an interactive graph
- Visualizes main topics and subtopics using **NetworkX** and **PyVis**
- Helps students **see connections between concepts**

### 4. AI Quiz Generator
- Generates **5 multiple-choice questions** from the notes
- Each question includes 4 options, correct answer, and short explanation
- Helps reinforce learning through practice

### 5. AI Flashcards
- Generates digital flashcards automatically
- Front: Question or concept  
- Back: Explanation or definition
- Easy for quick revision

### 6. Voice Explanation
- Converts AI-generated explanations into speech using **gTTS**
- Play audio directly in the app for auditory learning

### 7. Study Planner
- Creates a **4-day structured study plan**
  - Day 1: Concept overview  
  - Day 2: Subtopics  
  - Day 3: Quiz practice  
  - Day 4: Revision

### 8. Clean Hackathon UI
- Sections clearly separated: Upload → BrainGraph → Quiz → Flashcards → Voice → Study Plan
- Designed for **fast, interactive learning**

---

## 💻 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Gemini Vision API  
- **Libraries:** streamlit, google-generativeai, pillow, requests, networkx, pyvis, gtts  

---

## 🚀 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/braingraph-ai.git
cd braingraph-ai
