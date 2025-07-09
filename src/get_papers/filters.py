from typing import List, Tuple

ACADEMIC_KEYWORDS = ["university", "college", ".edu", "institute", "school", "department", "faculty"]

def is_non_academic_affiliation(aff: str) -> bool:
    aff_lower = aff.lower()
    return not any(keyword in aff_lower for keyword in ACADEMIC_KEYWORDS)

def extract_non_academic_authors(article) -> Tuple[List[str], List[str]]:
    authors = []
    companies = []

    try:
        author_list = article["MedlineCitation"]["Article"]["AuthorList"]
        for author in author_list:
            if "AffiliationInfo" in author:
                aff_info = author["AffiliationInfo"][0]
                aff = aff_info.get("Affiliation", "")
                if is_non_academic_affiliation(aff):
                    name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                    authors.append(name)
                    companies.append(aff)
    except:
        pass

    return authors, companies
