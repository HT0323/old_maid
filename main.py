from dealer import Dealer
from player import Player
from exec_game import ExecGame

dealer = Dealer()

player1 = Player("A", is_auto=False)
player2 = Player("B")
player3 = Player("C")

players = dealer.initial_deal(player1, player2, player3)

for i in range(len(players)):
    players[i].deck = dealer.initial_putdown(players[i].deck)

exec_game = ExecGame(players)
exec_game.run()
