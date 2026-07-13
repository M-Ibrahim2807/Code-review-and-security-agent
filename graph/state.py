from typing import TypedDict
from pathlib import Path


class GraphState(TypedDict):
 
    repo_url: str

    
    repository_path: Path

    
    python_files: list

    
    bandit_results: list
    semgrep_results: list

    llm_review: str

    report_path: str