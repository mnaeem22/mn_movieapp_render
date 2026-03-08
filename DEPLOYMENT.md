# Deploy to Render - Movie Recommendation App

## Prerequisites
- Git repository (GitHub, GitLab, or Bitbucket)
- Render account (https://render.com)
- TMDB API Key

## Step-by-Step Deployment Guide

### 1. Prepare Your Code

All necessary files have been created:
- ✅ `Procfile` - Tells Render how to run your app
- ✅ `.gitignore` - Excludes unnecessary files from Git
- ✅ Updated `run.py` - Production-ready configuration
- ✅ Updated `config.py` - Environment variable support

### 2. Initialize Git Repository

If you haven't already:

```bash
# Navigate to your project directory
cd movie_recommendation_app

# Initialize Git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Movie recommendation app ready for Render"
```

### 3. Push to GitHub

Create a new repository on GitHub, then:

```bash
# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/movie-recommendation-app.git

# Push to GitHub
git push -u origin main
```

### 4. Deploy on Render

#### Option A: Direct Deployment

1. **Login to Render** (https://dashboard.render.com)

2. **Click "New +" → "Web Service"**

3. **Connect your repository**
   - Select your GitHub repository
   - Or deploy from Git URL

4. **Configure Web Service**
   - **Name**: `movie-recommendation-app` (or your choice)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python run.py`
   - **Instance Type**: Free tier is fine for testing

5. **Add Environment Variables**
   
   Click "Advanced" and add these environment variables:
   
   ```
   TMDB_API_KEY=5d6ec26ebed1cf94e7a2d233303805f3
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here (optional - auto-generated if not provided)
   ```

6. **Click "Create Web Service"**

#### Option B: Using Render CLI (Alternative)

```bash
# Install Render CLI
npm install -g @render-cloud/cli

# Login
render login

# Create web service
render create web-service --name movie-recommendation-app \
  --region oregon \
  --plan free \
  --branch main \
  --build-command "pip install -r requirements.txt" \
  --start-command "python run.py" \
  --env TMDB_API_KEY=5d6ec26ebed1cf94e7a2d233303805f3 \
  --env FLASK_ENV=production
```

### 5. Monitor Deployment

1. Go to Render Dashboard
2. Click on your service
3. View logs in real-time
4. Wait for deployment to complete (usually 2-5 minutes)

### 6. Access Your App

Once deployed, Render will provide you with a URL like:
```
https://movie-recommendation-app.onrender.com
```

## Environment Variables on Render

Set these in Render Dashboard → Environment:

| Variable | Value | Required |
|----------|-------|----------|
| `TMDB_API_KEY` | Your TMDB API key | Yes |
| `FLASK_ENV` | `production` | Recommended |
| `SECRET_KEY` | Random string | Optional (auto-generated) |

## Troubleshooting

### Common Issues

**1. Build Fails**
- Check `requirements.txt` has all dependencies
- Ensure Python version is compatible
- Review build logs for specific errors

**2. App Won't Start**
- Verify `Procfile` exists and has correct format
- Check `PORT` environment variable is being used
- Review application logs in Render dashboard

**3. API Errors**
- Confirm `TMDB_API_KEY` is set correctly in Render
- Check API key is valid and active
- Verify network connectivity in logs

**4. Static Files Not Loading**
- Ensure Bootstrap CDN links are correct
- Check browser console for errors

## Testing Locally Before Deployment

```bash
# Set production-like environment
export FLASK_ENV=production
export PORT=5000
export TMDB_API_KEY=5d6ec26ebed1cf94e7a2d233303805f3

# Run the app
python run.py
```

## Updating Your App

After making changes:

```bash
# Commit changes
git add .
git commit -m "Description of changes"

# Push to trigger auto-deploy
git push origin main
```

Render will automatically rebuild and deploy your app!

## Pricing

- **Free Tier**: Good for testing and small projects
  - Limited hours per month
  - Auto-sleeps after 15 minutes of inactivity
  
- **Paid Plans**: Starting at $7/month
  - Always-on service
  - More resources
  - Better performance

## Security Best Practices

1. **Never commit `.env` file** to Git (already in `.gitignore`)
2. **Use Render's environment variables** for secrets
3. **Generate a strong `SECRET_KEY`** for production
4. **Keep dependencies updated** regularly

## Additional Resources

- Render Documentation: https://render.com/docs
- Flask Deployment Guide: https://flask.palletsprojects.com/en/2.0.x/deploying/
- TMDB API Docs: https://developers.themoviedb.org/3

## Support

If you encounter issues:
1. Check Render dashboard logs
2. Review this guide
3. Test locally first
4. Check Render community forums

---

**Ready to deploy!** 🚀
