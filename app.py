import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Content Generator", page_icon="✍️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }
.output-box {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border: 1px solid #e2b96f44; border-radius: 12px;
    padding: 24px; margin-top: 16px; color: #f0f0f0;
    line-height: 1.8; white-space: pre-wrap;
}
.badge {
    display: inline-block; background: #e2b96f22; color: #e2b96f;
    border: 1px solid #e2b96f55; border-radius: 20px;
    padding: 2px 12px; font-size: 12px; margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password", help="Get free $5 credits at platform.openai.com")
    if not api_key:
        st.sidebar.warning("Enter your OpenAI API key to get started")
        st.sidebar.markdown("👉 [Get free API key](https://platform.openai.com/signup)")
        st.stop()

client = OpenAI(api_key=api_key)

def generate(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content

st.markdown('<p class="badge">✨ Powered by OpenAI GPT</p>', unsafe_allow_html=True)
st.title("AI Content Generator")
st.caption("Create blogs, emails, and social captions instantly with AI")
st.divider()

tab1, tab2, tab3 = st.tabs(["📝 Blog Post", "📧 Email", "📱 Social Caption"])

with tab1:
    st.subheader("Blog Post Generator")
    col1, col2 = st.columns(2)
    with col1:
        blog_topic = st.text_input("Topic", placeholder="e.g. Benefits of morning exercise")
        blog_tone = st.selectbox("Tone", ["Professional", "Conversational", "Inspirational", "Educational", "Humorous"])
    with col2:
        blog_length = st.selectbox("Length", ["Short (300 words)", "Medium (600 words)", "Long (1000 words)"])
        blog_audience = st.text_input("Target Audience", placeholder="e.g. Fitness beginners")
    blog_keywords = st.text_input("SEO Keywords (optional)", placeholder="e.g. morning routine, health")
    if st.button("✍️ Generate Blog Post", type="primary", use_container_width=True):
        if not blog_topic:
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Writing your blog post..."):
                prompt = f"""Write a {blog_length} blog post about: {blog_topic}
Tone: {blog_tone}
Target audience: {blog_audience if blog_audience else 'general readers'}
{f'Include these SEO keywords naturally: {blog_keywords}' if blog_keywords else ''}
Structure: engaging title, compelling intro, 3-4 sections with subheadings, conclusion with CTA."""
                result = generate(prompt)
                st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download", result, file_name="blog_post.txt", use_container_width=True)

with tab2:
    st.subheader("Email Generator")
    col1, col2 = st.columns(2)
    with col1:
        email_type = st.selectbox("Email Type", ["Cold Outreach", "Follow Up", "Thank You", "Apology", "Job Application", "Newsletter", "Product Launch", "Meeting Request"])
        email_tone = st.selectbox("Tone", ["Formal", "Friendly", "Persuasive", "Concise"])
    with col2:
        sender_name = st.text_input("Your Name / Company", placeholder="e.g. John / TechCorp")
        recipient = st.text_input("Recipient Role", placeholder="e.g. Marketing Manager")
    email_context = st.text_area("What is the email about?", placeholder="e.g. Following up after our meeting about partnership", height=100)
    if st.button("📧 Generate Email", type="primary", use_container_width=True):
        if not email_context:
            st.warning("Please describe what the email is about!")
        else:
            with st.spinner("Drafting your email..."):
                prompt = f"""Write a {email_type} email.
Context: {email_context}
Sender: {sender_name if sender_name else 'the sender'}
Recipient: {recipient if recipient else 'the recipient'}
Tone: {email_tone}
Include subject line (prefix Subject:), greeting, body, sign-off."""
                result = generate(prompt)
                st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download", result, file_name="email.txt", use_container_width=True)

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
                prompt = f"""Generate {num_variations} different {platform} captions for:
Topic: {caption_topic}
Tone: {caption_tone}
{'Include relevant hashtags' if include_hashtags else 'No hashtags'}
{'Use emojis' if include_emoji else 'No emojis'}
Separate each variation with ---"""
                result = generate(prompt)
                st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
                st.download_button("⬇️ Download", result, file_name="captions.txt", use_container_width=True)

st.divider()
st.caption("Built with Streamlit + OpenAI GPT · Your First Gen AI App 🚀")
