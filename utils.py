from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):
    try:
        titles = data.get("titles", 0)
        first_cup_year = int(data.get("first_cup", "").split("-")[0])

        if titles < 0:
            raise NegativeTitlesError()

        if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
            raise InvalidYearCupError()

        max_possible_titles = (2024 - first_cup_year) // 4 + 1
        if titles > max_possible_titles:
            raise ImpossibleTitlesError()

        return "Data processing successful."
    except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
        raise e
