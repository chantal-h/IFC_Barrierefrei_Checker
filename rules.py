import pandas as pd


def load_rules(rules_path):
    rules = pd.read_excel(rules_path)
    return rules