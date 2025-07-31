<h1 align="center">storyforge-ai</h1>

An interactive web application that allows users to generate imaginative and personalized stories using OpenAI’s GPT models. Built with Python, FastAPI, and Streamlit, this beginner-friendly project is designed to teach real-world development skills while making storytelling fun and intuitive.


## 🚀 Project Features
 - **⚙️ Backend with Python & FastAPI**<br>
    Learn to build scalable APIs using FastAPI.

 - **🤖 GPT-Powered Story Generation**<br>
Use OpenAI’s models to generate unique, creative narratives.

 - **🌐 Interactive Frontend with Streamlit**<br>
    Build a simple, modern interface for story input and output.

 - **☁️ Cloud Deployment on AWS EC2**<br>
    Deploy your application live and accessible to the world.

 - **🧩 Environment & Dependency Management**<br>
    Follow best practices using requirements.txt and virtual environments.


## 📚 What You'll Learn
 - Full-stack development using Python tools and frameworks.

 - How to integrate AI into real-world web applications.

 - End-to-end deployment and best practices.

 - Using cloud platforms like AWS EC2 to host applications.

 - Fundamentals of API development and UI design.



## 🎯 Who This Project is For
 - 💡 Beginners in Python looking for a hands-on project.

 - 🧑‍💻 Aspiring developers eager to build AI-powered apps.

 - 🌍 Anyone passionate about creative writing or interactive tools.

 - 🚀 Learners wanting to understand deployment and production-ready practices.


## 🛠️ Tech Stack
| Technology |  	Purpose                        |
|------------|----------------------------------|
| Python     |	Core programming language        |
| FastAPI    |	Backend API framework            |
| OpenAI     | GPT	AI model for story generation|
| Streamlit  |	Web interface for interaction    |
| AWS EC2    |	Cloud deployment platform        |


## 🧱 Project Structure
```bash
Copy
Edit
creative-story-generator/
│
├── app/                      # FastAPI backend
│   └── main.py               # Main application logic
│
├── streamlit_app/            # Frontend (Streamlit)
│   └── app.py                # UI for story generation
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .env                      # API keys and environment variables
```

## 🚀 Getting Started
### 1. Clone the Repository
```bash
Copy
Edit
git clone https://github.com/your-username/creative-story-generator.git
cd creative-story-generator
```
### 2. Create Virtual Environment & Install Dependencies
```bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


### 3. Set Up Environment Variables
Create a .env file and add your OpenAI API key:

```bash
Copy
Edit
OPENAI_API_KEY=your_api_key_here
```
### 4. Run Backend
```bash
Copy
Edit
cd app
uvicorn main:app --reload
```
### 5. Run Streamlit Frontend
```bash
Copy
Edit
cd streamlit_app
streamlit run app.py
```

## 🌍 Deployment (AWS EC2)
1. Launch an EC2 instance.

2. SSH into your server and clone the repository.

3. Install Python, Pip, and dependencies.

4. Set up .env file with your API key.

5. Run both FastAPI and Streamlit with screen/tmux or a process manager.


🤝 Contributing
Contributions are welcome!
Feel free to fork the repo and submit a pull request.

<h3 align="center">Happy Coding!</h3>
