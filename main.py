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


def create_player(name: str, is_auto: bool = True) -> dict:
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
        player (dict): ゲーム参加するユーザー情報

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


def initial_putdown(deck: list) -> list:
    """初期手札を重複しているカードを捨てる

    Args:
        deck (list): 1プレイヤーの手札

    Returns:
        list: 重複削除後の手札
    """
    while len(set(deck)) != len(deck):
        popped_card = deck.pop(0)
        if popped_card in deck:
            # 同じ数字を持っているペアが存在する場合
            deck.remove(popped_card)
        else:
            # 同じ数字を持っているペアが存在しない場合
            deck.append(popped_card)
    return deck


def create_turn_index(passer_i: int, taker_i: int, players: list) -> tuple():
    """次にカードを引くプレイヤー、引かれるプレイヤーのindex情報を作成

    Args:
        passer_i (int): 現在のターンのカードを引いたプレイヤーのindex情報
        taker_i (int): 現在のターンのカードを引かれたプレイヤーのindex情報
        passer_i (int): プレイヤーのの一覧情報

    Returns:
        tuple: 次にカードを引くプレイヤー、引かれるプレイヤーのindex情報
    """
    passer_i = taker_i
    taker_i = taker_i + 1

    if passer_i >= len(players):
        passer_i = 0
        taker_i = 1
    elif taker_i >= len(players):
        taker_i = 0

    return passer_i, taker_i


initial_deck = create_initial_deck()
player1 = create_player("test", is_auto=False)
player2 = create_player("test2")
player3 = create_player("test3")
players = initial_deal(initial_deck, player1, player2, player3)
for i in range(len(players)):
    players[i]["deck"] = initial_putdown(players[i]["deck"])
print(player1["deck"])
print(player2["deck"])
print(player3["deck"])


players = ["Green", "Yellow", "Red"]

passer_i = 0
taker_i = 1

passer_i, taker_i = create_turn_index(passer_i, taker_i, players)
print(f"{players[passer_i]} ==> {players[taker_i]}")

passer_i, taker_i = create_turn_index(passer_i, taker_i, players)
print(f"{players[passer_i]} ==> {players[taker_i]}")
