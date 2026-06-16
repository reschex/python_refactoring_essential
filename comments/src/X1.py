class X1:

    @staticmethod
    def m(start, end):
        p = 0

        # Iterate from lower bound (q) to upper bound (z)
        for i in range(start, end + 1):
            # Add square of each number in the range
            p += X1.n(i)

        # Return accumulated sum
        return p

    @staticmethod
    def n(k):
        # Return square of input
        return k * k