from config import load_config
from ifc_reader import load_ifc
from rules import load_rules


def main():

    config = load_config()

    print("Config geladen.")

    model = load_ifc(config["ifc_path"])

    print("IFC geladen.")

    rules = load_rules(config["rules_path"])

    print("Prüfregeln geladen.")
    print(rules)


if __name__ == "__main__":
    main()