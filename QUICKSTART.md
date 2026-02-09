# 🚀 Quick Start Guide - OctoFit Tracker

## Fastest Way to Run

```bash
./start-servers.sh
```

This starts both backend (Django) and frontend (React) automatically!

---

## Manual Commands

### Start Backend Only
```bash
cd octofit-tracker/backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### Start Frontend Only
```bash
cd octofit-tracker/frontend
export REACT_APP_CODESPACE_NAME=$CODESPACE_NAME
npm start
```

---

## Access URLs

### GitHub Codespaces
- **Frontend**: Click "Open in Browser" when port 3000 notification appears
- **Backend API**: `https://YOUR-CODESPACE-NAME-8000.app.github.dev/api/`

### Local Development
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api/

---

## Test the API

```bash
# Test all endpoints
curl http://localhost:8000/api/users/
curl http://localhost:8000/api/teams/
curl http://localhost:8000/api/leaderboard/
```

---

## Stop Servers

Press **Ctrl+C** in each terminal window

Or if using the automated script, **Ctrl+C** once will stop both servers.

---

## Need Help?

See [RUNNING_THE_APP.md](./RUNNING_THE_APP.md) for detailed instructions and troubleshooting.
