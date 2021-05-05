from datetime import date


class ConfigTest:
    @staticmethod
    def get_graph_hausse():
        # Config courbe en hausse
        day1h = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 60, 0]}
        day2h = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 70, 0]}
        day3h = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 90, 0]}
        day4h = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 85, 0]}
        day5h = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 87, 0]}
        day6h = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 95, 0]}
        day7h = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 98, 0]}
        day8h = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 93, 0]}
        day9h = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 99, 0]}
        day10h = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 103, 0]}
        day11h = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 101, 0]}
        day12h = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 105, 0]}
        day13h = {'date': date(2020, 1, 16), 'data': [0, 0, 0, 104, 0]}
        day14h = {'date': date(2020, 1, 17), 'data': [0, 0, 0, 106, 0]}
        day15h = {'date': date(2020, 1, 18), 'data': [0, 0, 0, 107, 0]}

        graphDataH = list()
        graphDataH.append(day1h)
        graphDataH.append(day2h)
        graphDataH.append(day3h)
        graphDataH.append(day4h)
        graphDataH.append(day5h)
        graphDataH.append(day6h)
        graphDataH.append(day7h)
        graphDataH.append(day8h)
        graphDataH.append(day9h)
        graphDataH.append(day10h)
        graphDataH.append(day11h)
        graphDataH.append(day12h)
        graphDataH.append(day13h)
        graphDataH.append(day14h)
        graphDataH.append(day15h)

        return graphDataH

    @staticmethod
    def get_graph_baisse():
        # Config courbe en baisse
        day1b = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 100, 0]}
        day2b = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 96, 0]}
        day3b = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 94, 0]}
        day4b = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 90, 0]}
        day5b = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 91, 0]}
        day6b = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 86, 0]}
        day7b = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 84, 0]}
        day8b = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 88, 0]}
        day9b = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 85, 0]}
        day10b = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 80, 0]}
        day11b = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 77, 0]}
        day12b = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 76, 0]}
        day13b = {'date': date(2020, 1, 16), 'data': [0, 0, 0, 73, 0]}
        day14b = {'date': date(2020, 1, 17), 'data': [0, 0, 0, 72, 0]}
        day15b = {'date': date(2020, 1, 18), 'data': [0, 0, 0, 74, 0]}

        graphDataB = list()
        graphDataB.append(day1b)
        graphDataB.append(day2b)
        graphDataB.append(day3b)
        graphDataB.append(day4b)
        graphDataB.append(day5b)
        graphDataB.append(day6b)
        graphDataB.append(day7b)
        graphDataB.append(day8b)
        graphDataB.append(day9b)
        graphDataB.append(day10b)
        graphDataB.append(day11b)
        graphDataB.append(day12b)
        graphDataB.append(day13b)
        graphDataB.append(day14b)
        graphDataB.append(day15b)

        return graphDataB

    @staticmethod
    def get_graph_stable():
        # Config courbe stable
        day1s = {'date': date(2020, 1, 1), 'data': [0, 0, 0, 60, 0]}
        day2s = {'date': date(2020, 1, 2), 'data': [0, 0, 0, 62, 0]}
        day3s = {'date': date(2020, 1, 3), 'data': [0, 0, 0, 59, 0]}
        day4s = {'date': date(2020, 1, 4), 'data': [0, 0, 0, 58, 0]}
        day5s = {'date': date(2020, 1, 5), 'data': [0, 0, 0, 61, 0]}
        day6s = {'date': date(2020, 1, 8), 'data': [0, 0, 0, 60, 0]}
        day7s = {'date': date(2020, 1, 9), 'data': [0, 0, 0, 57, 0]}
        day8s = {'date': date(2020, 1, 10), 'data': [0, 0, 0, 63, 0]}
        day9s = {'date': date(2020, 1, 11), 'data': [0, 0, 0, 61, 0]}
        day10s = {'date': date(2020, 1, 12), 'data': [0, 0, 0, 59, 0]}
        day11s = {'date': date(2020, 1, 14), 'data': [0, 0, 0, 62, 0]}
        day12s = {'date': date(2020, 1, 15), 'data': [0, 0, 0, 60, 0]}
        day13s = {'date': date(2020, 1, 16), 'data': [0, 0, 0, 55, 0]}
        day14s = {'date': date(2020, 1, 17), 'data': [0, 0, 0, 58, 0]}
        days15s = {'date': date(2020, 1, 18), 'data': [0, 0, 0, 62, 0]}

        graphDataS = list()
        graphDataS.append(day1s)
        graphDataS.append(day2s)
        graphDataS.append(day3s)
        graphDataS.append(day4s)
        graphDataS.append(day5s)
        graphDataS.append(day6s)
        graphDataS.append(day7s)
        graphDataS.append(day8s)
        graphDataS.append(day9s)
        graphDataS.append(day10s)
        graphDataS.append(day11s)
        graphDataS.append(day12s)
        graphDataS.append(day13s)
        graphDataS.append(day14s)
        graphDataS.append(days15s)

        return graphDataS
