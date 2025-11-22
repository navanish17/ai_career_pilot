import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "ai_career_advisor"

list_of_files = [

    # Backend structure
    f"backend/src/{project_name}/__init__.py",
    f"backend/src/{project_name}/api/__init__.py",
    f"backend/src/{project_name}/api/routes/__init__.py",
    f"backend/src/{project_name}/api/routes/auth.py",
    f"backend/src/{project_name}/api/routes/profile.py",
    f"backend/src/{project_name}/api/routes/quiz.py",
    f"backend/src/{project_name}/api/routes/career.py",
    f"backend/src/{project_name}/api/routes/roadmap.py",
    f"backend/src/{project_name}/api/routes/colleges.py",
    f"backend/src/{project_name}/api/routes/scholarships.py",
    f"backend/src/{project_name}/api/routes/agent.py",

    f"backend/src/{project_name}/core/config.py",
    f"backend/src/{project_name}/core/database.py",
    f"backend/src/{project_name}/core/logger.py",

    f"backend/src/{project_name}/models/user.py",
    f"backend/src/{project_name}/models/profile.py",
    f"backend/src/{project_name}/models/career.py",
    f"backend/src/{project_name}/models/college.py",
    f"backend/src/{project_name}/models/scholarship.py",

    f"backend/src/{project_name}/services/find_career.py",
    f"backend/src/{project_name}/services/backward_planner.py",
    f"backend/src/{project_name}/services/stream_suggester.py",
    f"backend/src/{project_name}/services/degree_suggester.py",
    f"backend/src/{project_name}/services/course_mapper.py",
    f"backend/src/{project_name}/services/college_finder.py",
    f"backend/src/{project_name}/services/scholarship_engine.py",

    f"backend/src/{project_name}/rag/loader.py",
    f"backend/src/{project_name}/rag/embeddings.py",
    f"backend/src/{project_name}/rag/vector_store.py",
    f"backend/src/{project_name}/rag/retriever.py",

    f"backend/src/{project_name}/utils/common.py",
    f"backend/src/{project_name}/utils/validators.py",

    f"backend/src/{project_name}/pipelines/college_scraper.py",
    f"backend/src/{project_name}/pipelines/scholarship_scraper.py",
    f"backend/src/{project_name}/pipelines/entrance_exam_scraper.py",

    f"backend/src/{project_name}/main.py",
    f"backend/src/{project_name}/app.py",
    "backend/requirements.txt",
    "backend/Dockerfile",

    # Frontend
    "frontend/package.json",
    "frontend/components/.gitkeep",
    "frontend/pages/.gitkeep",
    "frontend/public/.gitkeep",
    "frontend/styles/.gitkeep",
    "frontend/utils/.gitkeep",
    "frontend/hooks/.gitkeep",

    # Data
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/colleges.json",
    "data/careers.json",
    "data/scholarships.json",

    # Docs
    "docs/01-project-overview.md",
    "docs/02-app-workflow.md",
    "docs/03-apis.md",
    "docs/04-db-models.md",
    "docs/05-roadmap.md",

    # Configs
    "configs/config.yaml",
    "configs/rag.yaml",
    "configs/database.yaml",

    # Scripts
    "scripts/deployment.sh",
    "scripts/start_local.sh",
    "scripts/build.sh",

    # Root
    "docker-compose.yml",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        if not os.path.exists(filedir):
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating folder: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
