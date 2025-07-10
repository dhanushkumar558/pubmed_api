from typing import List, Tuple, Dict, Any

# Keywords that likely indicate an academic institution
ACADEMIC_KEYWORDS = [
    "university", "college", ".edu", "institute", "school", "department", "faculty"
]

# Known pharma and biotech company keywords (partial match)
KNOWN_COMPANIES = [
    "pfizer", "moderna", "novartis", "astrazeneca", "genentech", "gsk", 
    "biotech", "pharma", "abbvie", "roche", "sanofi", "bayer", "merck", "amgen"
]

def is_academic(aff: str) -> bool:
    # Checks if the affiliation string looks academic
    return any(keyword in aff.lower() for keyword in ACADEMIC_KEYWORDS)

def is_company(aff: str) -> bool:
    # Checks if the affiliation mentions a known pharma/biotech company
    return any(company in aff.lower() for company in KNOWN_COMPANIES)

def should_include_affiliation(aff: str) -> bool:
    # Include if it's a company; otherwise only if it's not academic
    return is_company(aff) or not is_academic(aff)

def extract_non_academic_authors(article: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    # Extracts authors with non-academic affiliations from the article
    authors, companies = [], []

    try:
        author_list = article["MedlineCitation"]["Article"].get("AuthorList", [])
        for author in author_list:
            if "AffiliationInfo" in author:
                aff = author["AffiliationInfo"][0].get("Affiliation", "")
                if should_include_affiliation(aff):
                    name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                    authors.append(name)
                    companies.append(aff)
    except Exception as e:
        print(f"[WARNING] Failed to extract authors: {e}")

    return authors, companies
