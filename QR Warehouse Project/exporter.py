from pathlib import Path
from estimate_constructor import Estimate


def format_estimate(estimate: Estimate):
    lines = []
    lines.append(estimate.project_name)
    lines.append(f"Days of rent: {estimate.days_in_rent}")
    lines.append("")

    categories = {}
    for item in estimate.items:
        if item.category not in categories:
            categories[item.category] = []    
        categories[item.category].append(item)

    for category in categories:
        lines.append(f"Category: {category}")
        for item in categories[category]:
            lines.append(f"    - {item.name} - {item.quantity} pcs - {item.total_price:.2f}")

        lines.append("")

    lines.append(f"Grand total: {estimate.grand_total}")
    text = "\n".join(lines)
    return text

def save_estimate(save_path: str, text: str, project_name: str):
    folder_path = Path(save_path)
    if not folder_path.is_dir():
        raise FileNotFoundError(f"Path not exist or is not a folder: {save_path}")
    
    full_file_name = folder_path / f"{project_name}.txt"
    full_file_name.write_text(text, encoding="utf-8")
    print(f"File '{project_name}' successfully created at {save_path}")
