# s = "abcabcbb"
# s = "dvdf"
s = "pwwkew"
strings = ["pwwkew", "bbbbb", "dvdf", "abcabcbb", "asjrgapa"]
for s in strings:
    window = ""
    longest = 0
    for char in s:
        if char in window:
            start = window.rfind(char)
            longest = max(longest, start)
            if start == len(window):
                window = []
            else:
                window = window[start + 1:]
        window += char
        longest = max(longest, len(window))
    print(longest)