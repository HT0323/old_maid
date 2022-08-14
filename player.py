class Player:
    def __init__(self, name: str, is_auto: bool = True):
        """プレイヤー情報を作成

        Args:
            name (string): プレイヤー名
            is_auto (bool, optional): カード選択を自動で行うかどうか. Defaults to True.
        """

        self.name = name
        self.deck = []
        self.is_win = False
        self.is_auto = is_auto

    def __repr__(self):
        return f"name={self.name}\ndeck={self.deck}\nis_win={self.is_win}\nis_auto={self.is_auto}"


p = Player("name")
print(p)
