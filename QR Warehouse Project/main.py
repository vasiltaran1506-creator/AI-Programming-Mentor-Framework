from catalog_loader import load_catalog
from estimate_constructor import Estimate, Inventory
from price_policy import Standart_Policy, VGIK_Policy
from logger import FileLogger, ConsoleLogger
import exporter
import yaml
import os
from pathlib import Path


def main():
    #АБСОЛЮТНЫЕ ПУТИ
    BASE_DIR = Path(__file__).resolve().parent
    CONFIG_PATH = BASE_DIR / "config.yaml"

    #ЧТЕНИЕ config.yaml
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    catalog_path = str(BASE_DIR / config["catalog_path"])
    save_path = str(BASE_DIR / config["save_path"])
    log_path = str(BASE_DIR / config["log_path"])
    log_mode = config["log_mode"]

    # СОЗДАНИЕ ЛОГГЕРА
    if log_mode == "FileLog":
        logger = FileLogger(log_path)
    elif log_mode == "ConsoleLog":
        logger = ConsoleLogger()

    #ЗАГРУЗКА catalog.json
    catalog = load_catalog(catalog_path)

    #СОЗДАНИЕ Inventory и регистрация оборудоавия из catalog.json
    inventory = Inventory(logger=logger)
    inventory.register_equipment(catalog)

    #ВВОД НАЗВАНИЯ И ПРОДОЛЖИТЕЛЬНОСТИ ПРОЕКТА
    project_name = input("Enter project name: ")
    logger.log_info(f"Entered project name: {project_name}")
    days = int(input("Enter days of rent: "))
    logger.log_info(f"Entered project duration: {days} days")

    #ОПРЕДЕЛЕНИЕ ЦЕНОВОЙ ПОЛИТИКИ
    price_policy_input = input("Enter price policy:\n1. Standart.\n2.VGIK Student")
    if price_policy_input == "1":
        price_policy = Standart_Policy()
        logger.log_info(f"Entered Price Policy: Standart_Policy")
    elif price_policy_input == "2":
        price_policy = VGIK_Policy()
        logger.log_info("Entered Price Policy: VGIK_Policy")

    #СОЗДАНИЕ Estimate
    estimate = Estimate(
        project_name=project_name,
        days_in_rent=days,
        price_policy=price_policy, 
        logger=logger
    )

    while True:
        scan = input("Enter SKU ('done' for save): ")
        logger.log_info(f"Entered SKU: {scan}")
        clear_console()

        parts = scan.split()
        if not parts:
            continue 
        if parts[0] == "delete" and len(parts) >= 2:
            sku = parts[1]
            status, quantity = estimate.remove_one(sku)

            if status == "decreased_by_1":
                inventory.release_equipment(sku, quantity)
                logger.log_info("Equipment quantity decreased by 1")

            elif status == "removed_from_estimate":
                inventory.release_equipment(sku, quantity)
                logger.log_info("Equipment deleted from the estimate")

            elif status == "not_in_estimate":
                logger.log_warning(f"Entered scan {sku} not in current estimate")
            display_estimate(estimate)
            continue
            
        elif scan == "done": 
            text = exporter.format_estimate(estimate)
            exporter.save_estimate(save_path, text, project_name)
            break

        elif scan == "stop":
            break

        status, equipment = inventory.check_and_reserve(scan)
        if status == "reserved" and equipment is not None:
            status = estimate.process_scan(scan, equipment)
            if status == "added":
                logger.log_info(f"{equipment.name} added to estimate")
            elif status == "quantity_updated":
                logger.log_info(f"Quantity of {equipment.name} updated successfully")
        elif status == "over_stock" and equipment is not None:
            logger.log_warning(f"Equipment {equipment.name} is out of stock")
        elif status == "not_found":
            logger.log_warning(f"No scan {scan} in catalog")

        display_estimate(estimate)


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

