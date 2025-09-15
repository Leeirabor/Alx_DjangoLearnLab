# Security & HTTPS configuration

- DEBUG must be False in production.
- We enable:
  - SECURE_SSL_REDIRECT = True
  - SECURE_HSTS_SECONDS = 31536000
  - SESSION_COOKIE_SECURE = True
  - CSRF_COOKIE_SECURE = True
  - X_FRAME_OPTIONS = DENY
  - SECURE_CONTENT_TYPE_NOSNIFF = True
  - SECURE_BROWSER_XSS_FILTER = True

- Proxy: If using Nginx/Gunicorn, set SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") and ensure Nginx sends X-Forwarded-Proto.

- To obtain TLS cert with Let's Encrypt (Ubuntu):
  sudo apt install certbot python3-certbot-nginx
  sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

- Test with:
  curl -I https://yourdomain.com
