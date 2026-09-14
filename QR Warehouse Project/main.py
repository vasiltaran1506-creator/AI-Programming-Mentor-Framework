from estimate_constructor import Estimate, Inventory
from price_policy import Standart_Policy, VGIK_Policy
from logger import FileLogger, ConsoleLogger
from repository import SQLRepository
import exporter
import yaml
import os
from pathlib import Path

from use_cases import AddItemToEstimate


def main():
    #АБСОЛЮТНЫЕ ПУТИ
    BASE_DIR = Path(__file__).resolve().parent
    CONFIG_PATH = BASE_DIR / "config.yaml"

    #Чтение конфига
    config = read_config(CONFIG_PATH, BASE_DIR)

    #Создание Logger
    logger = create_logger(config["log_mode"], config["log_path"])

    #Создание репозитория
    #repository = create_repository(config["catalog_path"])
    repository = create_repository(config["db_path"])

    #Создание Inventory
    inventory = Inventory(repository)

    #Ввод названя и продолжительности проекта
    project_name, days = input_info()

    #Определение ценовой политики
    price_policy = decide_price_policy()

    #Создание Estimate
    estimate = Estimate(
        project_name=project_name,
        days_in_rent=days,
        price_policy=price_policy, 
        logger=logger
    )

    #Создание UseCases
    add_item_use_case = AddItemToEstimate(
        inventory=inventory,
        estimate=estimate
    )

    while True:
        sku, action = enter_scan()
        if action is None:
            if sku == "done":
                save_and_exit(config, estimate)
                break
            elif sku == "stop":
                break
            else:
                status, equipment = add_item_use_case.execute(sku)

        if action is not None:
            if action == "delete":
                status = delete_item(sku, estimate, inventory)

        clear_console()

        display_estimate(estimate)


def read_config(CONFIG_PATH, BASE_DIR):
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    catalog_path = str(BASE_DIR / config["catalog_path"])
    save_path = str(BASE_DIR / config["save_path"])
    log_path = str(BASE_DIR / config["log_path"])
    log_mode = config["log_mode"]
    db_path = str(BASE_DIR / config["db_path"])

    return {
        "catalog_path": catalog_path,
        "save_path": save_path,
        "log_path": log_path,
        "log_mode": log_mode,
        "db_path": db_path
    }

def create_logger(log_mode, log_path):
    if log_mode == "FileLog":
        return FileLogger(log_path)
    elif log_mode == "ConsoleLog":
        return ConsoleLogger()
    else:
        raise ValueError(f"Invalid log mode: {log_mode}")

def create_repository(db_path):
    return SQLRepository(db_path)

def input_info():
    project_name = input("Enter project name: ")
    days = int(input("Enter days of rent: "))
    return project_name, days

def decide_price_policy():
    price_policy_input = input("Enter price policy:\n1. Standart.\n2.VGIK Student")
    if price_policy_input == "1":
        return Standart_Policy()
    elif price_policy_input == "2":
        return VGIK_Policy()
    raise ValueError("Invalid price policy")

def enter_scan():
    scan = input("Enter SKU (or 'delete' for delete; 'done' for save):\n")
    if len(scan.split()) >= 2:
        parts = _split_scan(scan)
        action = parts[0]
        sku = parts[1]
        return sku, action
    else:
        sku = scan
        return sku, None

def _split_scan(scan):
    parts = scan.split()
    if len(parts) >= 2:
        return parts
    else:
        return scan

def delete_item(sku: str, estimate: Estimate, inventory: Inventory):
    status, quantity = estimate.remove_one(sku)
    if status == "decreased_by_1":
        inventory.release_equipment(sku, quantity)
        return status
    elif status == "removed_from_estimate":
        inventory.release_equipment(sku, quantity)
        return status
    elif status == "not_in_estimate":
        return status
    
def save_and_exit(config, estimate):
    exporter.save_estimate(config["save_path"],exporter.format_estimate(estimate), estimate.project_name)


#       =========================================
#       =           Service functions           =
#       =========================================


def display_estimate(estimate: Estimate):
    text = exporter.format_estimate(estimate)
    print(text)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()

