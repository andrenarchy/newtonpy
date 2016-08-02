from numpy import abs


def newton(fun, grad, x0, tol=1e-8):
    x = x0
    while abs(fun(x)) > tol:
        x = x - fun(x) / grad(x)
    return x
