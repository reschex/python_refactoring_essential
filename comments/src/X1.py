class X1:

    @staticmethod
    def calculate_accumulated_sum_of_squares(start, end):
        accumulated_sum = 0

        for i in range(start, end + 1):
            accumulated_sum += X1.calculate_square(i)

        return accumulated_sum

    @staticmethod
    def calculate_square(num):
        return num * num
