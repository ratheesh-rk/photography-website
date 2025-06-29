# 🚀 SD Photography Website Deployment Guide

## Quick Deployment Options

### Option 1: Railway (Recommended - Easiest)
**Perfect for client demos and feedback**

1. **Sign up at [Railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Deploy automatically**

**Steps:**
```bash
# 1. Push your code to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Go to Railway.app and:
# - Connect your GitHub account
# - Select your repository
# - Railway will auto-detect Django and deploy
```

**Environment Variables to set in Railway:**
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-app-name.railway.app
```

### Option 2: Render (Great Alternative)

1. **Sign up at [Render.com](https://render.com)**
2. **Create a new Web Service**
3. **Connect your GitHub repository**

**Build Command:**
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command:**
```bash
gunicorn sd_project.wsgi:application
```

### Option 3: Heroku (Popular Choice)

1. **Install Heroku CLI**
2. **Create Heroku app**

```bash
# Install Heroku CLI first
heroku create your-photography-app
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

## Pre-Deployment Checklist

### ✅ 1. Run these commands locally first:
```bash
# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Test locally
python manage.py runserver
```

### ✅ 2. Check your files are ready:
- ✅ `requirements.txt` - All dependencies listed
- ✅ `Procfile` - Web server configuration
- ✅ `runtime.txt` - Python version specified
- ✅ `sd_project/settings.py` - Production-ready settings

### ✅ 3. Database setup:
```bash
# If you have data, make sure migrations are ready
python manage.py makemigrations
python manage.py migrate
```

## Environment Variables

Set these in your hosting platform:

```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-domain.com,your-app-name.railway.app
```

## After Deployment

### 1. Create Superuser (if needed):
```bash
# For Railway/Render (use their shell)
python manage.py createsuperuser
```

### 2. Add your content:
- Upload photos through Django admin
- Add couples to portfolio
- Add testimonials

### 3. Test everything:
- ✅ Home page loads
- ✅ Portfolio page works
- ✅ About page displays
- ✅ Contact form functions
- ✅ Images display properly

## Client Feedback Process

### 1. Send the live URL to your client
**Example:** `https://your-app-name.railway.app`

### 2. Ask for specific feedback:
- Design and layout
- Photo quality and presentation
- Navigation and user experience
- Loading speed
- Mobile responsiveness

### 3. Make updates based on feedback:
```bash
# Make changes locally
# Test everything
git add .
git commit -m "Client feedback updates"
git push origin main
# Automatic redeployment on Railway/Render
```

## Troubleshooting

### Common Issues:

**1. Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**2. Database errors:**
```bash
python manage.py migrate
```

**3. Images not displaying:**
- Check MEDIA_URL and MEDIA_ROOT settings
- Ensure images are uploaded to the correct location

**4. 500 errors:**
- Check DEBUG=False in production
- Review server logs in your hosting platform

## Performance Tips

### 1. Image Optimization:
- Compress images before uploading
- Use appropriate formats (JPEG for photos, PNG for graphics)
- Consider using WebP format for better compression

### 2. Caching:
- Enable browser caching for static files
- Consider CDN for images

### 3. Database:
- For production, consider PostgreSQL instead of SQLite

## Security Checklist

- ✅ DEBUG=False in production
- ✅ SECRET_KEY is set and secure
- ✅ ALLOWED_HOSTS is configured
- ✅ HTTPS is enabled (automatic on most platforms)
- ✅ Static files are served securely

## Support

If you encounter issues:
1. Check the hosting platform's logs
2. Test locally first
3. Review Django deployment documentation
4. Contact the hosting platform's support

---

**🎉 Your photography website is now live and ready for client feedback!** 