const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files
app.use(express.static(__dirname));

// Serve projects JSON dynamically
app.get('/projects.json', (req, res) => {
    const projectsPath = path.join(__dirname, '../backend/projects/');
    let projectList = [];
    try {
        const dirs = fs.readdirSync(projectsPath, { withFileTypes: true })
                       .filter(d => d.isDirectory())
                       .map(d => d.name);
        projectList = dirs.map(name => ({ name, status: 'Deployed' }));
    } catch (err) {
        console.error(err);
    }
    res.json(projectList);
});

app.listen(PORT, () => console.log(`Frontend server running on port ${PORT}`));
