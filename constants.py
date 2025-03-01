SECRET: str = "punk"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False

    if idx < len(word):

        if word[idx] != secret[idx]:
            print(f"{word[idx]}isnt the secret words next letter.")
            return False
        else:
            print(
                f"{word[idx]} is at index [idx] for both words! Checking next letters..."
            )
            return guess_secret(word=word, secret=secret, idx=idx + 1)

    # TODO 3: If every pair of letters has ben the same and there are no letters left to check,
    # print "They are the same word" and return True

    print("They are the same word!")
    return True
