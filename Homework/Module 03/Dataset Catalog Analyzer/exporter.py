from pathlib import Path
import json

def export_dataset_report(settings, report):
    output_path = Path(settings['output_file_path'])

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)
        