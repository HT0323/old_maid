import random


class ExecGame:
    def __init__(self, players: list):
        self.players = players

    def create_turn_index(self, passer_i: int, taker_i: int) -> tuple():
        """次にカードを引くプレイヤー、引かれるプレイヤーのindex情報を作成

        Args:
            passer_i (int): 現在のターンのカードを引いたプレイヤーのindex情報
            taker_i (int): 現在のターンのカードを引かれたプレイヤーのindex情報

        Returns:
            tuple: 次にカードを引くプレイヤー、引かれるプレイヤーのindex情報
        """
        passer_i = taker_i
        taker_i = taker_i + 1

        if passer_i >= len(self.players):
            passer_i = 0
            taker_i = 1
        elif taker_i >= len(self.players):
            taker_i = 0

        return passer_i, taker_i

    def select(self, passer: object, taker: object) -> str:
        """カードを選択も若しくは自動で引く

        Args:
            passer (object): カードを引かれるプレイヤーのオブジェクト
            taker (object): カードを引くプレイヤーのオブジェクト

        Raises:
            IndexError: 選択できるカードの範囲外を選択外を入力した場合
            ValueError: 数字以外を入力した場合

        Returns:
            str: 引いたカードの番号
        """
        if taker.is_auto:
            # 自動で引くカードを選択
            select_index = random.randrange(len(passer.deck))
        else:
            # 手動で引くカードを選択
            while True:
                text = ""
                for n in range(len(passer.deck)):
                    text += f"[{n+1}]"
                select_index = input(f"Select card of {passer.name} from {text}: ")

                try:
                    select_index = int(select_index) - 1
                    if select_index < 0 or select_index >= len(passer.deck):
                        raise IndexError()
                except ValueError:
                    print("\t*please input integer!")
                except IndexError:
                    print("\t*please input right number!")
                else:
                    break
            print(f"\tYou chose {select_index + 1}.")

        selected_card = passer.deck.pop(select_index)
        return selected_card

    def putdown_or_add(self, selected_card: str, taker: object):
        """引いたカードを手持ちに加えるかペアを捨てるかの判定
        Args:
            selected_card (str): 引いたカードの番号
            taker (object): カードを引いたプレイヤーのオブジェクト
        """
        try:
            # 引いたカードが手持ちに存在する場合ペアのカードを捨てる
            taker.deck.remove(selected_card)
        except ValueError:
            # 引いたカードが手持ちに存在しない場合手持ちに加える
            taker.deck.append(selected_card)

    def run(self):
        """ゲームスタート"""

        passer_i = -1
        taker_i = 0
        loop = 0
        rank = []

        print("GAME START")

        while True:
            loop += 1
            print(f"\n --- TURN {loop} ---")

            passer_i, taker_i = self.create_turn_index(passer_i, taker_i)
            selected_card = self.select(self.players[passer_i], self.players[taker_i])
            self.putdown_or_add(selected_card, self.players[taker_i])
            print("\tCurrent card number: ", end="")

            for i in range(len(self.players)):
                print(f"{self.players[i].name}:{len(self.players[i].deck)} ", end="")
                if len(self.players[i].deck) == 0:
                    print("WIN!!", end="")
                    rank.append(self.players.pop(i))
                    break
            if len(self.players) < 2:
                break

        rank.append(self.players.pop())
        print("\n\nGAME END\n")

        for i in range(len(rank)):
            print(f"RANK {i+1}: {rank[i].name}")
