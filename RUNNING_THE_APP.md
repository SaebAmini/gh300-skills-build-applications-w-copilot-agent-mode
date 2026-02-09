# Running the OctoFit Tracker App

This guide will help you run both the Django backend and React frontend for testing.

## Prerequisites

- Python 3.12 (already installed in the environment)
- Node.js and npm (already installed in the environment)
- GitHub Codespace or local development environment

---

## Option 1: Quick Start (Automated)

Use this script to start both servers automatically:

```bash
# From the repository root
./start-servers.sh
```

The script will:
1. Start Django backend on port 8000
2. Start React frontend on port 3000
3. Display URLs for accessing the app

---

## Option 2: Manual Start (Step by Step)

### Step 1: Start the Django Backend

Open a terminal and run:

```bash
# Navigate to the backend directory
cd octofit-tracker/backend

# Activate the virtual environment
source venv/bin/activate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
```

You should see output like:
```
Django version 4.2.26, using settings 'octofit_tracker.settings'
Starting development server at http://0.0.0.0:8000/
```

**Backend is now running on port 8000** ✅

---

### Step 2: Start the React Frontend

Open a **NEW terminal** (keep the backend running) and run:

```bash
# Navigate to the frontend directory
cd octofit-tracker/frontend

# Set the Codespace environment variable (if using Codespaces)
export REACT_APP_CODESPACE_NAME=$CODESPACE_NAME

# Start the React development server
npm start
```

You should see output like:
```
webpack compiled successfully
```

**Frontend is now running on port 3000** ✅

---

## Accessing the Application

### In GitHub Codespaces:

1. **Frontend URL**: Look for the notification that port 3000 is available
   - Click "Open in Browser" when prompted
   - Or go to the Ports tab and click the globe icon next to port 3000
   - URL format: `https://<YOUR-CODESPACE-NAME>-3000.app.github.dev`

2. **Backend API URL**: 
   - URL format: `https://<YOUR-CODESPACE-NAME>-8000.app.github.dev/api/`
   - Test endpoint: `https://<YOUR-CODESPACE-NAME>-8000.app.github.dev/api/users/`

### Locally:

1. **Frontend**: http://localhost:3000
2. **Backend API**: http://localhost:8000/api/

---

## Testing the Application

### Test Backend API Endpoints

```bash
# Test users endpoint
curl http://localhost:8000/api/users/

# Test teams endpoint
curl http://localhost:8000/api/teams/

# Test activities endpoint
curl http://localhost:8000/api/activities/

# Test leaderboard endpoint
curl http://localhost:8000/api/leaderboard/

# Test workouts endpoint
curl http://localhost:8000/api/workouts/
```

### Navigate the Frontend

Once the React app loads in your browser:

1. **Home Page**: Welcome screen with the OctoFit logo
2. **Users**: View all superhero users from Team Marvel and Team DC
3. **Teams**: See the two competing teams
4. **Activities**: Browse logged fitness activities
5. **Leaderboard**: Check competitive rankings with total points
6. **Workouts**: Explore superhero-themed workout suggestions

---

## Stopping the Servers

### Stop Backend (Django):
- Press `Ctrl+C` in the terminal running the Django server

### Stop Frontend (React):
- Press `Ctrl+C` in the terminal running the React server

---

## Using VS Code Launch Configurations

You can also use the pre-configured launch settings:

1. Go to the "Run and Debug" panel (Ctrl+Shift+D)
2. Select "Launch Django Backend" from the dropdown
3. Click the green play button to start the backend
4. Repeat with "Launch React Frontend" for the frontend

---

## Troubleshooting

### Port Already in Use

If you get an error about ports being in use:

```bash
# Find and kill processes on port 8000 (Django)
lsof -ti:8000 | xargs kill -9

# Find and kill processes on port 3000 (React)
lsof -ti:3000 | xargs kill -9
```

### Database Issues

If you need to reset the database:

```bash
cd octofit-tracker/backend
source venv/bin/activate
rm db.sqlite3
python manage.py migrate
python manage.py populate_db
```

### Dependencies Not Installed

**Backend:**
```bash
cd octofit-tracker/backend
source venv/bin/activate
pip install -r requirements.txt
```

**Frontend:**
```bash
cd octofit-tracker/frontend
npm install
```

---

## Environment Variables

### Backend (Django)
- Automatically uses `CODESPACE_NAME` environment variable
- Configured in `settings.py` for `ALLOWED_HOSTS`

### Frontend (React)
- Uses `REACT_APP_CODESPACE_NAME` for API URL construction
- Set automatically in the start script
- Components check this to determine API endpoint URLs

---

## Sample Data

The app comes pre-loaded with:
- 10 superhero users (5 from Team Marvel, 5 from Team DC)
- 2 teams (Team Marvel and Team DC)
- 49 fitness activities
- 10 leaderboard entries
- 6 superhero-themed workouts

To repopulate the database:
```bash
cd octofit-tracker/backend
source venv/bin/activate
python manage.py populate_db
```

---

## Quick Reference

| Service | Port | Local URL | Codespace URL Pattern |
|---------|------|-----------|----------------------|
| Django Backend | 8000 | http://localhost:8000 | https://CODESPACE-8000.app.github.dev |
| React Frontend | 3000 | http://localhost:3000 | https://CODESPACE-3000.app.github.dev |

---

## Need Help?

- Check the console logs in both terminals for error messages
- Verify both servers are running before accessing the frontend
- Make sure ports 3000 and 8000 are forwarded in Codespaces
- Check browser console (F12) for frontend errors
