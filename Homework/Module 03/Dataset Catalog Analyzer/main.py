import os
import config_loader
from pathlib import Path
import processor
import exporter
import filereader

def main():
    settings = config_loader.load_config()
    loaded_datasets = filereader.load_datasets(settings)
    report = processor.process_dataset(loaded_datasets, settings)
    exporter.export_dataset_report(settings, report)
    
    

def _clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

main()