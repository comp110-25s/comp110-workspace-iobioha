def count_to_n(n: int) -> None:
    count: int = 0
    while count <= n:
        print(f"Count is:{count}")
        count = count + 1


count_to_n(n=4)
