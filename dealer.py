import random


class Dealer:
    def __init__(self):
        self.initial_deck = self.create_initial_deck()

    def create_initial_deck(self) -> list:
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

    def initial_deal(self, *args: tuple()) -> list:
        """プレイヤーの数に応して初期手札を配る

        Args:
            player (dict): ゲーム参加するユーザー情報

        Returns:
            dict: 各プレイヤーに初期手札を分配した結果の情報
        """
        random.shuffle(self.initial_deck)
        players = list(args)
        q, mod = divmod(len(self.initial_deck), len(players))

        for i in range(len(players)):
            slice_n = q
            # 端数のカードが存在する場合はそれが無くなるまで追加して配る
            if i < mod:
                slice_n += 1
            players[i].deck = self.initial_deck[:slice_n]
            del self.initial_deck[:slice_n]
        return players

    def initial_putdown(self, deck: list) -> list:
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
