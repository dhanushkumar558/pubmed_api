from typing import List, Dict
from Bio import Entrez

Entrez.email = "dhanushkumar558@gmail.com"  # REQUIRED

def search_pubmed(query: str, max_results: int = 20) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record.get("IdList", [])

def fetch_details(id_list: List[str]) -> List[Dict]:
    if not id_list:
        return []
    ids = ",".join(id_list)
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="xml")
    records = Entrez.read(handle)
    return records.get("PubmedArticle", [])
