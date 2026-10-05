"""
Program: Word Count (Lab 10)
Author: bjohnston14 (cet)
Purpose: Present a menu of text files, read the selected file, count the
        frequency of every word, and print an alphabetical report.
        Supports an optional list of "stop words" to exclude.
Starter code: None. Written from the Lab 10 assignment description.
Date: 2026-10-04
"""

import string
from pathlib import Path

# Bird Analyzer
class WordAnalyzer:

    def __init__(self, filepath, stop_words=None):
        self.__filepath = Path(filepath)
        self.__frequencies = {}
        self.__stop_words = set(stop_words) if stop_words else set()

    def process_file(self):
        ret = True
        table = str.maketrans("", "", string.punctuation)
        try:
            if self.__filepath.exists():
                with self.__filepath.open("r", encoding="utf-8-sig") as file:
                    for line in file:
                        for word in line.translate(table).lower().split():
                            if word not in self.__stop_words:
                                self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            else:
                raise FileNotFoundError(self.__filepath)
        except FileNotFoundError:
            print(f"Error: '{self.__filepath}' was not found.")
            ret = False
        return ret

    def print_report(self):
        for word in sorted(self.__frequencies.keys()):
            print(f"{word:<7}:: {self.__frequencies[word]}")

def main():
    files = {
        "1": Path("monte_cristo.txt"),
        "2": Path("princess_mars.txt"),
        "3": Path("Tarzan.txt"),
        "4": Path("treasure_island.txt"),
    }
    exit_choice = str(len(files) + 1)

    while True:
        print("--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key, path in files.items():
            print(f"{key}. {path.stem.replace('_', ' ').title()}")
        print(f"{exit_choice}. Exit")
        print()

        choice = input(f"Enter your choice (1-{exit_choice}): ")
        print()

        if choice == exit_choice:
            print("Goodbye!")
            break

        if choice in files:
            path = files[choice]
            print(f"Processing '{path.name}'...")
            print()
            analyzer = WordAnalyzer(path)
            if analyzer.process_file():
                analyzer.print_report()
        else:
            print(f"Invalid choice. Please select from 1-{exit_choice}.")

        print()
        input("Press Enter to return to the menu... ")
        print()

main()
