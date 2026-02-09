#!/bin/bash

# OctoFit Tracker - Start Both Servers
# This script starts both the Django backend and React frontend

set -e  # Exit on error

echo "🏋️  Starting OctoFit Tracker Application..."
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BACKEND_DIR="$SCRIPT_DIR/octofit-tracker/backend"
FRONTEND_DIR="$SCRIPT_DIR/octofit-tracker/frontend"

# Check if directories exist
if [ ! -d "$BACKEND_DIR" ]; then
    echo "❌ Backend directory not found at $BACKEND_DIR"
    exit 1
fi

if [ ! -d "$FRONTEND_DIR" ]; then
    echo "❌ Frontend directory not found at $FRONTEND_DIR"
    exit 1
fi

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start Django Backend
echo -e "${BLUE}Step 1: Starting Django Backend...${NC}"
cd "$BACKEND_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please create it first:"
    echo "   python3 -m venv venv"
    exit 1
fi

# Activate virtual environment and start Django
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000 > /tmp/django.log 2>&1 &
BACKEND_PID=$!

# Wait a bit for Django to start
sleep 3

# Check if Django started successfully
if ! ps -p $BACKEND_PID > /dev/null; then
    echo "❌ Failed to start Django backend. Check /tmp/django.log for errors."
    cat /tmp/django.log
    exit 1
fi

echo -e "${GREEN}✅ Django backend started on port 8000 (PID: $BACKEND_PID)${NC}"

# Start React Frontend
echo ""
echo -e "${BLUE}Step 2: Starting React Frontend...${NC}"
cd "$FRONTEND_DIR"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}⚠️  node_modules not found. Installing dependencies...${NC}"
    npm install
fi

# Set environment variable for Codespaces
export REACT_APP_CODESPACE_NAME=$CODESPACE_NAME

# Start React (suppress browser opening)
BROWSER=none npm start > /tmp/react.log 2>&1 &
FRONTEND_PID=$!

# Wait for React to start
echo "⏳ Waiting for React to compile..."
sleep 15

# Check if React started successfully
if ! ps -p $FRONTEND_PID > /dev/null; then
    echo "❌ Failed to start React frontend. Check /tmp/react.log for errors."
    cat /tmp/react.log
    exit 1
fi

echo -e "${GREEN}✅ React frontend started on port 3000 (PID: $FRONTEND_PID)${NC}"

# Display access URLs
echo ""
echo "================================================"
echo -e "${GREEN}🎉 Both servers are running!${NC}"
echo "================================================"
echo ""

if [ -z "$CODESPACE_NAME" ]; then
    # Local development
    echo "📱 Frontend:  http://localhost:3000"
    echo "🔧 Backend:   http://localhost:8000/api/"
else
    # GitHub Codespaces
    echo "📱 Frontend:  https://$CODESPACE_NAME-3000.app.github.dev"
    echo "🔧 Backend:   https://$CODESPACE_NAME-8000.app.github.dev/api/"
fi

echo ""
echo "💡 Test endpoints:"
echo "   - Users:       /api/users/"
echo "   - Teams:       /api/teams/"
echo "   - Activities:  /api/activities/"
echo "   - Leaderboard: /api/leaderboard/"
echo "   - Workouts:    /api/workouts/"
echo ""
echo "📝 Logs:"
echo "   - Django:  /tmp/django.log"
echo "   - React:   /tmp/react.log"
echo ""
echo "Press Ctrl+C to stop both servers"
echo "================================================"

# Keep script running
wait
