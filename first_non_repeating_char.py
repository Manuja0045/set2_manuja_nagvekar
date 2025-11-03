from collections import Counter

def first_non_repeating_char(s):
    if not s:
        return ""

    freq = Counter(s)  

    
    for ch in s:
        if freq[ch] == 1:
            return ch
    return ""  



if __name__ == "__main__":
    tests = {
        "swiss": "w",
        "aabbcc": "",
        "aabcc": "b",
        "": "",
        "x": "x",
        "teeter": "r",
        "redivider": "v"
    }

    
    print("FIRST NON-REPEATING CHARACTER TEST RESULTS ")
    print("------------------------------------------------------------")
    print(f"{'Input String':<15} | {'Output':<10} | {'Expected':<10} | {'Status'}")
    print("------------------------------------------------------------")

    for s, expected in tests.items():
        result = first_non_repeating_char(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{s!r:<15} | {result!r:<10} | {expected!r:<10} | {status}")

    print("All tests executed successfully.")
