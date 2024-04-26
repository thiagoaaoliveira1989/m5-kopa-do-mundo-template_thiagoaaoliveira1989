from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):
    titles = data.get("titles", 0)
    first_cup_year = int(data.get("first_cup", "").split("-")[0])

    if titles < 0:
        raise NegativeTitlesError()

    # Validar se o ano da primeira copa é um ano válido
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    # Calcular o máximo de títulos possíveis
    max_possible_titles = (2024 - first_cup_year) // 4 + 1
    if titles > max_possible_titles:
        raise ImpossibleTitlesError()
