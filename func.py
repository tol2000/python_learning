print("\nOur gen_dec definition")


def gen_dec(x):
    print(f"In a gen_dec with {x}")

    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        print("Generated a wrapper")
        return wrapper

    print("Generated a decorator")
    return decorator


print("\nOur mul definition")


@gen_dec(42)
def mul(a, b):
    return a * b


print("\nOur mul running")

print(mul(3, 4))
