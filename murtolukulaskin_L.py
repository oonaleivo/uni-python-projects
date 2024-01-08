# COMP.CS.100
# Tekijä: Oona Leivo
# Opiskelijanumero: 150872052

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions, does different things with given fractions
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """simplifies the fraction"""

        gcd = greatest_common_divisor(self.__numerator, self.__denominator)

        new_numerator = self.__numerator // gcd
        new_denominator = self.__denominator // gcd

        return Fraction(new_numerator, new_denominator)

    def complement(self):
        """returns the vastaluku of the fraction"""

        numerator = self.__numerator * -1
        denominator = self.__denominator

        complement_fraction = Fraction(numerator, denominator)

        return complement_fraction

    def reciprocal(self):
        """returns the käänteisluku of the fraction"""

        numerator = self.__denominator
        denominator = self.__numerator

        reciprocal_fraction = Fraction(numerator, denominator)

        return reciprocal_fraction

    def multiply(self, second_fraction):
        """calculates the multiplication of two fractions

        :param second_fraction: int, a given second fraction
        :return new_fraction: int, the result of the multiplication"""

        num_frac1 = self.__numerator
        num_frac2 = second_fraction.__numerator
        den_frac1 = self.__denominator
        den_frac2 = second_fraction.__denominator

        numerator = num_frac1 * num_frac2
        denominator = den_frac1 * den_frac2

        result = Fraction(numerator, denominator)

        return result

    def divide(self, second_fraction):
        """Divides first fraction with the given second fraction

        :param second_fraction: int, a given second fraction
        :return new fraction: int, the result of the division"""

        # let's define the method we'll need
        # sending the second factor to reciprocal method to get the käänteisluku
        reciprocal = second_fraction.reciprocal()

        frac1 = Fraction(self.__numerator, self.__denominator)
        # eli luku frac1 kerrotaan metodista reciprocal saadulla arvolla
        division = frac1.multiply(reciprocal)

        return division

    def add(self, second_fraction):
        """adds the two fractions together

        :param second_fraction: int, a given second fraction
        :return addition: lavennetut fractions added together
        """

        frac1 = Fraction(self.__numerator, self.__denominator)
        frac1_laventaja = Fraction(second_fraction.__denominator, second_fraction.__denominator)
        lavennettu_frac1 = frac1.multiply(frac1_laventaja)

        frac2_laventaja = Fraction(self.__denominator, self.__denominator)
        lavennettu_frac2 = second_fraction.multiply(frac2_laventaja)

        numerator = lavennettu_frac1.__numerator + lavennettu_frac2.__numerator
        denominator = lavennettu_frac2.__denominator

        fraction_after_addition = Fraction(numerator, denominator)

        return fraction_after_addition

    def deduct(self, second_fraction):
        """Calculates the difference between the two given fractions

        :param second_fraction: in, a given second fraction
        :return deduction: the difference between the two fractions"""

        frac1 = Fraction(self.__numerator, self.__denominator)
        frac1_laventaja = Fraction(second_fraction.__denominator,
                                   second_fraction.__denominator)
        lavennettu_frac1 = frac1.multiply(frac1_laventaja)

        frac2_laventaja = Fraction(self.__denominator, self.__denominator)
        lavennettu_frac2 = second_fraction.multiply(frac2_laventaja)

        numerator = lavennettu_frac1.__numerator - lavennettu_frac2.__numerator
        denominator = lavennettu_frac2.__denominator

        fraction_after_deduction = Fraction(numerator, denominator)

        return fraction_after_deduction

    def into_float(self):
        """
        Turn a fraction into a decimal number for comparing them.

        :return: float, fraction as decimal
        """
        to_float = self.__numerator / self.__denominator

        return "{:.3f}".format(to_float)

    def __str__(self):
        """prints in correct form"""

        return f"{self.__numerator}/{self.__denominator}"

    def __lt__(self, second_fraction):
        return self.into_float() < second_fraction.into_float()

    def __gt__(self, second_fraction):
        return self.into_float() > second_fraction.into_float()

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    dict_of_fractions = {}

    do_loop = True

    while do_loop:

        command = input("> ")

        if command == "add":
            """asks name and fraction from user and adds to dict"""
            fraction = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")
            numerator, denominator = fraction.split("/")
            dict_of_fractions[name] = Fraction(int(numerator),int(denominator))

        elif command == "print":
            """prints the fraction assigned to a given name"""
            name = input("Enter a name: ")
            if name in dict_of_fractions:
                print(f"{name} = {dict_of_fractions[name]}")
            else:
                print(f"Name {name} was not found")

        elif command == "list":
            """prints the whole list"""
            for name in sorted(dict_of_fractions):
                print(f"{name} = {dict_of_fractions[name]}")

        elif command == "*":
            """multiplies two fractions"""
            first_name = input("1st operand: ")
            if first_name not in dict_of_fractions:
                print(f"Name {first_name} was not found")
                continue

            second_name = input("2nd operand: ")
            if second_name not in dict_of_fractions:
                print(f"Name {second_name} was not found")
                continue

            else:
                first_name = dict_of_fractions[first_name]
                second_name = dict_of_fractions[second_name]

                # send to multiply method
                # print answer
                multiplication = first_name.multiply(second_name)
                print(f"{first_name} * {second_name} = {multiplication}")
                # simplify answer
                simp = multiplication.simplify()
                print(f"simplified {simp}")

        elif command == "file":
            """reads the fractions in the given file"""
            try:
                file_name = input("Enter the name of the file: ")
                file = open(file_name, mode="r")

                for line in file:
                    line = line.strip()
                    line = line.split("=")
                    # nimetään kaksi jaettua osaa
                    name = line[0]
                    fraction = line[1]
                    numerator, denominator = fraction.split("/")
                    new_fraction = Fraction(int(numerator), int(denominator))
                    # adding to dict
                    dict_of_fractions[name] = new_fraction

            except ValueError:
                print("Error: the file cannot be read.")

            except OSError:
                print("Error: the file cannot be read.")

        elif command == "quit":
            print("Bye bye!")
            do_loop = False
        else:
            print("Unknown command!")
            pass

if __name__ == "__main__":
    main()