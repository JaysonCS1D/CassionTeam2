# Deployment Plan

## Project: Python Task Manager App

---

## 1. Deployment Strategy

**Selected Strategy:** Continuous Deployment to Render.com (free tier)

Every push to the main branch triggers the GitHub Actions CI/CD pipeline,
which automatically runs tests and deploys to Render.com if all tests pass.

---

## 2. Prerequisites

- Python 3.10+
- Git repository on GitHub
- Account on Render.com
- requirements.txt in project root

---

## 3. Deployment Steps

### Step 1 — Push to GitHub
```bash
git add .
git commit -m "feat: prepare app for deployment v1.0"
git push origin main
```

### Step 2 — GitHub Actions Runs Automatically
- Installs dependencies from requirements.txt
- Runs all 15 unit tests
- Runs smoke test to verify app starts
- Deploys to Render if all steps pass

### Step 3 — Manual Deploy to Render.com (first time only)
1. Go to https://render.com and sign in
2. Click New > Web Service
3. Connect your GitHub repository
4. Set Build Command: pip install -r requirements.txt
5. Set Start Command: python demo.py
6. Click Deploy

### Step 4 — Verify Deployment
- Open the provided Render URL
- Confirm the system is live and functional
- Check logs for any errors

---

## 4. Rollback Steps

If deployment fails or causes critical issues:

1. Go to Render dashboard and select your service
2. Click Rollback to the previous successful deploy
3. OR revert the last commit and push:
```bash
git revert HEAD
git push origin main
```
4. Notify the team immediately
5. Log the incident in docs/defect-log.md

---

## 5. Post-Deployment Checklist

- [ ] App is accessible via public URL
- [ ] All features work as expected
- [ ] No critical errors in deployment logs
- [ ] Team notified of successful deployment
- [ ] URL documented and shared with stakeholders
