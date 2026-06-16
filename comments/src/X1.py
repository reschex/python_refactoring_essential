class X1:

    @staticmethod
    def calculate_accumulated_sum(start, end):
        acc_sum = 0

        for i in range(start, end + 1):
            acc_sum += X1.calculate_square(i)

        return acc_sum

    @staticmethod
    def calculate_square(num):
        return num * num
