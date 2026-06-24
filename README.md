# Wajha (AI-Powered Scholarship Matching Platform)

Wajha is an AI-powered portal specifically designed for Palestinian students and graduates to discover verified grant listings, receive AI-generated match explanations, simplify eligibility text, and track applications from start to finish.

## 🛠️ Tech Stack
*   **Backend:** Django (Python 3)
*   **Database:** MySQL (SQLite for local development)
*   **Frontend:** HTML5, CSS3, Bootstrap 5, AJAX (Fetch API)
*   **Task Scheduling:** Celery / Celery Beat (or cron)
*   **Web Scraping:** BeautifulSoup4 / Scrapy
*   **AI Integration:** Anthropic Claude API (Anthropic Python SDK)

---

## 📂 Project Structure
To keep development structured and clean, the code is separated into 5 dedicated Django apps inside the single project repository:

```
team-project/
│
├── wajha/                        # Main Django Project folder
│   ├── wajha/                    # Settings, general routing
│   ├── accounts/                 # User auth, registration, student profile
│   ├── grants/                   # Scholarship database, search, and admin CRUD
│   ├── applications/             # Saved lists, application stages, deadlines
│   ├── scrapers/                 # Web scraper settings, Celery beats, review queue
│   └── ai_engine/                # Claude API endpoints, prompts, and match score engines
│
├── requirements.txt              # Shared Python dependencies
├── .env.example                  # Environment configuration template
└── README.md                     # This file!
```

---

## ⚙️ Initial Local Setup

Follow these steps to run the project locally on your machine:

### 1. Clone and Navigate
Clone this repository to your machine, then open your terminal inside the root directory:
```bash
cd team-project
```

### 2. Set Up Virtual Environment
Create and activate your Python virtual environment:
```bash
# On Windows:
python -m venv wajha_env
wajha_env\Scripts\activate

# On Mac/Linux:
python3 -m venv wajha_env
source wajha_env/bin/activate
```

### 3. Install Dependencies
Install all package requirements:
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
1. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open the new `.env` file and verify the variables. For local SQLite development, you can use:
   ```env
   DEBUG=True
   SECRET_KEY=your-django-secret-key
   DB_ENGINE=sqlite
   DB_NAME=db.sqlite3
   ```

### 5. Run Database Migrations
Generate and run migrations to create database tables:
```bash
cd wajha
python manage.py migrate
```

### 6. Create Superuser (Admin)
Create an admin account to manage scholarship listings:
```bash
python manage.py createsuperuser
```

### 7. Run the Server
Launch the development server:
```bash
python manage.py runserver
```
Visit the local site at `http://127.0.0.1:8000/`.

---

## 🤝 Git Contribution Workflow
1. Pull the latest updates: `git pull origin main`
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add feature explanation"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request (PR)** on GitHub for review!
