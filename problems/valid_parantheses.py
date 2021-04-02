def valid_parantheses(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in pairs:
            stack.append(char)
        elif not stack or pairs[char] != stack.pop():
            return False

    return len(stack) == 0
