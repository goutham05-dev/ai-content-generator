# ✍️ AI Content Generator

A full-stack Gen AI web app that generates blogs, emails, and social media captions instantly — built with Streamlit and powered by Groq's free LLaMA 3.3 API.

🌍 **Live App:** [ai-content-generator-goutham05-dev.streamlit.app](https://ai-content-generator-goutham05-dev.streamlit.app)

---

## ✨ Features

- 📝 **Blog Post Generator** — Choose topic, tone, length, audience, and SEO keywords
- 📧 **Email Generator** — Cold outreach, follow-ups, job applications, and more
- 📱 **Social Caption Generator** — Instagram, LinkedIn, Twitter/X, Facebook, YouTube

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web app framework |
| Groq API | Free AI inference |
| LLaMA 3.3 70B | Language model |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/goutham05-dev/ai-content-generator.git
cd ai-content-generator
```

**2. Install packages**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```
Get a free key at 👉 [console.groq.com](https://console.groq.com) — no credit card needed!

**4. Run the app**
```bash
streamlit run app.py
```

Open 👉 `http://localhost:8501`

---

## ☁️ Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add secret in Settings:
```toml
GROQ_API_KEY = "your_key_here"
```
5. Click Deploy ✅

---

## 📁 Project Structure

```
ai-content-generator/
├── app.py              ← Main Streamlit app
├── requirements.txt    ← Python dependencies
├── Dockerfile          ← For Google Cloud Run deployment
├── .env                ← Local API key (never commit!)
├── .gitignore          ← Keeps secrets out of GitHub
└── README.md           ← You are here
```

---

## 🔄 Local Development Workflow

```bash
# Make changes to app.py
# Test locally
streamlit run app.py

# Push to GitHub (auto-deploys to Streamlit Cloud)
git add .
git commit -m "your change description"
git push
```

---

## 🏆 Built By

**Goutham** — Completed the Google Skill Badge: *Develop GenAI Apps with Gemini and Streamlit*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/goutham05-dev)