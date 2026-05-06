# Push to GitHub - Step by Step

## Prerequisites
- GitHub account (create at https://github.com if needed)
- Repository created: https://github.com/electrolics/automasker
- Git installed on your computer

## Option 1: Using GitHub Desktop (Easiest) ⭐

### Step 1: Download GitHub Desktop
- Go to: https://desktop.github.com/
- Install and open

### Step 2: Clone Your Repository
1. Click "File" → "Clone Repository"
2. Select "GitHub.com"
3. Find "electrolics/automasker"
4. Click "Clone" (choose a location)

### Step 3: Copy Files
1. Copy all files from your Automasker folder
2. Paste into the cloned repository folder
3. Replace all files when prompted

### Step 4: Push to GitHub
1. GitHub Desktop will show "Changes"
2. Bottom left, write commit message:
   ```
   Initial commit: YOLO masking pipeline for equirectangular images
   ```
3. Click "Commit to main"
4. Click "Push origin"

**Done!** Your code is now on GitHub.

---

## Option 2: Using Command Line (Advanced)

### Step 1: Configure Git
```bash
git config --global user.name "Electrolics"
git config --global user.email "electrolics@gmail.com"
```

### Step 2: Navigate to Your Folder
```bash
cd C:\Users\elect\Downloads\Automasker\Automasker
```

### Step 3: Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: YOLO masking pipeline for equirectangular images"
```

### Step 4: Add Remote Repository
```bash
git branch -M main
git remote add origin https://github.com/electrolics/automasker.git
```

### Step 5: Push to GitHub
```bash
git push -u origin main
```

**When prompted for password:**
- Don't use your GitHub password!
- Use a Personal Access Token:
  1. Go to: https://github.com/settings/tokens
  2. Click "Generate new token"
  3. Select "repo" scope
  4. Copy the token
  5. Paste as password

---

## Option 3: Using GitHub CLI (Modern)

### Step 1: Install GitHub CLI
- Download: https://cli.github.com/
- Install and restart Command Prompt

### Step 2: Authenticate
```bash
gh auth login
```

### Step 3: Navigate and Push
```bash
cd C:\Users\elect\Downloads\Automasker\Automasker
git init
git add .
git commit -m "Initial commit: YOLO masking pipeline"
git branch -M main
git remote add origin https://github.com/electrolics/automasker.git
git push -u origin main
```

---

## 📝 GitHub Repository Setup

Before pushing, make sure your repository is set up:

1. **Go to:** https://github.com/new
2. **Fill in:**
   - Repository name: `automasker`
   - Description: `YOLO masking pipeline for equirectangular images in photogrammetry and Gaussian splatting`
   - Public or Private: Public (recommended for open source)
   - Initialize: Leave unchecked (we'll push our files)
3. **Click "Create repository"**

---

## ✅ After Pushing

### Verify on GitHub
1. Go to: https://github.com/electrolics/automasker
2. You should see all your files and folders
3. Check the folder structure:
   - App/
   - Setup/
   - Guides/
   - Models/
   - Launchers/
   - Build/
   - README.md
   - etc.

### Create a .gitignore (Optional but Recommended)

Create file: `C:\Users\elect\Downloads\Automasker\Automasker\.gitignore`

Add this content:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# PyInstaller
build/
dist/
*.egg-info/
.eggs/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Cache
.cache/
*.cache

# Models (optional - these are large)
*.pt
```

Then commit and push:
```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

## 🚀 Recommended Workflow After Push

1. **Add README badge** to your GitHub repository
2. **Create releases** when you have stable versions
3. **Enable GitHub Actions** for CI/CD (optional)
4. **Add issues template** for bug reports
5. **Add contributing guide** if accepting contributions

---

## 🆘 Troubleshooting

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/electrolics/automasker.git
```

### "Permission denied (publickey)"
You need SSH keys or HTTPS authentication:
```bash
# Use HTTPS instead:
git remote set-url origin https://github.com/electrolics/automasker.git
```

### "fatal: could not read password: No data available"
Use Personal Access Token instead of password (see Step 5 above)

### "fatal: The current branch main does not have any commits yet"
```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 📚 Next Steps

After pushing to GitHub:

1. **Add GitHub Actions** for automated testing
2. **Enable GitHub Pages** to host documentation
3. **Create releases** for version tags
4. **Add contributing guide** (CONTRIBUTING.md)
5. **Monitor issues** and pull requests

---

## 💡 Pro Tips

1. **Use meaningful commit messages** - Helps track changes
2. **Create branches** for new features:
   ```bash
   git checkout -b feature/gpu-optimization
   ```
3. **Create releases** for stable versions:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
4. **Keep .gitignore updated** - Don't commit large model files

---

## ✨ You're Ready!

Choose Option 1 (easiest) or Option 2/3 (if comfortable with command line).

**Need help?** Check GitHub's official guides:
- https://docs.github.com/en/get-started
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

---

**Happy pushing! 🚀**
