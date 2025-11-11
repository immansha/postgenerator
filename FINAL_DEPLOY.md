# ⚡ QUICK DEPLOY TO STREAMLIT CLOUD

Your app is ready! Just 3 steps to go live.

## Step 1: Make Sure Latest Changes Are Pushed

```powershell
cd "C:\Users\imman\Downloads\Post-Generator-main (1)\Post-Generator-main\project-genai-post-generator-main"
git add .
git commit -m "Updated for Streamlit Cloud deployment"
git push origin main
```

---

## Step 2: Deploy on Streamlit Cloud ☁️

1. **Go to**: https://share.streamlit.io
2. **Click**: "New app"
3. **Fill in**:
   - Repository: `Post-Generator-main` (or your repo name)
   - Branch: `main`
   - Main file: `main.py`
4. **Click**: "Deploy"

**⏱️ Wait 2-5 minutes while it builds...**

---

## Step 3: Add Your API Key 🔑

Once deployment is complete:

1. Your app URL will appear (e.g., `https://post-generator-xxxxx.streamlit.app`)
2. Click the **⚙️ Settings** button (top-right)
3. Click **"Secrets"**
4. Paste this exactly:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

5. Click **"Save"**
6. App auto-restarts ✅ **Done!**

---

## Your App is Now Live! 🎉

Test it:
- Select a topic
- Choose length & language  
- Click "Generate"
- See your LinkedIn post!

**Share your app URL**: `https://post-generator-xxxxx.streamlit.app`

---

## Need Help?

- App won't deploy? Make sure repo is PUBLIC
- No API key working? Check Secrets section in Settings
- Other issues? Check app logs at bottom of page

**Questions?** See DEPLOYMENT.md
