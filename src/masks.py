def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number is None:
        return ""
    refactored_card_number: str = str(card_number)
    scale_of_number = len(refactored_card_number)
    if scale_of_number <= 6:
        if scale_of_number <= 2:
            return "*" * scale_of_number
        return "*" * 2 + " " + "*" * (scale_of_number - 2)
    return " ".join(
        [refactored_card_number[:4], refactored_card_number[4:6] + "**", "****", refactored_card_number[-4:]]
    )


def get_mask_account(card_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    refactored_card_number = str(card_number)
    length = len(refactored_card_number)
    if card_number is None:
        return ""
    elif length > 4:
        return "**" + refactored_card_number[-4:]
    else:
        if length == 1:
            return "*"
        visible_length = length - 2
        visible_digits = refactored_card_number[-visible_length:] if visible_length > 0 else ""
        return "**" + visible_digits
