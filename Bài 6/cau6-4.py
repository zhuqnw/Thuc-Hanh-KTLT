print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

class RomanToInt:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total

# Ví dụ sử dụng
converter = RomanToInt()
print(converter.roman_to_int('IX'))  # Đầu ra: 9
print(converter.roman_to_int('MCMXCIV'))  # Đầu ra: 1994
