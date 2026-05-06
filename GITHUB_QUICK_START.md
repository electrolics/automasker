# Push to GitHub - Quick Start (2 Minutes)

## 🚀 The Easiest Way

### Step 1: Create GitHub Repository
1. Go to: https://github.com/new
2. Repository name: `automasker`
3. Description: `YOLO masking pipeline for equirectangular images`
4. Public (recommended)
5. **Don't** initialize with README/gitignore
6. Click "Create repository"

### Step 2: Run Push Script
```bash
Double-click: push_to_github.bat
```

**You'll be prompted for GitHub credentials:**
- **Username:** your GitHub username
- **Password:** Use Personal Access Token (not your password!)
  - Get token: https://github.com/settings/tokens
  - Generate new token → Select "repo" → Copy token

### Step 3: Verify
Go to: https://github.com/electrolics/automasker

You should see all your files!

---

## ⚠️ Important: Personal Access Token (PAT)

**Don't use your GitHub password!**

### Get a Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Name it: `Automasker Push`
4. Select "repo" scope
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again)
7. Use as password when push script asks

---

## 🎯 Complete Steps

```
1. Create repository at https://github.com/new
2. Double-click: push_to_github.bat
3. Enter GitHub username
4. Paste Personal Access Token (as password)
5. Wait for completion
6. Verify at https://github.com/electrolics/automasker
```

---

## ✅ What Gets Pushed

✅ All source code (`App/`, `Setup/`, etc.)
✅ All documentation (`Guides/`, `README.md`)
✅ All launchers and scripts
✅ Models (warning: large files ~70MB)
⚠️ Build artifacts (in `Build/` folder)

---

## 📊 File Count
- **Total files:** ~29
- **Total size:** ~70MB (mostly model files)
- **Documentation:** 10+ guides

---

## 🆘 If Something Goes Wrong

### "Repository not found"
- Make sure you created it at https://github.com/new
- Check username is correct

### "Authentication failed"
- Use Personal Access Token, not password
- Get new token: https://github.com/settings/tokens

### "remote origin already exists"
- Repository was already pushed
- Just check: https://github.com/electrolics/automasker

---

## 📁 Repository Structure on GitHub

After pushing, you'll have:
```
electrolics/automasker/
├── App/
├── Setup/
├── Guides/
├── Models/
├── Launchers/
├── Build/
├── README.md
├── INDEX.md
├── GITHUB_PUSH.md
└── (all other files)
```

---

## 🎉 Next Steps

After successfully pushing:

1. **Check if files are there:** https://github.com/electrolics/automasker
2. **Add a GitHub badge to README** (optional)
3. **Create releases** for versions (optional)
4. **Enable GitHub Pages** for documentation (optional)

---

## 📚 Helpful Links

- **GitHub Docs:** https://docs.github.com
- **Personal Access Token:** https://github.com/settings/tokens
- **Create Repository:** https://github.com/new
- **Your Repository:** https://github.com/electrolics/automasker

---

## ✨ That's It!

**Just run the script and follow prompts!**

```bash
Double-click: push_to_github.bat
```

**Happy pushing! 🚀**
