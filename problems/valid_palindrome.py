import argparse
import re


def is_palindrome(self, s: str) -> bool:

    # 특수문자 및 공백 제거
    s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

    # 뒤집힌 char 집합 생성
    chars = list(s)
    chars.reverse()

    # 뒤집힌 문자열 생성
    s_reverse = "".join([char for char in chars])

    return s == s_reverse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a sentence or sentences palindrome")
    parser.add_argument("string", required=True, tyep=ascii, help="string to validate")

    args = parser.parse_args()
    print("Is it palindrome?", is_palindrome(args.string))
