from math import sqrt

class MathModule:

    @staticmethod
    def solve_equation(a, b, c) -> str:
        discr = MathModule._find_discriminant(a,b,c)

        if discr < 0:
            return "Сожалеем, но действительных корней у ур-ия нет"
        if discr == 0:
            solution = (-b + sqrt(discr))//2*a
            return "Корень уравнения: " + str(solution)
        if discr > 0:
            first_solution = (-b + sqrt(discr))//2*a
            second_solution = (-b - sqrt(discr))//2*a
            return "Корни уравнения: " + str(first_solution) + "и" + str(second_solution)

    @staticmethod
    def _find_discriminant(a, b, c):
        return b ** 2 - 4 * a * c