import typer
from typing import List
from get_papers.main import get_papers

app = typer.Typer()

@app.command()
def fetch(
    query: List[str],
    file: str = "",
    debug: bool = False
):
    """Fetch PubMed papers with non-academic authors"""
    full_query = " ".join(query)
    get_papers(full_query, file, debug)

if __name__ == "__main__":
    app()
