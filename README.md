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

<img width="1911" height="913" alt="Screenshot (618)" src="https://github.com/user-attachments/assets/4ce2d13e-31c5-4a6d-9047-22ef0565331a" />
<img width="1877" height="903" alt="Screenshot (617)" src="https://github.com/user-attachments/assets/44914350-d150-47ee-ab03-ca0db979e579" />
<img width="1891" height="918" alt="Screenshot (616)" src="https://github.com/user-attachments/assets/b14d170f-8957-4436-b40b-bf2c904e0bd9" />
<img width="1887" height="862" alt="Screenshot (625)" src="https://github.com/user-attachments/assets/1f6af3d4-1e8d-4ab4-b04c-7cfd134d7461" />
<img width="1901" height="899" alt="Screenshot (624)" src="https://github.com/user-attachments/assets/54a20713-e06e-4139-8196-b08a68a46421" />
<img width="1891" height="841" alt="Screenshot (623)" src="https://github.com/user-attachments/assets/76c813de-dc90-4ad5-bc17-93a0b9bf4017" />
<img width="1889" height="893" alt="Screenshot (622)" src="https://github.com/user-attachments/assets/378e0936-1f52-4f60-ad57-2816e959f75c" />
<img width="1888" height="930" alt="Screenshot (621)" src="https://github.com/user-attachments/assets/5dafa957-cef1-4c57-b815-3f15790165b8" />
<img width="1895" height="919" alt="Screenshot (620)" src="https://github.com/user-attachments/assets/bc65046e-b6cd-47d8-af28-80ab0ff8f501" />
<img width="1873" height="910" alt="Screenshot (619)" src="https://github.com/user-attachments/assets/d6e088fb-1cdc-4cad-9055-1d09f41a1924" />

