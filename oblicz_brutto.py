def oblicz_brutto(netto: float, vat: float) -> float:
    """
    Args:
        netto (float): _description_
        vat (float): _description_

    Returns:
        float: _description_
    """

    return netto * (1 + vat)
