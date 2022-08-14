#!/usr/bin/env python3

from statistics import mean
from tabulate import tabulate

data = [
    90, 30, 13, 67, 85, 87, 50, 45, 51, 72,
    64, 69, 59, 17, 22, 23, 44, 25, 16, 67,
    85, 87, 50, 45, 51, 72, 59, 14, 50, 55,
    32, 23, 24, 25, 37, 28, 39, 30, 33, 35,
    40, 34, 41, 43, 94, 95, 98, 99, 44, 45,
    47, 48, 49, 53, 61, 63, 69, 75, 77, 60,
    83,
]


def calculate_total_student_marks(input_data: list[int]) -> int:
    """
        Take in a list of numbers and return the sum of that list
        :param input_data: A list of numbers
        :return total_student_marks: A sum of all integers in the list
    """
    return len(input_data)


def calculate_lowest_and_highest_marks(input_data: list[int]) -> dict[str, int]:
    """
        Takes in a list of numbers and returns the lowest and highest value from that list of numbers
        :param input_data: A list of numbers
        :return: a dictionary with the keys lowest and highest and values respective to description from list
    """
    return {"highest": max(input_data), "lowest": min(input_data)}


def calculate_the_average_mark(input_data: list[int]) -> float:
    """
        Takes in a list of number and calculates the average of these numbers
        :param input_data: A list of numbers
        :return: a floating point number to two decimal places that is the average of your supplied list of numbers
    """
    return round(mean(input_data), 2)


def calculate_mark_bands(input_data: list[int]) -> list[list[str, int, str]]:
    """
        Takes in a list of numbers and will then return a list of list for each band
        :param input_data: A list of number
        :return mark_weights: a list containing lists of the band, scores at that band and the asterix string
    """
    mark_weights_data = {
        "0-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0,
        "51-60": 0,
        "61-70": 0,
        "71-80": 0,
        "81-90": 0,
        "91-100": 0,
    }

    for i in input_data:
        if 0 <= i <= 10:
            mark_weights_data["0-10"] += 1
        elif 11 <= i <= 20:
            mark_weights_data["11-20"] += 1
        elif 21 <= i <= 30:
            mark_weights_data["21-30"] += 1
        elif 31 <= i <= 40:
            mark_weights_data["31-40"] += 1
        elif 41 <= i <= 50:
            mark_weights_data["41-50"] += 1
        elif 51 <= i <= 60:
            mark_weights_data["51-60"] += 1
        elif 61 <= i <= 70:
            mark_weights_data["61-70"] += 1
        elif 71 <= i <= 80:
            mark_weights_data["71-80"] += 1
        elif 81 <= i <= 90:
            mark_weights_data["81-90"] += 1
        elif 91 <= i <= 100:
            mark_weights_data["91-100"] += 1

    mark_weights = []
    for i in mark_weights_data:
        mark_weights.append([i, mark_weights_data[i], f'{"*" * mark_weights_data[i]}'])

    return mark_weights


def draw_scores_table(input_data: list[list[str, int, str]]) -> str:
    """
        Takes in a list containing list of data and will return a string that is a table
        :param input_data: a list of lists of test scores based on bands [[band, scores at that band, asterix],]
        :return scores_table : A string containing bands,
    """

    col_names = ["Mark", "Count", " "]
    table_content = (tabulate(input_data, headers=col_names, tablefmt="fancy_grid"))
    return table_content


def calculate_pass_mark(raw_data: list[int]) -> int:
    required_students_to_pass = round(((len(raw_data) / 100) * 60), 0)
    score_data = raw_data.copy()
    score_data.sort()
    pass_mark = 0
    for index, value in enumerate(score_data):
        if index == required_students_to_pass:
            pass_mark = round(value / 10) * 10
    return pass_mark


if __name__ == "__main__":
    total_students: int = calculate_total_student_marks(data)
    print(f"The total amount of students who took the tests was: {total_students}")

    lowest_and_highest_marks: dict[str, int] = calculate_lowest_and_highest_marks(data)
    print(f"The lowest mark was: {lowest_and_highest_marks['lowest']}\n"
          f"The highest mark was: {lowest_and_highest_marks['highest']}")

    average_mark: float = calculate_the_average_mark(data)
    print(f"The average mark of the students was: {average_mark}")

    scores_and_bands: list[list[str, int, str]] = calculate_mark_bands(data)

    table = draw_scores_table(scores_and_bands)
    print(table)

    passing_mark = calculate_pass_mark(data)
    print(f"The passing mark is {passing_mark}")
