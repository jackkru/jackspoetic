# Vercel Deployment Guide

This guide will help you deploy your Flask blog to Vercel and migrate from AWS.

## Prerequisites

1. A Vercel account (sign up at https://vercel.com - it's free)
2. Your domain `jackspoetic.com` (you'll migrate DNS from Route 53)
3. Git repository (Vercel deploys from Git)

## Step 1: Push to Git

If you haven't already, initialize a git repository and push your code:

```bash
git init
git add .
git commit -m "Prepare for Vercel deployment"
git remote add origin <your-git-repo-url>
git push -u origin main
```

## Step 2: Deploy to Vercel

### Option A: Via Vercel Dashboard (Recommended)

1. Go to https://vercel.com and sign in
2. Click "Add New Project"
3. Import your Git repository
4. Vercel will auto-detect Python/Flask
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (default)
   - **Build Command**: Leave empty (no build needed)
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`
6. Click "Deploy"

### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Follow the prompts
```

## Step 3: Configure Your Domain

1. In Vercel dashboard, go to your project → Settings → Domains
2. Add `jackspoetic.com` and `www.jackspoetic.com`
3. Vercel will show you DNS records to add

## Step 4: Update DNS Records

You need to update your domain's DNS settings:

### If using Route 53:
1. Go to Route 53 → Hosted Zones → jackspoetic.com
2. Update the A record to point to Vercel's IP (Vercel will provide this)
3. Or better: Use CNAME records pointing to Vercel's domain (e.g., `cname.vercel-dns.com`)

### If using another registrar:
1. Update your domain's DNS settings
2. Add the DNS records Vercel provides
3. Remove old AWS/EC2 DNS records

**Vercel will provide specific DNS instructions in the dashboard.**

## Step 5: SSL Certificate

Vercel automatically provisions SSL certificates via Let's Encrypt. No action needed!

## Step 6: Test Your Deployment

1. Visit your Vercel deployment URL (e.g., `your-project.vercel.app`)
2. Test all routes:
   - Home page (`/`)
   - Blog listing (`/blog`)
   - Individual posts (`/blog/<slug>`)
   - Static files (images, CSS, JS)

## Step 7: Clean Up AWS (After Testing)

Once everything works on Vercel:

1. **Stop your EC2 instance** (don't terminate yet - keep as backup for a few days)
2. **Update Route 53 DNS** to point to Vercel
3. **Wait 24-48 hours** for DNS propagation
4. **Test thoroughly** on the new domain
5. **Terminate EC2 instance** if everything works
6. **Cancel Route 53** if you're not using it for anything else

## Cost Comparison

- **AWS (Current)**: ~$12-13/month
  - EC2 instance: ~$10-11/month
  - Route 53: ~$0.50/month
  - Data transfer: ~$1-2/month

- **Vercel (New)**: **FREE** (for your traffic level)
  - Free tier includes:
    - 100GB bandwidth/month
    - 100 hours execution time/month
    - Automatic SSL
    - Global CDN
    - Unlimited deployments

## Troubleshooting

### Static files not loading?
- Check that `static/` folder is in the root directory
- Verify routes in `vercel.json` are correct

### Posts not showing?
- Ensure `posts/` directory is included in deployment
- Check file paths are relative (they should be)

### 404 errors?
- Verify all routes are defined in `app.py`
- Check Vercel function logs in dashboard

### Domain not working?
- Wait for DNS propagation (can take up to 48 hours)
- Check DNS records match Vercel's requirements
- Verify domain is added in Vercel dashboard

## Support

- Vercel Docs: https://vercel.com/docs
- Vercel Python Support: https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python

## Notes

- Vercel uses serverless functions, so there may be a slight cold start (~100-500ms) on first request after inactivity
- Your Flask app will work exactly as before - no code changes needed!
- All your posts, images, and content will be deployed automatically

