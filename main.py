def check_annotations(func):
    def wrap(a, b):
        types = func.__annotations__
        if not isinstance(a, types['a']):
            return False
        c = func(a, b)
        return c
    return wrap


@check_annotations
def main(a: str, b: int) -> str:
    return a * b


print(main("hi", 2))
