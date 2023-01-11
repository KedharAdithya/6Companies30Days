class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))

        if numerator % denominator == 0:
            return "".join(res)

        res.append(".")
        remainder_pos = {}
        remainder = numerator % denominator
        while remainder:
            if remainder in remainder_pos:
                res.insert(remainder_pos[remainder], "(")
                res.append(")")
                break
            remainder_pos[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
