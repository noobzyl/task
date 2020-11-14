class Solution():
    def int_to_roman(self, num):
        c = {0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
             1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
             2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
             3: ["", "M", "MM", "MMM"]}
        roman = []
        roman.append(c[3][(num // 1000) % 10])
        roman.append(c[2][(num // 100) % 10])
        roman.append(c[1][(num // 10) % 10])
        roman.append(c[0][num % 10])
        s = ''
        for i in roman:
            s = s + i
        return s


if __name__ == '__main__':
    a = Solution()
    arabic_numerals = int(input("请输入需要转换的数字："))
    result = a.int_to_roman(arabic_numerals)
    print(f'{arabic_numerals}转换成罗马数字的结果是{result}')
