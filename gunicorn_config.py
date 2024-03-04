# gunicorn_config.py

# Number of worker processes
workers = 2

# Bind to 0.0.0.0:80
bind = '0.0.0.0:80'

# Enable access logging
accesslog = '-'  # Log to stdout
