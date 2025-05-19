# ✅ Task Board App (Flask + Tailwind CSS)

A **Trello-like task board** built using:

- 🐍 Flask (Python) for the backend API
- 🌐 HTML + JavaScript for the frontend
- 🎨 Tailwind CSS for styling
- 🗃 JSON file-based task storage

This project allows users to **create**, **edit**, **delete**, and **drag-and-drop** tasks across three columns — just like Trello.

---

## 📁 Project Structure
 ```
task-board/
│
├── backend/
│   ├── app.py               # Flask API
│   └── tasks.json           # Task data (auto-created)
│
├── frontend/
│   ├── index.html           # Frontend UI
│   ├── src/
│   │   └── input.css        # Tailwind source file
│   ├── dist/
│   │   └── output.css       # Compiled Tailwind CSS
│   ├── tailwind.config.js   # Tailwind config
│   └── postcss.config.js    # PostCSS config
│
├── package.json             # Node.js config
├── package-lock.json
├── .gitignore
└── README.md
```
---

## 🔧 Setup Instructions

### ⚙️ Backend Setup (Flask)

#### Step 1: Navigate to `backend` directory

```bash
cd backend
pip install flask flask-cors
python app.py
The Flask API will run on:
📡 http://localhost:5000



## 🎨 Frontend Setup (Tailwind CSS)
Step 1: Go to project root
bash
Copy
Edit
cd ..


Step 2: Initialize npm
bash
Copy
Edit
npm init -y


Step 3: Install Tailwind + PostCSS
bash
Copy
Edit
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p


Step 4: Configure Tailwind
In tailwind.config.js:

js
Copy
Edit
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
In frontend/src/input.css:

css
Copy
Edit
@tailwind base;
@tailwind components;
@tailwind utilities;
Step 5: Add build script to package.json
json
Copy
Edit
"scripts": {
  "build:css": "npx tailwindcss -i ./frontend/src/input.css -o ./frontend/dist/output.css --watch"
}
Step 6: Start Tailwind compiler
bash
Copy
Edit
npm run build:css
This generates frontend/dist/output.css used by your HTML.

🚀 Usage
Start Flask Backend
Go to backend/ and run:

bash
Copy
Edit
python app.py
Start Tailwind Watcher
In root:

bash
Copy
Edit
npm run build:css
Open Frontend
Simply open frontend/index.html in your browser.


🔁 Features
✅ Create tasks with title and description

📝 Edit existing tasks

🗑 Delete tasks

🧲 Drag-and-drop between "To Do", "In Progress", and "Done"

💾 Tasks are saved persistently in tasks.json

⚡ Fast and responsive with Tailwind



🔒 API Endpoints (Flask)
Method	Endpoint	Description
GET	/tasks	Get all tasks
POST	/tasks	Add a new task
PUT	/tasks/<id>	Update a task by ID
DELETE	/tasks/<id>	Delete a task by ID

All tasks are stored in backend/tasks.json

📦 Dependencies
Python
flask

flask-cors

Node
tailwindcss

postcss

autoprefixer



