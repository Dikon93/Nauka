from typing import List


def powiedz_czesc(names: List[str]) -> List[str]:
    """Podsumowanie

    Args:
        names (List[str]): Tutaj wpisujesz Liste imion do wywołania

    Returns:
        List[str]: wywołuje ci osoby 
    """
    wiadomosc_powitalna = []
    for name in names:
        wiadomosc_powitalna.append(f"Siemanko {name}")

    return wiadomosc_powitalna


print(powiedz_czesc(["Adam", "Zenek", "Jozek"]))
