def greet(name):
    print("Salut, " + name + "!")


greet("Alex")
greet("Yannick")


def season_pref(season='Eté'):
    print('Ma saison préférée est: ' + season)

season_pref("Printemps")
season_pref()


def visit(*countries):
    for country in countries:
        print("J'ai visité ce pays: " + country)


visit('Venezuela', 'Allemagne', 'Finlande', 'France')


def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + " " + competitor_2 + " " + competitor_3)


list_game("Jullien", "Eva", "Anne")
list_game(competitor_2="Eva", competitor_1="Anne", competitor_3="Jullien")