def create_initial_deck() -> list:
    """53枚のカードを生成する(12 * 4マーク分のセット + Joker)
    X = Joker

    Returns:
        initial_deck: A ~ K + Jokerの文字列を格納しているリスト
    """
    initial_deck = []

    for n in range(1, 14):
        if n == 1:
            court_Card = "A"
        elif n == 11:
            court_Card = "J"
        elif n == 12:
            court_Card = "Q"
        elif n == 13:
            court_Card = "k"
        else:
            court_Card = str(n)
        initial_deck.append(court_Card)

    initial_deck = initial_deck * 4
    initial_deck.append("X")
    return initial_deck


def create_player(name: str, is_auto: bool = True) -> dict():
    """プレイヤー情報を作成

    Args:
        name (_type_): プレイヤー名
        is_auto (bool, optional): カード選択を自動で行うかどうか. Defaults to True.

    Returns:
        _type_: プレイヤー情報
    """
    return {"name": name, "deck": [], "is_win": False, "is_auto": is_auto}


player1 = create_player("test", is_auto=False)
player2 = create_player("test2")

print(player1)
print(player2)


sample = create_initial_deck()
print(sample)
