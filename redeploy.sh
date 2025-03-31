#!/bin/bash

APP_DIR="./"
GUNICORN_CMD="gunicorn -w 4 -b 0.0.0.0:5000 'api.app:app'"

# Navigate to app directory
cd $APP_DIR || exit

# Pull the latest changes
git pull origin main

# Install updated dependencies (if needed)
uv pip install --no-deps -r requirements.txt

# Find and kill the existing Gunicorn process
pkill -f "gunicorn"

# Restart Gunicorn
nohup $GUNICORN_CMD > /dev/null 2>&1 &

echo "Redeployment completed!"
