# saas_ai.py
import os
from agents.coder_ai import generate_code

PAYMENT_SYSTEMS = ["Stripe", "PayPal"]

def build_saas(project_name: str, payment="Stripe"):
    base = f"backend/projects/{project_name}"
    os.makedirs(base, exist_ok=True)

    backend_code = generate_code(f"SaaS backend for {project_name} with {payment}")
    frontend_code = generate_code(f"SaaS frontend for {project_name} with {payment}")

    with open(f"{base}/app.py", "w") as f:
        f.write(backend_code)

    with open(f"{base}/index.html", "w") as f:
        f.write(frontend_code)

    return f"{project_name} created with {payment}"
