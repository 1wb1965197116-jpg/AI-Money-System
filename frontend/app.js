const projectsDiv = document.getElementById('projects');
const refreshBtn = document.getElementById('refresh');

function fetchProjects() {
    fetch('/projects.json') // Replace with actual API or file serving project list
        .then(res => res.json())
        .then(data => {
            projectsDiv.innerHTML = '';
            data.forEach(proj => {
                const div = document.createElement('div');
                div.className = 'project';
                div.textContent = proj.name + ' - ' + proj.status;
                projectsDiv.appendChild(div);
            });
        });
}

refreshBtn.addEventListener('click', fetchProjects);
fetchProjects();
