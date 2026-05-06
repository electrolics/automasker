@echo off
REM Push Automasker to GitHub
REM This script pushes your code to https://github.com/electrolics/automasker

echo.
echo ========================================
echo PUSH TO GITHUB
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Download from: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo [1/5] Configuring git...
git config --global user.name "Electrolics"
git config --global user.email "electrolics@gmail.com"
echo ✓ Git configured

echo.
echo [2/5] Initializing repository...
if exist .git (
    echo Repository already exists
) else (
    git init
    echo ✓ Repository initialized
)

echo.
echo [3/5] Adding files...
git add .
echo ✓ Files staged

echo.
echo [4/5] Creating commit...
git commit -m "Initial commit: YOLO equirectangular image masker for photogrammetry"
if errorlevel 1 (
    echo Note: Files may already be committed
)

echo.
echo [5/5] Setting up remote and pushing...
git branch -M main

REM Check if remote already exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote: https://github.com/electrolics/automasker.git
    git remote add origin https://github.com/electrolics/automasker.git
) else (
    echo Remote already configured
)

echo.
echo Pushing to GitHub...
echo Note: You may be prompted for GitHub credentials (use Personal Access Token)
echo Get token from: https://github.com/settings/tokens
echo.

git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Push failed
    echo Common issues:
    echo   1. Repository doesn't exist on GitHub
    echo   2. Wrong GitHub credentials
    echo   3. No internet connection
    echo.
    echo Solutions:
    echo   1. Create repo at: https://github.com/new
    echo   2. Use PAT instead of password: https://github.com/settings/tokens
    echo   3. Check internet connection
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS!
echo ========================================
echo.
echo Your code has been pushed to:
echo https://github.com/electrolics/automasker
echo.
echo Next steps:
echo 1. Verify files on GitHub
echo 2. (Optional) Create .gitignore to exclude large files
echo 3. (Optional) Create releases for versions
echo.
pause
