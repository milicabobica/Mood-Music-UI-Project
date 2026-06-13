# Mood Music UI 

AI-powered mood-based playlist generation application built with modern UI technologies and integrated with the Hugging Face Inference API.

Designed as a lightweight AI-assisted recommendation system that generates personalized playlists based on the user’s emotional state, focus mode, or coding vibe.

---

## Overview

Mood Music UI is an AI-powered application that transforms natural language mood descriptions into curated playlist recommendations.

Users can describe how they feel or the atmosphere they want, and the application generates music suggestions using a Hugging Face AI model.

The project was created to explore:
- AI API integration
- Prompt engineering
- User-focused AI experiences
- Async frontend communication
- Recommendation workflows
- Modern UI development

### Example Prompts
- “sadness”
- “calm”
- “energetic”
- “happy”

---

# Features

- Mood-based playlist generation
- Hugging Face AI model integration
- Natural language mood input
- Fast asynchronous API requests
- Modern responsive UI
- Dynamic recommendation generation
- AI-powered contextual interpretation
- Developer focus mode concept
- Error handling for failed requests
- API key protection using environment variables

---

# How AI Is Used

The application uses the Hugging Face Inference API to:
1. Interpret the user’s mood or vibe input
2. Generate contextual playlist recommendations
3. Match emotional tone and energy level
4. Return music suggestions formatted for the UI

The project focuses on practical AI integration rather than training custom machine learning models.

### AI Workflow

```text
User Input
     ↓
Mood Processing Layer
     ↓
Prompt Builder
     ↓
Hugging Face API Client
     ↓
AI Response Parser
     ↓
Playlist Formatter
     ↓
Results UI
```

---

# Technical Decisions

## Hugging Face API
The Hugging Face Inference API was chosen because it provides lightweight and flexible access to AI models without requiring local model hosting.

## Modular Structure
The application logic is separated into:
- UI components
- API handling
- Prompt generation
- Response formatting

This keeps the project maintainable and scalable.

## Async Communication
Asynchronous requests improve responsiveness and create a smoother user experience while waiting for AI-generated results.

## Environment Variables
API keys are stored using environment variables to avoid exposing sensitive information in the repository.

## Recommendation-Oriented Design
The application was designed as an AI-assisted recommendation system rather than a static music application.

---

# Tech Stack

- Frontend Framework: React
- Styling: CSS
- AI Integration: Hugging Face Inference API
- Version Control: Git + GitHub

---

# Project Structure

```text
Mood-Music-UI-Project/
│
├── backend/
│   ├── node_modules/
│   ├── index.py
│   ├── package-lock.json
│   └── package.json
│
├── frontend/
│   ├── images/
│   ├── index.html
│   ├── index.js
│   ├── package-lock.json
│   ├── package.json
│   └── style.css
│
├── .gitignore
└── README.md
```

## Structure Overview

### backend/
Contains the backend logic responsible for:
- AI API communication
- Request handling
- Playlist generation logic
- Response formatting

### frontend/
Contains the frontend application and UI logic:
- User mood input
- Playlist display
- Responsive interface
- Frontend interaction handling

### node_modules/
Automatically generated project dependencies managed through npm.

### index.py
Main application entry point for backend/frontend logic.

### package.json
Contains project metadata, dependencies, and scripts.

### package-lock.json
Locks dependency versions for consistent installations.

### .gitignore
Specifies files and folders ignored by Git.

### README.md
Project documentation and setup instructions.

---

# Setup & Installation

## Clone the repository

```bash
git clone https://github.com/milicabobica/Mood-Music-UI-Project.git
```

## Navigate to the project folder

```bash
cd Mood-Music-UI-Project
```

## Install dependencies

```bash
npm install
```

## Create a `.env` file

```env
VITE_HUGGINGFACE_API_KEY=your_api_key_here
```

## Run the development server

```bash
npm run dev
```

---

# Example Workflow

1. User enters a mood or vibe
2. Application builds a contextual AI prompt
3. Prompt is sent to the Hugging Face API
4. AI generates playlist suggestions
5. Results are formatted and displayed in the UI

---

# Challenges

Some challenges during development included:
- Structuring prompts for more consistent recommendations
- Managing asynchronous API responses
- Handling invalid or empty user input
- Designing a clean and responsive UI
- Formatting AI-generated responses into readable playlist suggestions

---

# Future Improvements

Potential future improvements include:
- IntelliJ Plugin version
- Spotify API integration
- Playlist export functionality
- Playlist history and favorites
- Mood classification system
- Streaming AI responses
- AI-generated playlist descriptions
- Developer productivity focus modes
- Caching previously generated results
- Theme customization

---
# Why This Project

This project was created to explore how AI can enhance user-focused experiences through recommendation systems and natural language interaction.

The goal was not to build a production-ready music platform, but to demonstrate:
- practical AI tool usage
- clean project structure
- API integration
- thoughtful engineering decisions
- and user-centered design

---

# Repository

Repository Link:
https://github.com/milicabobica/Mood-Music-UI-Project
