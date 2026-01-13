# Pre-AWS Shutdown Checklist

Before shutting down your AWS EC2 instance and Route 53, verify everything works on Vercel.

## ✅ Critical Tests

### 1. **Domain & DNS**
- [ ] Your domain `jackspoetic.com` is connected in Vercel dashboard
- [ ] DNS records are pointing to Vercel (check in Route 53 or your DNS provider)
- [ ] Visit `https://jackspoetic.com` - does it load correctly?
- [ ] Visit `https://www.jackspoetic.com` - does it redirect/load correctly?
- [ ] SSL certificate is active (green lock in browser)

### 2. **All Pages Load**
- [ ] Homepage (`/`) loads correctly
- [ ] Blog listing page (`/blog`) loads correctly
- [ ] Test at least 3-5 individual blog posts (`/blog/<slug>`) load correctly
- [ ] 404 page works (try `/blog/nonexistent`)

### 3. **Images & Static Files**
- [ ] Homepage hero image displays
- [ ] All images in blog posts display correctly
- [ ] CSS styles load (check dark mode works)
- [ ] JavaScript works (theme toggle button functions)
- [ ] Test images from different folders:
  - [ ] `/static/images/general/` (homepage)
  - [ ] `/static/images/disfrutar/` (blog post images)
  - [ ] `/static/images/neural_networks/` (neural network post)
  - [ ] `/static/images/perceptron/` (perceptron post)
  - [ ] `/static/images/vectors/` (vectors post)

### 4. **Functionality**
- [ ] Dark mode toggle works on all pages
- [ ] Navigation links work (Home, Blog)
- [ ] Blog posts are sorted correctly (newest first)
- [ ] Post metadata displays (date, author, excerpt)
- [ ] Markdown rendering works (code blocks, links, formatting)

### 5. **Performance**
- [ ] Pages load quickly (< 3 seconds)
- [ ] No console errors (check browser DevTools)
- [ ] No 404 errors in Vercel function logs
- [ ] Check Vercel dashboard → Functions → Logs for any errors

### 6. **Mobile/Responsive**
- [ ] Site looks good on mobile
- [ ] Navigation works on mobile
- [ ] Images scale properly on mobile

## 🔍 Testing Commands

### Test Direct Image URLs:
```
https://jackspoetic.com/static/images/general/25746811-2bfe-4d0f-a502-6c55257bac97.JPG
https://jackspoetic.com/static/images/neural_networks/neural.png
https://jackspoetic.com/static/images/perceptron/perceptron.jpg
```

### Test Blog Posts:
```
https://jackspoetic.com/blog
https://jackspoetic.com/blog/neural_network
https://jackspoetic.com/blog/perceptron
https://jackspoetic.com/blog/llms
```

## 📋 Before Shutting Down AWS

### 1. **Wait for DNS Propagation** (if you just changed DNS)
- DNS changes can take 24-48 hours to fully propagate
- Use `dig jackspoetic.com` or `nslookup jackspoetic.com` to verify DNS points to Vercel
- Test from multiple locations/devices

### 2. **Keep EC2 as Backup** (Recommended)
- Don't terminate immediately - **stop** the instance first
- Keep it stopped for 1-2 weeks as backup
- Only **terminate** after you're 100% confident everything works
- This gives you a safety net if something goes wrong

### 3. **Save Important Info**
- [ ] Note your EC2 instance ID (in case you need to reference it)
- [ ] Save any custom nginx configs (you already have `jackspoetic.com.conf`)
- [ ] Document any environment variables or secrets (if any)

## 🚨 If Something Goes Wrong

### Rollback Plan:
1. **Start your EC2 instance** (if you only stopped it)
2. **Update DNS** back to EC2 IP (if you changed it)
3. **Wait for DNS propagation**
4. **Debug the Vercel issue** while site is still on AWS

## ✅ Final Steps (After Everything Works)

1. **Stop EC2 instance** (don't terminate yet)
2. **Wait 1-2 weeks** to ensure everything is stable
3. **Terminate EC2 instance** (only after you're confident)
4. **Cancel Route 53** (if you're not using it for anything else)
   - Note: You might want to keep Route 53 if you're using it for DNS management
   - Vercel can handle DNS, but Route 53 is fine too

## 💰 Cost Savings Confirmation

After shutdown, you should see:
- **EC2**: $0/month (was ~$10-11/month)
- **Route 53**: $0.50/month (if you keep it) or $0 (if you cancel)
- **Vercel**: $0/month (free tier)

**Total savings: ~$12-13/month**

## 📝 Notes

- Vercel automatically handles SSL certificates
- Vercel provides global CDN (faster than single EC2 instance)
- Auto-deployments from GitHub mean easier updates
- No server maintenance needed!

---

**When you're ready to shut down:**
1. Complete all checkboxes above
2. Test for at least 24-48 hours
3. Stop (don't terminate) EC2 instance
4. Wait 1-2 weeks
5. Terminate EC2 if everything is stable

