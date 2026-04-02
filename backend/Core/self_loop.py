# self_loop.py
import os
import random
import time
from backend.agents.saas_ai import build_saas
from backend.agents.marketing_ai import create_landing_page
from auto_deploy import create_or_get_repo, push_to_github, trigger_render_deploy

PROJECTS = ["AI_SaaS_Tools","AutoLandingPro","ChatBotEnterprise","SmartDashboard"]

def start_self_loop():
    while True:
        project_name = random.choice(PROJECTS)
        print(f"Creating project: {project_name}")

        # Build SaaS project
        build_saas(project_name)
        print(f"{project_name} built successfully")

        # Marketing landing page
        landing_page_path = create_landing_page(project_name)
        print(f"Landing page created at {landing_page_path}")

        # Auto GitHub push
        clone_url = create_or_get_repo()
        push_to_github(clone_url)

        # Trigger Render deploy
        trigger_render_deploy()

        print(f"Project {project_name} deployed automatically!\n")
        time.sleep(random.randint(300,600))  # 5–10 min per project

if __name__ == "__main__":
    print("Starting Multi-AI Swarm Self-Loop...")
    start_self_loop()
