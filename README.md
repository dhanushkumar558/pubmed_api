# 📚 Get Papers List

A command-line Python tool to fetch research papers from **PubMed** and filter them to include only those with at least one **non-academic author** — such as from a pharma or biotech company.

---

## 📁 Project Structure

```
get-papers/
├── src/
│   └── get_papers/
│       ├── cli.py           # Typer CLI interface
│       ├── main.py          # Orchestrates the workflow
│       ├── pubmed_api.py    # Fetches data from PubMed (Entrez API)
│       ├── filtering.py     # Filters authors by academic vs non-academic
│       ├── csv_writer.py    # Saves results to CSV
│       └── __init__.py
├── tests/                   # Optional test files
├── pyproject.toml           # Poetry project config
├── README.md                # You're reading it
└── report.pdf               # Project summary report
```

---

## ⚙️ Installation

1. Ensure Python 3.9+ is installed  
2. Install Poetry → [Poetry Installation Guide](https://python-poetry.org/docs/#installation)  
3. Clone this repo and install dependencies:

```bash
poetry install
```

---

## 🚀 Usage

```bash
poetry run get-papers-list "your query" --file output.csv --debug
```

### Example:

```bash
poetry run get-papers-list "mRNA vaccine" --file results.csv --debug
```

### CLI Options:

- `--file` or `-f`: Save results to CSV (optional; prints to console if not used)  
- `--debug` or `-d`: Show extra logs and filtering steps  
- `--help` or `-h`: Show CLI usage help  

---

## 🧠 How Filtering Works

The program analyzes each paper's authors and their affiliations:

- **Academic authors** (with keywords like _university_, _college_, _.edu_, _institute_) are excluded  
- **Non-academic authors** (e.g., pharma, biotech companies) are included  
- Known companies like **Pfizer**, **Moderna**, **Genentech**, etc., are prioritized  
- If a paper has at least one non-academic author, it is included in the final results

---

## 🧪 Testing & Output

Tested with queries like `"covid vaccine"` and `"gene therapy"`.  
The tool correctly filters papers to ensure at least one author is from a **non-academic institution**.  
Handles missing emails, affiliations, and author data without crashing.

---

## 🛠 Tools & Libraries Used

- [`Biopython`](https://biopython.org/wiki/Entrez) — for accessing PubMed Entrez API  
- [`Typer`](https://typer.tiangolo.com/) — for building the CLI  
- [`pandas`](https://pandas.pydata.org/) — for CSV file handling  
- [`Poetry`](https://python-poetry.org/) — for packaging and dependency management  

---

## 📦 Test PyPI Package (Bonus)

This CLI tool was also published to **Test PyPI**.

🔗 [get-papers-list-dkv on Test PyPI](https://test.pypi.org/project/get-papers-list-dkv/)

### To install:

```bash
pip install --index-url https://test.pypi.org/simple/ get-papers-list-dkv
```

### To run:

```bash
get-papers-list "covid vaccine" -f test.csv
```

---

## 🤖 LLM Tools Used

This project was developed with assistance from **ChatGPT (OpenAI)** for:

- Designing the CLI structure  
- Implementing PubMed querying logic  
- Building the academic vs non-academic filtering  
- Error handling and documentation generation  

👉 [Link to ChatGPT Conversation Transcript](<insert-your-link-here>)

---

## ✍️ Author

**Dhanushkumar V**

---

## 📝 License

This project is shared for educational and demonstration purposes.
