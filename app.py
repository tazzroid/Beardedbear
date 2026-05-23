from flask import Flask, render_template
import json
from pathlib import Path

app = Flask(__name__)

# Profile data for the /projects header
PROFILE = {
    "name": "Kratos",
    "title": "Graphic Designer • Brand Identity • Social Media • Print",
    "bio": "I design brand systems, social media kits, and production-ready print assets that stay consistent and look premium.",
    "location": "Auckland, New Zealand",
    "links": [
        {"label": "Behance", "url": "https://www.behance.net/yourhandle"},
        {"label": "Dribbble", "url": "https://dribbble.com/yourhandle"},
        {"label": "Instagram", "url": "https://instagram.com/yourhandle"}
    ]
}

PROJECTS_PATH = Path("data/projects.json")

def load_projects():
    if not PROJECTS_PATH.exists():
        return []
    with open(PROJECTS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else []

@app.route("/")
def home():
    projects = load_projects()
    featured = projects[:6]
    return render_template("index.html", featured=featured)

@app.route("/projects")
def projects():
    items = load_projects()
    return render_template("projects.html", projects=items, profile=PROFILE)

@app.route("/project/<slug>")
def project(slug):
    items = load_projects()
    item = next((p for p in items if p.get("slug") == slug), None)
    if not item:
        return ("Not Found", 404)
    return render_template("project.html", project=item)

if __name__ == "__main__":
    app.run(debug=True)
