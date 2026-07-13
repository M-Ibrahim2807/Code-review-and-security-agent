from pathlib import Path
from git import Repo
from app.config import settings
import shutil


def clone_repository(repo_url:str)->Path:
    repository_path=settings.REPOSITORY_DIR/"current_repository"

    if repository_path.exists():
        shutil.rmtree(repository_path)


    Repo.clone_from(repo_url,repository_path)
    
    return repository_path
       
       