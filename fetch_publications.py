from scholarly import scholarly

scholar_id = "sPRgURoAAAAJ"  # Replace with the correct Scholar ID
print(f"Fetching Google Scholar publications for ID: {scholar_id}")

author = scholarly.search_author_id(scholar_id)
if author:
    scholarly.fill(author, sections=["publications"])
    publications = author.get("publications", [])

    pub_list = []
    for pub in publications:  
        title = pub.get("bib", {}).get("title", "Unknown Title")
        link = pub.get("pub_url", "#")
        citation = pub.get("num_citations", 0)
        pub_list.append(f"- [{title}]({link}) 📄 Citations: {citation}\n")

    print(pub_list)
    # Update README
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.readlines()

    start_marker = "<!-- PUBLICATION START -->"
    end_marker = "<!-- PUBLICATION END -->"
    
    new_readme = []
    inside_section = False
    for line in readme_content:
        if start_marker in line:
            new_readme.append(line)
            new_readme.append("**Publications:**\n")
            new_readme.extend(pub_list)
            inside_section = True
        elif end_marker in line:
            inside_section = False
            new_readme.append("\n" + line)
        elif not inside_section:
            new_readme.append(line)

    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(new_readme)

    print("README updated successfully.")
else:
    print("No author found. Check the Scholar ID.")
