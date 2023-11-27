import cmath
import math


class InvalidSidesOfTriangleError(Exception):
    __module__ = Exception.__module__


class MissingRequiredAttributeError(Exception):
    __module__ = Exception.__module__


def convert_complex_to_float(number: complex):
    """
    Convert Complex to Float function :-
        This function converts complex numbers to float numbers.
    """
    numberStr = str(number)
    if not numberStr == "0j":
        if not number.real == 0.0:
            return float(number.real)
        else:
            return float(number.imag)
    else:
        return float(0)


def calculate_basic(what: str, number_1, number_2):
    """
    Basic calculation function :-
        This function calculates some basic calculation and return it.

        !!! Parameters !!! what -> What to be calculated. Must be 'add' for addition, 'sub' for subtraction,
        'mul' for multiplication, 'div' for division, 'pow' for power and 'mod' for modulo. -> Must be a string.
        number_1 -> First number. -> Must be float or int. number_2 -> Second number. -> Must be float or int.
    """
    number_1, number_2 = float(number_1), float(number_2)
    if what.lower() == "add":
        return number_1 + number_2

    elif what.lower() == "sub":
        return number_1 - number_2

    elif what.lower() == "mul":
        return number_1 * number_2

    elif what.lower() == "div":
        return number_1 / number_2

    elif what.lower() == "pow":
        return number_1 ** number_2

    elif what.lower() == "mod":
        return number_1 // number_2

    else:
        raise AttributeError(
            f"""Attribute 'what' must be 'add', 'sub', 'mul', 'div', 'pow' or 'mod' and not '{what}'.""")


def calculate_infinite(what: str, *value):
    """
    Calculate Infinite function :-
        This function calculates infinite addition and infinite multiplication

        !!! Parameters !!!
        what -> What to calculate. Must be 'sum' for addition or 'mul' for multiplication. -> Must be str.
        value -> Value to be calculated. Can be as many as you want.
    """
    for j in value:
        int(j)
    if what == "mul":
        res = 1
        for i in value:
            res *= i
        return res

    elif what == "sum":
        res = 0
        for i in value:
            res += i
        return res
    else:
        raise AttributeError(
            f"""Attribute 'what' must be 'sum' or 'mul' and not '{what}'.""")


def invert_value(value):
    """
    Invert value function :-
        This function inverts the number given and returns it.

        !!! Parameters !!!
        value -> Value to be inverted. -> Must be float or int.
    """
    value = float(value)
    return -value


def calculate_accuracy(actual_value, approx_value):
    error_rate = ((actual_value - approx_value) / approx_value) * 100
    return {"accuracy": 100 - error_rate, "error_rate": error_rate}


def calculate_interest(what: str, principle: float, rate: float, time: int):
    """
    Calculate Simple or Compound Interest function :-
        This function calculates Simple as well as Compound Interest.

        !!! Parameters !!!
        what -> What to calculate. Must be 'simple' or 'compound'. -> Must be str.
        principle -> Principle or Initial amount. -> Must be float.
        rate -> Rate of Interest. Must be less than 100 -> Must be float.
        time -> Interval of time. -> Must be in months and int.
    """
    principle = float(principle)
    rate = float(rate)
    time = int(time)

    if rate > 100:
        raise ValueError("Attribute 'rate' must be less than 100.")
    if what.lower() == "simple":
        simple_interest = (principle * rate * time) / 100
        amount = simple_interest + principle
        res = {f'Simple Interest : {simple_interest}', f'Amount : {amount}'}
        return res

    elif what.lower() == "compound":
        amount = principle * (((1 + rate) / 100) ** time)
        compound_interest = amount - principle
        return {f'Compound Interest': {compound_interest}, f'Amount': {amount}}

    else:
        raise AttributeError(
            f"Attribute 'what' should be 'simple' or 'compound' and not '{what}'")


def calculate_lcm(number_1: int, number_2: int):
    """
    Calculate LCM (The Lowest Common Multiple) function :-
        This function calculates the LCM (The Lowest Common Multiple) of two numbers.

        !!! Parameters !!!
        number_1 -> First number. -> Must be int
        number_2 -> Second number. -> Must be int
    """
    return math.lcm(int(number_1), int(number_2))


def calculate_profit_loss(what: str, **kwargs):
    """
    Calculate Profit or Loss or Profit(in %) or Loss(in %) function:-
        This function calculates profit, loss, profit(in %), loss(in %) of kwargs.
    """
    what = what.lower()
    if what == "profit":
        if "selling_price" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
            return float(kwargs["selling_price"]) - float(kwargs["cost_price"])
        else:
            raise MissingRequiredAttributeError(
                f"Attribute 'selling_price' or 'cost_price' is missing.")
    elif what == "loss":
        if "selling_price" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
            return float(kwargs["cost_price"]) - float(kwargs["selling_price"])
        else:
            raise MissingRequiredAttributeError(
                f"Attribute 'selling_price' or 'cost_price' is missing.")
    elif what == "profit%":
        if "profit" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
            return (float(kwargs["profit"]) / float(kwargs["cost_price"])) * 100
        else:
            if "selling_price" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
                profit = calculate_profit_loss("profit", selling_price=kwargs["selling_price"],
                                               cost_price=kwargs["cost_price"])
                return calculate_profit_loss("profit%", cost_price=kwargs["cost_price"], profit=profit)
            else:
                raise MissingRequiredAttributeError(
                    f"Attribute 'selling_price' or 'cost_price' is missing.")
    elif what == "loss%":
        if "loss" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
            return (float(kwargs["loss"]) / float(kwargs["cost_price"])) * 100
        else:
            if "selling_price" in list(kwargs.keys()) and "cost_price" in list(kwargs.keys()):
                loss = calculate_profit_loss("loss", selling_price=kwargs["selling_price"],
                                             cost_price=kwargs["cost_price"])
                return calculate_profit_loss("loss%", cost_price=kwargs["cost_price"], loss=loss)
            else:
                raise MissingRequiredAttributeError(
                    f"Attribute 'selling_price' or 'cost_price' is missing.")
    else:
        raise AttributeError(
            f"Attribute 'what' should be 'profit' or 'loss' or 'profit%' or 'loss%' and not '{what}'")


def calculate_sin_cos_tan(radians, what: str):
    """
    Calculate Sin, Cos, Tan function :-
        This function calculates Sin, Cos and Tan of attribute 'radians'.

        !!! Parameters !!!
        radians -> Radians of which the corresponding value of attribute 'what' is to be found.
        what -> What to be calculated. Must be 'sin', 'cos' or 'tan'. -> Must be in str.
    """
    radians = float(radians)
    if what.lower() == "sin":
        return math.sin(radians)
    elif what.lower() == "cos":
        return math.cos(radians)
    elif what.lower() == "tan":
        return math.tan(radians)
    else:
        raise AttributeError(
            f"Attribute 'what' must be 'sin', 'cos' or 'tan' and not '{what}'.")


def calculate_sqrt(number: float, returnStr: str):
    """
    Calculate Square Root function :-
        This function calculates the Square Root of the number given.

        !!! Parameters !!!
        number -> Number to be calculated. -> Must be float.
    """
    number = float(number)
    return cmath.sqrt(number) if not returnStr else f"Square Root of {str(number)} is {str(cmath.sqrt(number))}"


def calculate_area_of_circle(number: float, returnStr: str):
    """
    Calculate Area of Circle function :-
        This function calculates the Area of Circle of the number given.

        !!! Parameters !!!
        number -> Number to be calculated. -> Must be float.
    """
    number = float(number)
    return cmath.pi * (
            number ** 2) if not returnStr else f"Area of Circle with radius {str(number)} is " \
                                               f"{str(cmath.pi * (number ** 2))}"


def calculate_circumference_of_circle(number: float, returnStr: str):
    """
    Calculate Area of Circle function :-
        This function calculates the Area of Circle of the number given.

        !!! Parameters !!!
        number -> Number to be calculated. -> Must be float.
    """
    number = float(number)
    return 2 * cmath.pi * number if not returnStr else f"Circumference of Circle with radius {str(number)} is " \
                                                       f"{str(2 * cmath.pi * number)}"


def calculate_perimeter_of_rect(width: float, height: float):
    """
    Calculate Perimeter of Rectangle function :-
        This function calculates the Perimeter of Rectangle of the width and height given.

        !!! Parameters !!!
        width -> Width of the rectangle. -> Must be float.
        height -> Height of the rectangle. -> Must be float.
    """
    width = float(width)
    height = float(height)
    return 2 * (width + height)


def calculate_area_of_rect(width: float, height: float):
    """
    Calculate Area of Rectangle function :-
        This function calculates the Area of Rectangle of the width and height given.

        !!! Parameters !!!
        width -> Width of the rectangle. -> Must be float.
        height -> Height of the rectangle. -> Must be float.
    """
    width = float(width)
    height = float(height)
    return width * height


def calculate_area_of_triangle(base, height):
    """
    Calculate Area of Triangle function :-
        This function calculates Area of Triangle.

        !!! Parameters !!!
        base -> Length of Base of a triangle.
        height -> Length of the height of a triangle.
    """
    return (float(base) * float(height)) * 2


def check_valid_triangle_with_sides(side_1, side_2, side_3):
    """
    Check if the given sides can form a triangle function :-
        This function checks if the given sides can form a triangle.

        !!! Parameters !!!
        side_1 -> Length of first side. -> Must be float.
        side_2 -> Length of second side. -> Must be float.
        side_3 -> Length of third side. -> Must be float.
    """
    side_1, side_2, side_3 = float(side_1), float(side_2), float(side_3)
    if side_1 == side_2 == side_3:
        return True
    if side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        return True
    for i in range(1, 180):
        third_side = round(math.sqrt(side_1 ** 2 + side_2 ** 2 - 2. * side_1 * side_2 * math.cos(math.radians(i))),
                           2)
        if third_side == side_3:
            return True
    return False


def calculate_area_of_triangle_with_sides(side_1, side_2, side_3):
    """
    Calculate area of triangle with three sides function:-
        This function calculates the area of triangle with given three sides.

        !!! Parameters !!!
        side_1 -> Length of first side
        side_2 -> Length of second side
        side_3 -> Length of third side
    """
    if check_valid_triangle_with_sides(side_1, side_2, side_3):
        side_1, side_2, side_3 = float(side_1), float(side_2), float(side_3)
        sPerimeter = (side_1 + side_2 + side_3) / 2
        return (sPerimeter * (sPerimeter - side_1) * (sPerimeter - side_2) * sPerimeter - side_3) ** 0.5
    else:
        raise InvalidSidesOfTriangleError(
            f"Triangle with sides {side_1}, {side_2} and {side_3} is not possible")


def calculate_volume_of_cuboid(width, height, length):
    """
    Calculate Volume of Cube or Cuboid function :-
        This function calculates the volume of cube or cuboid.

        !!! Parameters !!!
        width -> Width of Cube or Cuboid
        height -> Height of Cube or Cuboid
        length -> Length of Cube or Cuboid
    """
    return float(width) * float(height) * float(length)


def calculate_volume_of_cylinder(radius, height):
    """
    Calculate Volume of Cylinder function :-
        This function calculates the volume of cylinder.

        !!! Parameters !!!
        radius -> Radius of the cylinder.
        height -> Height of the cylinder.
    """
    radius = float(radius)
    height = float(height)
    return math.pi * radius * radius * height


def calculate_angle_of_polygon(what: str, no_of_sides: int):
    """
    Calculate Angle of Polygon function :-
        This function calculates the angle of any polygon.

        !!! Parameters !!!
        what -> What to calculate. Must be 'sum of interior angles', 'each interior angle' or 'each exterior angle'. ->
        Must be str
        no_of_sides -> Number of sides of the polygon.
    """
    if what.lower() == 0:
        return (int(no_of_sides) - 2) * 180

    elif what.lower() == 1:
        return ((int(no_of_sides) - 2) * 180) / int(no_of_sides)

    elif what.lower() == 2:
        return 360 / int(no_of_sides)

    else:
        raise AttributeError(
            f"Attribute 'what' must be 0, 1 or 2 and not '{what}'.")


def calculate_factorial(to):
    """
    Calculate Factorial function :-
        This function calculates the factorial to the given number and returns it.

        !!! Parameters !!!
        to -> The number to the factorial is to be found. Means '1*2*3*...*n' where n is the attribute 'to'. ->
        Must be int.

        Note:-
            If the attribute 'to' is a negative number, it will return 1.
    """
    to = int(to)
    if to > 99999:
        raise AttributeError("Attribute 'to' must be less than 100000.")
    res = 1
    for i in range(1, to + 1):
        res *= i

    return res


def calculate_average(*value):
    """
    Calculate Average function :-
        This function calculates average.

        !!! Parameters !!!
        value -> Value to be calculated. Can be as many as you want.
    """
    b = []
    c = 0
    for i in value:
        b.append(i)

    for a in b:
        c += float(str(a))
    return c / len(b)


def calculate_num_of_notes(amount: float | int, notes: list[int]):
    """
    Calculate Num of Notes function:-
        This function calculates the number of notes against given amount.

        !!! Parameters !!!
        amount -> The amount -> Must be float or int
        notes -> The notes to be used.
    """
    amount = float(amount)
    notes = list(notes)
    notes.sort(reverse=True)
    res = {}
    for i in notes:
        if amount >= i:
            res[str(i)] = int(amount // i)
            amount -= int(amount // i) * i
        else:
            res[str(i)] = 0
    res["remaining"] = amount
    return res


def calculate_fibonacci_series(to: int):
    """
    Calculate Fibonacci Series function:-
        This function calculater the fibonacci series to the 'to' argument
    :param to: To calculate the series to
    :return: int or float
    """
    f = [0, 1]
    for i in range(2, to+1):
        f.append(f[i - 1] + f[i - 2])
    return f


if __name__ == '__main__':
    print(calculate_fibonacci_series(0))
