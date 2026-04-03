Write-Host "=== Starting AI Money System Full Deployment ==="

# Step 1: Install frontend Node dependencies
Write-Host "Installing frontend dependencies..."
cd frontend
npm install
Write-Host "Frontend dependencies installed."
cd ..

# Step 2: Start frontend server in background
Write-Host "Starting frontend server..."
Start-Process "node" "frontend/server.js"
Write-Host "Frontend server started at http://localhost:3000"

# Step 3: Run backend self-loop in background
Write-Host "Starting backend AI self-loop..."
Start-Process "python" "backend/core/self_loop.py"
Write-Host "Backend self-loop running..."

# Step 4: GitHub auto-push & Render deploy
Write-Host "Triggering GitHub push and Render deploy..."
python auto_deploy.py

Write-Host "=== Full AI Money System Deployment Complete ==="
pause
