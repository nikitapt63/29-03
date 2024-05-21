def check_annotations(func):
    def wrap(a, b):
        print(func.__annotations__)
        c = func(a, b)
        return c
    return wrap


@check_annotations
def main(a: str, b: int) -> str:
    return a * b


print(main("hi", 2))
