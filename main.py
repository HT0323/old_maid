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


sample = create_initial_deck()
print(sample)
