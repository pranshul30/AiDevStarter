#🤖 AI-Dev Starter (Backend Engine)
This repository contains the core backend engine for the AI-Dev Starter, an intelligent project scaffolding tool. It uses a Large Language Model (Gemini 1.5 Flash) to automatically determine the necessary dependencies for a new Python project, sets up a virtual environment, and installs everything for you, all through a simple command-line interface.

This backend is fully functional as a standalone terminal application and is designed to be the foundation for a future web-based version.

#✨ Core Features
AI-Powered Dependency Analysis: Simply describe your project in plain English (e.g., "a web scraper with BeautifulSoup"), and the AI will figure out the required packages.

Automated Project Scaffolding: Automatically creates a project directory, a Python virtual environment, and installs the dependencies for you.

Secure by Design: Implements a crucial user confirmation step before any files are created or packages are installed on your local machine.

Modular and Clean Code: The logic is separated into distinct modules for AI, scaffolding, and the main application, making it easy to understand and extend.

#🚀 How It Works

The engine operates via a simple, powerful workflow:

Describe: The user runs the script and is prompted for a project name and a natural language description.

Reason: The description is sent to the Gemini API. The model analyzes the request and returns a structured JSON list of the essential starter packages.

Build: The scaffolding module receives the package list and, after user confirmation, runs the necessary shell commands to create the project folder, set up the venv, install the packages, and generate the requirements.txt file.

🛠️ Getting Started
Follow these steps to get the terminal application running on your local machine.

Prerequisites
Python 3.9+

A Google Gemini API Key

1. Clone the Repository
git clone [https://github.com/your-username/ai-dev-starter.git](https://github.com/your-username/ai-dev-starter.git)
cd ai-dev-starter

2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
Install all the required packages for the project itself.

pip install google-generativeai

4. Set Up Your API Key
Set your Google Gemini API key as an environment variable. This is the most secure way to handle your key.

# For macOS/Linux
export GOOGLE_API_KEY='YOUR_API_KEY_HERE'

# For Windows (PowerShell)
$env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"

5. Run the Application
You're all set! Run the main script to start the scaffolding process.

python main.py

The application will then guide you through the process of naming and describing your new project.

🌐 Future Development: Building a Web App
This terminal application serves as the robust backend for a planned web interface. The current architecture is designed to be easily wrapped by a web framework like FastAPI or Flask.

The future web application will:

Provide a user-friendly web form for project input.

Call this backend engine to generate the project on the server.

Package the generated project folder into a .zip file.

Allow the user to download the final, ready-to-use project directly from their browser.

🤝 Contributing
Contributions are welcome! If you have ideas for improving the backend, optimizing the AI prompts, or are interested in helping build the web frontend, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add some amazing feature').

Push to the branch (git push origin feature/your-feature-name).e

Open a Pull Request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
