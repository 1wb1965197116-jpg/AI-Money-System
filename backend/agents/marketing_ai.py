# marketing_ai.py
from agents.coder_ai import generate_code
import os

def create_landing_page(app_name: str):
    content = generate_code(f"Landing page + copywriting for {app_name} to maximize conversions")
    path = f"backend/projects/{app_name}/landing.html"
    with open(path, "w") as f:
        f.write(content)
    return path
