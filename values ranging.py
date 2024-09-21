def number_to_words(num):
    if num < 1 or num > 999999999:
        return "Number out of range"

    # Define word representations for numbers
    below_20 = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    thousands = [
        "", "thousand", "million"
    ]

    def helper(n):
        if n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return below_20[n // 100] + " hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        else:
            return ""

    result = ""
    for i, scale in enumerate(thousands):
        if num % 1000 != 0:
            result = helper(num % 1000) + (" " + scale if scale else "") + (" " + result if result else "")
        num //= 1000
    
    return result.strip()

# Examples
print(number_to_words(1000))  # Output: 'one thousand'
print(number_to_words(4003))  # Output: 'four thousand three'
