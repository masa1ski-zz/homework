from warriors import *


king_yaroglek = Spearman('King Yaroglek')
king_gravet = Infantryman('King Gravet')
king_harlaus = Knight('King Harlaus')

king_harlaus.go_fight(king_gravet)
king_harlaus.heal()
king_gravet.heal()

king_gravet.go_fight(king_yaroglek)
king_gravet.heal()
king_yaroglek.heal()

king_yaroglek.go_fight(king_harlaus)
king_yaroglek.heal()
king_harlaus.heal()
