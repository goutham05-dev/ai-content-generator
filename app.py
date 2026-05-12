import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}
.main { background-color: #0f0f0f; }
.stTextArea textarea {
    background-color: #1a1a1a;
    color: #f0f0f0;
    border: 1px solid #333;
    border-radius: 8px;
}
.stSelectbox > div > div {
    background-color: #1a1a1a;
    color: #f0f0f0;
}
.output-box {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border: 1px solid #e2b96f44;
    border-radius: 12px;
    padding: 24px;
    margin-top: 16px;
    color: #f0f0f0;
    line-height: 1.8;
    white-space: pre-wrap;
}
.badge {
    display: inline-block;
    background: #e2b96f22;
    color: #e2b96f;
    border: 1px solid #e2b96f55;
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 12px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ── API Key setup ─────────────────────────────────────────────────────────────
api_key = os.getenv("AIzaSyCpTXJJVUJoIpREw2eDGCdCNTt4aJCCe5I")
if not api_key:
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password", help="Get it from aistudio.google.com")
    if not api_key:
        st.sidebar.warning("Enter your API key to get started")
        st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="badge">✨ Powered by Gemini 2.0</p>', unsafe_allow_html=True)
st.title("AI Content Generator")
st.caption("Create blogs, emails, and social captions instantly with Gemini AI")

st.divider()

# ── Content type tabs ─────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📝 Blog Post", "📧 Email", "📱 Social Caption"])

# ════════════════════════════════════════════════════════
# TAB 1 — BLOG POST
# ════════════════════════════════════════════════════════
with tab1:
    st.subheader("Blog Post Generator")
    col1, col2 = st.columns(2)
    with col1:
        blog_topic = st.text_input("Topic", placeholder="e.g. Benefits of morning exercise")
        blog_tone = st.selectbox("Tone", ["Professional", "Conversational", "Inspirational", "Educational", "Humorous"])
    with col2:
        blog_length = st.selectbox("Length", ["Short (300 words)", "Medium (600 words)", "Long (1000 words)"])
        blog_audience = st.text_input("Target Audience", placeholder="e.g. Fitness beginners")

    blog_keywords = st.text_input("SEO Keywords (optional)", placeholder="e.g. morning routine, health, productivity")

    if st.button("✍️ Generate Blog Post", type="primary", use_container_width=True):
        if not blog_topic:
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Writing your blog post..."):
                prompt = f"""Write a {blog_length} blog post about: {blog_topic}
                
Tone: {blog_tone}
Target audience: {blog_audience if blog_audience else 'general readers'}
{f'Include these SEO keywords naturally: {blog_keywords}' if blog_keywords else ''}

Structure it with:
- An engaging title
- A compelling introduction
- 3-4 main sections with subheadings
- A conclusion with a call to action

Write in a {blog_tone.lower()} tone. Make it engaging and valuable."""

                response = model.generate_content(prompt)
                st.markdown(f'<div class="output-box">{response.text}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download Blog Post", response.text, file_name="blog_post.txt", use_container_width=True)

# ════════════════════════════════════════════════════════
# TAB 2 — EMAIL
# ════════════════════════════════════════════════════════
with tab2:
    st.subheader("Email Generator")
    col1, col2 = st.columns(2)
    with col1:
        email_type = st.selectbox("Email Type", [
            "Cold Outreach", "Follow Up", "Thank You", 
            "Apology", "Job Application", "Newsletter",
            "Product Launch", "Meeting Request"
        ])
        email_tone = st.selectbox("Tone", ["Formal", "Friendly", "Persuasive", "Concise"])
    with col2:
        sender_name = st.text_input("Your Name / Company", placeholder="e.g. John / TechCorp")
        recipient = st.text_input("Recipient Role", placeholder="e.g. Marketing Manager")

    email_context = st.text_area("What is the email about?", placeholder="e.g. I want to follow up after our meeting last week about the new product partnership", height=100)

    if st.button("📧 Generate Email", type="primary", use_container_width=True):
        if not email_context:
            st.warning("Please describe what the email is about!")
        else:
            with st.spinner("Drafting your email..."):
                prompt = f"""Write a professional {email_type} email.

Context: {email_context}
Sender: {sender_name if sender_name else 'the sender'}
Recipient: {recipient if recipient else 'the recipient'}
Tone: {email_tone}

Include:
- A clear subject line (prefix with "Subject: ")
- Professional greeting
- Clear and concise body
- Appropriate sign-off

Keep it {email_tone.lower()} and to the point."""

                response = model.generate_content(prompt)
                st.markdown(f'<div class="output-box">{response.text}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download Email", response.text, file_name="email.txt", use_container_width=True)

# ════════════════════════════════════════════════════════
# TAB 3 — SOCIAL CAPTION
# ════════════════════════════════════════════════════════
with tab3:
    st.subheader("Social Media Caption Generator")
    col1, col2 = st.columns(2)
    with col1:
        platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter/X", "Facebook", "YouTube"])
        caption_tone = st.selectbox("Tone", ["Engaging", "Professional", "Funny", "Inspirational", "Promotional"])
    with col2:
        include_hashtags = st.toggle("Include Hashtags", value=True)
        include_emoji = st.toggle("Include Emojis", value=True)

    caption_topic = st.text_area("What is your post about?", placeholder="e.g. Launching my new online course about digital marketing", height=100)
    num_variations = st.slider("Number of variations", 1, 3, 2)

    if st.button("📱 Generate Captions", type="primary", use_container_width=True):
        if not caption_topic:
            st.warning("Please describe your post!")
        else:
            with st.spinner("Creating your captions..."):
                prompt = f"""Generate {num_variations} different {platform} caption(s) for this post:

Topic: {caption_topic}
Tone: {caption_tone}
Platform: {platform}
{'Include relevant hashtags' if include_hashtags else 'Do NOT include hashtags'}
{'Use emojis where appropriate' if include_emoji else 'Do NOT use emojis'}

For each variation:
- Write the caption optimized for {platform}
- Keep character limits in mind (Twitter: 280 chars, Instagram: engaging but not too long)
- Separate each variation with "---"

Make each variation distinctly different in style."""

                response = model.generate_content(prompt)
                st.markdown(f'<div class="output-box">{response.text}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download Captions", response.text, file_name="captions.txt", use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit + Gemini 2.0 Flash · Your First Gen AI App 🚀")