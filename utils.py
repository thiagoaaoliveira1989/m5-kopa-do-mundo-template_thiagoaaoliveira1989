from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
import datetime


def data_processing(data):
    titles = data.get("titles", 0)
    first_cup = data.get("first_cup", None)

    if first_cup is None:
        raise InvalidYearCupError("First cup date must be provided")

    first_cup_year = int(first_cup.split("-")[0])

    # Validar títulos negativos
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    # Validar se a primeira copa é um ano válido
    if first_cup_year < 1930:
        raise InvalidYearCupError("there was no world cup this year")

    # Verificar se o ano é um ano de Copa válido (1930, 1934, etc.)
    if (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    # Calcular o máximo de títulos possíveis
    current_year = datetime.datetime.now().year
    max_titles = (current_year - first_cup_year) // 4 + 1

    if titles > max_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
