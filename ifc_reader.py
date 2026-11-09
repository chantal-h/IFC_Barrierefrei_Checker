import ifcopenshell


def load_ifc(ifc_path):
    model = ifcopenshell.open(ifc_path)
    return model