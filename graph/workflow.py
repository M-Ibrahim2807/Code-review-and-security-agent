from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import GraphState

from graph.nodes import (
    clone_repository_node,
    validate_proj_node,
    read_python_files_node,
    bandit_node,
    semgrep_node,
    llm_review_node,
    report_node
)

workflow=StateGraph(GraphState)


workflow.add_node("clone", clone_repository_node)

workflow.add_node("validate", validate_proj_node)

workflow.add_node("read_files", read_python_files_node)

workflow.add_node("bandit", bandit_node)

workflow.add_node("semgrep", semgrep_node)

workflow.add_node("llm_review", llm_review_node)

workflow.add_node("report", report_node)

workflow.set_entry_point("clone")


workflow.add_edge("clone", "validate")

workflow.add_edge("validate", "read_files")

workflow.add_edge("read_files", "bandit")

workflow.add_edge("bandit", "semgrep")

workflow.add_edge("semgrep", "llm_review")

workflow.add_edge("llm_review", "report")

workflow.add_edge("report", END)

graph = workflow.compile()
