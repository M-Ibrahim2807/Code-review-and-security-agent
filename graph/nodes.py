from graph.state import GraphState

from services.clone_repo import clone_repository
from services.proj_val import validate_project
from services.bandit_runner import run_bandit
from services.semgrep_runner import run_semgrep
from services.file_reader import read_python_files


def clone_repository_node(state:GraphState):
    repository_path=clone_repository(state["repo_url"])

    state["repository_path"]=repository_path

    return state
def validate_proj_node(state:GraphState):
     validate_project(state['repository_path'])

     return state

def read_python_files_node(state:GraphState):
     files=read_python_files(state["repository_path"])
     state["python_files"]=files

     return state

def bandit_node(state:GraphState):
     results=run_bandit(state["repository_path"])
     state["bandit_results"]=results
     return state

def semgrep_node(state:GraphState):
     results=run_semgrep(state["repository_path"])
     state["semgrep_results"]=results
     return state

def llm_review_node(state:GraphState):
     print("llm review node")
     return state
 
def report_node(state: GraphState):

    print("Generate Report Node")

    return state
     
