# Streamlit Cloud Deployment Guide

## Prerequisites
1. **GitHub Account**: You need a GitHub account
2. **Streamlit Account**: Sign up at https://streamlit.io/cloud (free tier available)
3. **Repository**: Your project must be pushed to a public GitHub repository

---

## Step 1: Prepare Your GitHub Repository

If your project is NOT yet on GitHub, follow these steps:

### 1a. Initialize Git (if not already done)
```powershell
cd "C:\Users\imman\Downloads\Post-Generator-main (1)\Post-Generator-main\project-genai-post-generator-main"
git init
git add .
git commit -m "Initial commit: LinkedIn Post Generator"
```

### 1b. Create a GitHub Repository
- Go to https://github.com/new
- Create a new repository (e.g., `linkedin-post-generator`)
- Make it **PUBLIC** (required for free Streamlit Cloud)
- Copy the repository URL

### 1c. Push to GitHub
```powershell
git remote add origin https://github.com/YOUR_USERNAME/linkedin-post-generator.git
git branch -M main
git push -u origin main
```

---

## Step 2: Add Secrets to Streamlit Cloud

1. Go to https://share.streamlit.io and sign in with your GitHub account
2. Create a **New app**
3. Fill in:
   - **Repository**: YOUR_USERNAME/linkedin-post-generator
   - **Branch**: main
   - **Main file path**: main.py
4. Click **Deploy**

### During Deployment: Add Secrets
1. After clicking Deploy, go to your app's **Settings** (gear icon, top-right)
2. Click **Secrets**
3. Paste your secrets in the **Secrets** tab:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## Step 3: Verify Your Code Reads Secrets Correctly

Make sure your code uses `st.secrets` to access the API key. Check `llm_helper.py`:

```python
import streamlit as st
import os
from langchain_groq import ChatGroq

# Get API key from secrets
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Use the API key
llm = ChatGroq(
    temperature=0.9,
    groq_api_key=api_key,
    model_name="mixtral-8x7b-32768"
)
```

---

## Step 4: Monitor Your Deployment

1. After deployment, you'll get a **Public URL**: `https://your-app-name-XXXXXX.streamlit.app`
2. Check the **Logs** tab to debug any issues
3. Your app will auto-redeploy when you push changes to GitHub

---

## Troubleshooting

### Issue: "No module named 'streamlit'"
**Solution**: Ensure `streamlit==1.51.0` is in `requirements.txt`

### Issue: "FileNotFoundError: data/processed_posts.json"
**Solution**: Ensure the `data/` directory is committed to GitHub with the JSON files

### Issue: "GROQ_API_KEY not found"
**Solution**: 
1. Check Streamlit Cloud **Settings → Secrets**
2. Ensure your code uses `st.secrets.get("GROQ_API_KEY")`

### Issue: App won't start
**Solution**: Check **Logs** at the bottom of your app page

---

## Quick Reference

### Your App URL (after deployment)
```
https://your-app-name-XXXXXX.streamlit.app
```

### Key Files Needed on GitHub
- `main.py` ✅
- `requirements.txt` ✅
- `few_shot.py` ✅
- `llm_helper.py` ✅
- `post_generator.py` ✅
- `preprocess.py` ✅
- `data/processed_posts.json` ✅
- `.streamlit/secrets.toml` ❌ (Do NOT commit—add in Streamlit Cloud)

---

## Next Steps

1. **Push to GitHub** (if not already done)
2. **Go to** https://share.streamlit.io
3. **Sign in** with GitHub
4. **Deploy** and add secrets in Streamlit Cloud settings
5. **Share** your public app URL!

For more help: https://docs.streamlit.io/deploy/streamlit-cloud
