from typing import List, Dict
from get_papers.pubmed_api import search_pubmed, fetch_details
from get_papers.filters import extract_non_academic_authors

def get_papers(query: str, file: str = "", debug: bool = False) -> None:
    ids = search_pubmed(query, max_results=50)
    if debug:
        print(f"Found {len(ids)} IDs")

    articles = fetch_details(ids)
    output_data = []

    for article in articles:
        paper_id = article["MedlineCitation"]["PMID"]
        title = article["MedlineCitation"]["Article"].get("ArticleTitle", "")
        pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"].get("PubDate", {})
        date_str = pub_date.get("Year", "Unknown")

        authors, companies = extract_non_academic_authors(article)
        if authors:
            email = "Not available"
            try:
                for aff in companies:
                    if "@" in aff:
                        email = aff.split()[-1]
                        break
            except:
                pass

            output_data.append({
                "PubmedID": paper_id,
                "Title": title,
                "Publication Date": date_str,
                "Non-academic Author(s)": "; ".join(authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email
            })

    if file:
        from get_papers.csv_writer import save_to_csv
        save_to_csv(output_data, file)
        print(f"✅ Results saved to {file}")
    else:
        for row in output_data:
            print(row)
