# Deployment & Hosting Guide

This guide walks through deploying the **Mani Subramanian Executive Portfolio Webpage** across multiple hosting environments.

---

## 🚀 Option 1: GitHub Pages (Recommended)

Because this project is built entirely on vanilla HTML, CSS, and JavaScript, it deploys effortlessly to GitHub Pages with zero build steps.

### Step-by-Step Setup:

1. **Commit and Push Files to GitHub**:
   ```bash
   cd /Users/manisubramanian/Documents/GitHub/Day3_HW
   git init   # If not already part of a git repository
   git add .
   git commit -m "Deploy Mani Subramanian Executive Portfolio"
   git branch -M main
   # Link to your remote GitHub repo:
   git remote add origin https://github.com/spmaniusa-hub/<your-repo-name>.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub (`https://github.com/spmaniusa-hub/<your-repo-name>`).
   - Click on **Settings** > **Pages** (under the "Code and automation" section).
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Under **Branch**, select `main` (or root `/`).
   - Click **Save**.

3. **Live URL**:
   Within 1–2 minutes, your website will be live at:
   ```
   https://spmaniusa-hub.github.io/<your-repo-name>/
   ```

---

## 🌐 Custom Domain Setup (e.g., `manisubramanian.com`)

If you own a custom domain (such as `manisubramanian.com` or `manisubramanian.dev`):

1. **Add Custom Domain in GitHub**:
   - In GitHub repository **Settings** > **Pages**, enter your custom domain under **Custom domain**.
   - Check the **Enforce HTTPS** box.

2. **Configure DNS Records** with your DNS provider (Cloudflare, Namecheap, GoDaddy, etc.):
   
   | Type | Host | Value / Target |
   | :--- | :--- | :--- |
   | `A` | `@` | `185.199.108.153` |
   | `A` | `@` | `185.199.109.153` |
   | `A` | `@` | `185.199.110.153` |
   | `A` | `@` | `185.199.111.153` |
   | `CNAME` | `www` | `spmaniusa-hub.github.io` |

---

## ⚡ Option 2: Cloudflare Pages

Cloudflare Pages provides global edge distribution with fast TTFB (Time to First Byte):

1. Log into your [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Select your repository.
4. Set Build Settings:
   - **Framework preset**: `None`
   - **Build command**: *(leave blank)*
   - **Build output directory**: `/` (or `Day3_HW` if within a monorepo)
5. Click **Save and Deploy**.

---

## 🛠️ Local Testing & Development

You can test the webpage locally on macOS using any of the following methods:

### Method A: Built-in Python Server
```bash
cd /Users/manisubramanian/Documents/GitHub/Day3_HW
python3 -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### Method B: Directly Open in Default Browser
```bash
open /Users/manisubramanian/Documents/GitHub/Day3_HW/index.html
```

### Method C: Node.js `npx serve`
```bash
npx serve /Users/manisubramanian/Documents/GitHub/Day3_HW
```

---

## 🔍 Pre-Launch Quality Checklist

- [x] All anchor links (`#about`, `#experience`, `#leadership`, etc.) scroll smoothly.
- [x] LinkedIn URL (`https://www.linkedin.com/in/manisubramanian/`) is functional.
- [x] UC Irvine Advisory profile link is accurate.
- [x] Dark / Light theme toggle persists across page refreshes.
- [x] Interactive skill category filtering functions cleanly.
- [x] Contact form validation checks email format and required fields.
- [x] Live Pacific Time clock displays accurate San Francisco Bay Area time.
