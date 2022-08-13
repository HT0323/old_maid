import random


def create_initial_deck() -> list:
    """53枚のカードを生成する(13 * 4マーク分のセット + Joker)
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
        name (string): プレイヤー名
        is_auto (bool, optional): カード選択を自動で行うかどうか. Defaults to True.

    Returns:
        dict: プレイヤー情報
    """
    return {"name": name, "deck": [], "is_win": False, "is_auto": is_auto}


def initial_deal(initial_deck: list, *args: tuple()) -> list:
    """プレイヤーの数に応して初期手札を配る

    Args:
        initial_deck (list): create_initial_deckで作成したカードのリスト
        player(dict): ゲーム参加するユーザー情報

    Returns:
        dict: 各プレイヤーに初期手札を分配した結果の情報
    """
    random.shuffle(initial_deck)
    players = list(args)
    q, mod = divmod(len(initial_deck), len(players))

    for i in range(len(players)):
        slice_n = q
        # 端数のカードが存在する場合はそれが無くなるまで追加して配る
        if i < mod:
            slice_n += 1
        players[i]["deck"] = initial_deck[:slice_n]
        del initial_deck[:slice_n]
    return players


initial_deck = create_initial_deck()

player1 = create_player("test", is_auto=False)
player2 = create_player("test2")
player3 = create_player("test3")


players = initial_deal(initial_deck, player1, player2, player3)
print(players)
