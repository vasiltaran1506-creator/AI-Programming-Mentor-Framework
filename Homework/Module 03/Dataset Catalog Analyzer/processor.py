from pathlib import Path


def process_dataset(loaded_datasets, settings):
    report = _output_dataset(loaded_datasets, settings)

    return report

def _validate_dataset(dataset):
    if "name" not in dataset:
        return False
    if not isinstance(dataset["name"], str):
        return False
    if "images" not in dataset:
        return False
    if not isinstance(dataset["images"], int):
        return False
    if "tags" not in dataset:
        return False
    if not isinstance(dataset["tags"], list):
        return False
    return True

def _sort_datasets(loaded_datasets):
    valid_datasets = []
    invalid_datasets = []
    invalid_count = 0
    for dataset in loaded_datasets:
        if _validate_dataset(dataset):
            valid_datasets.append(dataset)
        else: 
            invalid_count += 1
            invalid_datasets.append(dataset)
    return {
        "valid_datasets": valid_datasets,
        "invalid_datasets": invalid_datasets
    }

def _calculate_metrix(datasets_statuses, settings):
    valid_datasets = datasets_statuses["valid_datasets"]
    if not valid_datasets: 
        return {
            "total_images": 0,
            "average_images_per_dataset": 0,
            "largest_dataset": None,
            "below_minimum_dataset": []
        }

    total_images = sum(d["images"] for d in datasets_statuses["valid_datasets"])

    average_images_per_dataset = total_images / len(datasets_statuses["valid_datasets"])

    largest_dataset = max(datasets_statuses["valid_datasets"], key=lambda x: x["images"])

    below_minimum_names = []
    for dataset in datasets_statuses["valid_datasets"]:
        if dataset["images"] < settings["min_images_required"]:
            below_minimum_names.append(dataset["name"])
            
    return {"total_images": total_images,
            "average_images_per_dataset": average_images_per_dataset,
            "largest_dataset": [largest_dataset["name"], largest_dataset["images"]],
            "below_minimum_dataset": below_minimum_names,
            }
    
def _pack_to_dict(dataset_statuses, metrix):
    report = {
        "valid_datasets": [d["name"] for d in dataset_statuses["valid_datasets"]],
        "invalid_datasets": [d["name"] for d in dataset_statuses["invalid_datasets"]],
        "total_images_in_valid_datasets": metrix["total_images"],
        "average_images_per_dataset_in_valid_datasets": metrix["average_images_per_dataset"],
        "largest_valid_dataset": metrix["largest_dataset"],
        "below_minimum_datasets": metrix["below_minimum_dataset"]

    }
    return report

def _output_dataset(loaded_datasets, settings):
    datasets_statuses = _sort_datasets(loaded_datasets)
    metrix = _calculate_metrix(datasets_statuses, settings)
    report = _pack_to_dict(datasets_statuses, metrix)
    
    return report
