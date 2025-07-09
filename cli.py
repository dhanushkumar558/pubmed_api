import typer
from get_papers.main import get_papers

app = typer.Typer()

@app.command()
def fetch(
    query: str,
    file: str = "",
    debug: bool = False
):
    """Fetch PubMed papers with non-academic authors"""
    get_papers(query, file, debug)

if __name__ == "__main__":
    app()
