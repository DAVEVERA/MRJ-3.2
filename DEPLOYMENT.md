# MRJ3.2 Deployment Guide

## Vercel Deployment

### Prerequisites

1. **GitHub Account** - Repository synced at https://github.com/DAVEVERA/MRJ-3.2
2. **Vercel Account** - Sign up at https://vercel.com
3. **Environment Variables** - API keys ready

### Step-by-Step Deployment

#### 1. Connect GitHub to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Search for and select `MRJ-3.2` repository
4. Click **"Import"**

#### 2. Configure Environment Variables

In Vercel dashboard → Project Settings → **Environment Variables**, add:

```
ANTHROPIC_API_KEY = sk-ant-api03-...
GEMINI_API_KEY = AIzaSy...
GEMINI_MODEL = gemini-flash-3.5
FLASK_ENV = production
```

**Optional Supabase (for image storage):**
```
SUPABASE_URL = https://your-project.supabase.co
SUPABASE_KEY = eyJhbGc...
```

#### 3. Configure Build & Deploy

Default settings should work:
- **Framework Preset:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Output Directory:** (leave empty for serverless)
- **Install Command:** `pip install -r requirements.txt`

#### 4. Deploy

1. Click **"Deploy"**
2. Wait for build to complete (2-3 minutes)
3. Once deployed, you'll get a URL like: `https://mrj-3-2.vercel.app`

### Post-Deployment

#### Test API Endpoints

```bash
# Landing page
curl https://your-deployment.vercel.app

# Analyze endpoint
curl -X POST https://your-deployment.vercel.app/analyze \
  -H "Content-Type: application/json" \
  -d '{"image":"data:image/jpeg;base64,..."}'
```

#### Monitor Performance

- **Vercel Dashboard**: Real-time logs and analytics
- **Function Duration**: Check execution time (should be < 60s)
- **API Response**: Monitor `/analyze` and `/render` latency

### Limitations & Considerations

⚠️ **Serverless Constraints:**

| Aspect | Limit | Impact |
|--------|-------|--------|
| Max Duration | 60s | Large images may timeout |
| Memory | 3GB | Sufficient for most use cases |
| File Upload | 4.5MB | Matches frontend requirement |
| Cold Start | ~3-5s | First request slower |

**Solutions:**

- **For large images**: Add image compression before upload
- **For timeouts**: Increase maxDuration in `vercel.json` (max 300s for Pro plan)
- **For cold starts**: Keep app active with periodic requests

### Custom Domain

1. Go to Project Settings → **Domains**
2. Add your domain (e.g., `mrjealousy.com`)
3. Follow DNS instructions
4. SSL certificate auto-issued

### Rollback & Version History

All deployments are versioned on Vercel:
- Click any deployment to view/rollback
- Zero-downtime rollbacks available
- Git commits trigger automatic deployments

### Environment-Specific Behavior

```python
# app.py respects FLASK_ENV
if os.getenv("FLASK_ENV") == "production":
    app.run(host="0.0.0.0", debug=False)
else:
    app.run(debug=True)
```

Vercel sets this automatically.

---

## Alternative Deployment Options

### Heroku (Alternative)

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
3. Add to requirements.txt: `gunicorn>=21.0.0`
4. Deploy:
   ```bash
   heroku login
   heroku create mrj-3-2
   git push heroku main
   heroku config:set ANTHROPIC_API_KEY=...
   ```

### Railway (Alternative)

1. Connect GitHub repo
2. Auto-detects Python/Flask
3. Add environment variables
4. Deploy with one click

### Docker (Self-Hosted)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Deploy to AWS ECS, Google Cloud Run, or any container registry.

---

## Monitoring & Logging

### Vercel Logs

```bash
# View live logs
vercel logs [deployment-url]

# Filter by endpoint
vercel logs --since 1h [deployment-url]
```

### Error Tracking

Add Sentry for error monitoring:

```python
import sentry_sdk
sentry_sdk.init("https://key@sentry.io/project")
```

### Analytics

- **Function Invocations**: Track API usage
- **Response Time**: Monitor performance
- **Error Rate**: Catch issues early

---

## Updating After Deployment

Push updates to GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```

Vercel auto-deploys on push. To manually trigger:
```bash
vercel --prod
```

---

## Troubleshooting

### Deployment Fails

Check logs in Vercel dashboard for:
- Build errors → Fix `requirements.txt` or import issues
- Runtime errors → Check function timeout or memory
- Environment variable missing → Add to dashboard

### API Returns 500

1. Verify API keys in Vercel environment
2. Check Anthropic/Gemini API rate limits
3. Review function logs in dashboard

### Slow Response Times

1. Check function duration (target < 30s)
2. Optimize image size before upload
3. Cache results if possible

### CORS Issues

Flask-CORS is configured in `app.py`:
```python
CORS(app)  # Allows all origins
```

For production, restrict to specific domains:
```python
CORS(app, resources={
    r"/analyze": {"origins": ["https://yoursite.com"]},
    r"/render": {"origins": ["https://yoursite.com"]}
})
```

---

## Production Checklist

- [ ] Environment variables configured in Vercel
- [ ] API keys rotated and secured
- [ ] `.env` file excluded from git (.gitignore)
- [ ] `.env.example` committed for reference
- [ ] Domain connected and SSL active
- [ ] Monitoring/logging set up
- [ ] Rate limiting configured (if needed)
- [ ] Error handling & user feedback implemented
- [ ] Performance tested with production data
- [ ] Rollback plan documented

---

## Support

For issues:
- **Vercel Docs**: https://vercel.com/docs
- **GitHub Issues**: https://github.com/DAVEVERA/MRJ-3.2/issues
- **Framework Docs**: https://flask.palletsprojects.com
