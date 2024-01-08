# COMP.CS.100 listan indeksien läpikäyminen
# Tekijä: Oona Leivo
# Opiskelijanumero: 150872052

"""
COMP.CS.100 Programming 1
A program that saves points to a file and then counts the total points, try-except
"""

def main():
    filename = input("Enter the name of the score file: ")

    try:
        points_file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    # an empty dict at the beginning
    points_book = {}

    # Populate the dictionary, until the file has been processed.
    for line in points_file:
        s = line.split()

        # if there's no two str:s separated by a space
        if len(s) != 2:
            temp = line.replace('\n', '')
            print(f"There was an erroneous line in the file:\n{temp}")
            return

        name, points = s[0], s[1]
        # change to int so we can add points together
        try:
            points = int(points)
        except ValueError:
            print(f"There was an erroneous score in the file:\n{points}")
            return

        # add to the points dict
        if name not in points_book:
            points_book[name] = points
        else:
            points_book[name] += points

    points_file.close()

    print("Contestant score:")

    for i in sorted(points_book):
        print(i, points_book[i])

if __name__ == '__main__':
    main()