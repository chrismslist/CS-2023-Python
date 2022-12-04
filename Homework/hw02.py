def fixed_point_iteration(f, x=1.0):
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step

"""
def approx_fixed_point(f, x) should
return True if and only if f(x) is
very close (distance < 1e-15) to x.
"""