def fu(v1=None):
    if not getattr(fu, "v", None):
        fu.v = v1
    return fu.v


print(fu())
print(fu(5))
print(fu())
