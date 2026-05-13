# ✍️ AI Content Generator
### Built with Streamlit + Gemini 2.0 Flash

Generate blogs, emails, and social captions instantly using Google's Gemini AI.

---

## 🚀 Run Locally

```bash
# 1. Install packages
pip install -r requirements.txt

# 2. Add your API key
copy .env.example .env
# Open .env and replace with your actual key from aistudio.google.com

# 3. Run the app
python -m streamlit run app.py
```

---

## ☁️ OPTION 1 — Deploy to Streamlit Community Cloud (FREE, Easiest)

### Step 1 — Push code to GitHub
1. Go to github.com → Sign in → Click "New Repository"
2. Name it `ai-content-generator` → Create repository
3. In VS Code terminal:
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-content-generator.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud
1. Go to 👉 share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository → Branch: main → Main file: app.py
5. Click "Advanced settings" → Add secret:
   - Key: `GEMINI_API_KEY`
   - Value: your actual API key
6. Click "Deploy!" ✅

Your app will be live at:
`https://YOUR_USERNAME-ai-content-generator-app-XXXXX.streamlit.app`

---

## 🐳 OPTION 2 — Deploy to Google Cloud Run

### Prerequisites
- Google Cloud account (free tier available)
- Google Cloud CLI installed: https://cloud.google.com/sdk/docs/install

### Step 1 — Setup Google Cloud
```bash
# Login
gcloud auth login

# Create a new project (or use existing)
gcloud projects create my-content-gen-app
gcloud config set project my-content-gen-app

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Step 2 — Build and Deploy
```bash
# Build and deploy in one command
gcloud run deploy ai-content-generator \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your_actual_key_here
```

### Step 3 — Get your URL
After deployment, Cloud Run gives you a URL like:
`https://ai-content-generator-XXXXX-uc.a.run.app` ✅

---

## 📁 Project Structure
```
ai-content-generator/
├── app.py              ← Main Streamlit app
├── requirements.txt    ← Python dependencies
├── Dockerfile          ← For Cloud Run deployment
├── .env                ← Local API key (never commit this!)
├── .env.example        ← Template for others
├── .gitignore          ← Keeps secrets out of GitHub
└── .streamlit/
    └── secrets.toml    ← Streamlit Cloud secrets template
```

---

## 🔑 Getting Your API Key
1. Go to https://aistudio.google.com
2. Sign in with Google
3. Click "Get API Key" → "Create API Key"
4. Copy the key (starts with AIzaSy...)

---

Built as part of the Google Skill Badge: Develop GenAI Apps with Gemini and Streamlit 🏆
