# Vercel Image Troubleshooting Guide

If images aren't loading on Vercel, here are steps to diagnose and fix:

## Quick Checks

1. **Verify static folder is included**: Make sure `static/` folder is in your Git repository and gets deployed
2. **Check file paths**: All image paths should start with `/static/` (absolute paths)
3. **Verify file extensions**: Make sure image file extensions match exactly (case-sensitive on some systems)

## Common Issues

### Issue: Images return 404

**Possible causes:**
- Static files not included in deployment
- Path case sensitivity (Linux vs Windows)
- File extensions don't match

**Solution:**
1. Check Vercel build logs to see if static files are being uploaded
2. Verify file paths in your markdown/posts match exactly
3. Check that images exist in the `static/images/` directory structure

### Issue: Images load slowly or timeout

**Possible causes:**
- Large image files
- Cold start on serverless function

**Solution:**
1. Optimize images (compress/resize)
2. Consider using Vercel's Image Optimization API
3. Use WebP format for better compression

## Testing Locally

To test if paths work correctly:

```bash
# Run Flask locally
python3 app.py

# Test a static file URL
curl http://localhost:5000/static/images/general/25746811-2bfe-4d0f-a502-6c55257bac97.JPG
```

## Debugging on Vercel

1. **Check Function Logs**: 
   - Go to Vercel Dashboard → Your Project → Functions
   - Check logs for any errors when accessing `/static/` routes

2. **Test Direct URLs**:
   - Try accessing an image directly: `https://your-project.vercel.app/static/images/general/25746811-2bfe-4d0f-a502-6c55257bac97.JPG`
   - If this works, the issue is with how images are referenced in HTML/markdown

3. **Check File Structure**:
   - Verify `static/images/` exists in your repo
   - Check that all subdirectories (general, disfrutar, etc.) are included

## File Path Checklist

- ✅ All paths start with `/static/` (absolute)
- ✅ File extensions match exactly (.JPG vs .jpg)
- ✅ Directory names match exactly (case-sensitive)
- ✅ Files are committed to Git
- ✅ Files are not in `.vercelignore`

## If Still Not Working

1. Check Vercel deployment logs for errors
2. Verify the `static/` folder structure matches your local setup
3. Try accessing a simple test image first
4. Check browser console for 404 errors on specific image paths

