import warnings

PCT_LIMIT_20 = 22

def can_buy_alc(age, alc_pct):
    """
    Determine whether or not a person can buy the drink.

    Parameters
    ----------
    age : int
        The age of the person.
    alc_pct : float
        The volume percentage alcohol in the beverage (0-100).
    """
    if age >= 20 or alc_pct == 0:
        return True
    return (18 <= age <= 20) and alc_pct < PCT_LIMIT_20


if __name__ == "__main__":
    age = int(input("age: "))
    alcohol = float(input("alcohol percent: "))
    can_buy = can_buy_alc(age, alcohol)
    print(can_buy)