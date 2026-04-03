import os
import random
import time
import json
from backend.agents.saas_ai import build_saas
from backend.agents.marketing_ai import create_landing_page
from auto_deploy import create_or_get_repo, push_to_github, trigger_render_deploy

PROJECTS = ["AI_SaaS_Tools","AutoLandingPro","ChatBotEnterprise","SmartDashboard"]

FRONTEND_JSON_PATH = os.path.join(os.path.dirname(__file__), "../../frontend/projects.json")

def update_frontend_json(project_names):
    """Update the frontend dashboard JSON with live project status."""
    project_list = [{"name": name, "status": "Deployed"} for name in project_names]
    with open(FRONTEND_JSON_PATH, "w") as f:
        json.dump(project_list, f, indent=2)

def start_self_loop():
    created_projects = []

    while True:
        project_name = random.choice(PROJECTS)
        if project_name in created_projects:
            # Skip duplicates
            time.sleep(5)
            continue

        print(f"Creating project: {project_name}")

        # Build SaaS project
        build_saas(project_name)
        print(f"{project_name} built successfully")

        # Marketing landing page
        landing_page_path = create_landing_page(project_name)
        print(f"Landing page created at {landing_page_path}")

        # Add to created projects
        created_projects.append(project_name)
        update_frontend_json(created_projects)
        print(f"Updated frontend projects.json with {len(created_projects)} projects")

        # Auto GitHub push
        clone_url = create_or_get_repo()
        push_to_github(clone_url)

        # Trigger Render deploy
        trigger_render_deploy()

        print(f"Project {project_name} deployed automatically!\n")
        time.sleep(random.randint(300, 600))  # 5–10 min per project

if __name__ == "__main__":
    print("Starting Multi-AI Swarm Self-Loop with live frontend JSON...")
    start_self_loop()
