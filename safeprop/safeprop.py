# -*- coding: utf-8 -*-

from itertools import tee

from CoolProp.CoolProp import PhaseSI, PropsSI
from CoolProp.HumidAirProp import HAPropsSI
from numpy import nan

from .nomenclature import AirProperties, RefProperties


air = AirProperties()
ref = RefProperties()


# Define constants used throughout calculations.
P_ATM = 101325.


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def safe_round(x, ndigits=0):
    """Function used by approximate memoizer to round numerical values."""
    try:
        return round(x, ndigits)
    except TypeError:
        return x


def approximate_memoize(options):
    """Parameterized decorator used to memoize refprop calls."""
    def decorator(function):
        cache = function.cache = {}

        def wrapper(*args, **kwargs):
            """Caches a functions output by storing approximate arguments."""
            args = tuple(args[0]) + tuple(
                safe_round(b, options.get(a, 0)) for a, b in pairwise(args)
            )
            if args not in cache:
                cache[args] = function(*args, **kwargs)
            return cache[args]
        wrapper.__doc__ = function.__doc__
        wrapper.__name__ = function.__name__
        return wrapper

    return decorator


def set_option(*options):
    """Parameterized decorator used to set last arguments of functions."""
    def decorator(function):
        def wrapper(*args, **kwargs):
            args += options
            return function(*args, **kwargs)
        wrapper.__doc__ = function.__doc__
        wrapper.__name__ = function.__name__
        return wrapper
    return decorator


@approximate_memoize({air.T: 3, air.P: 0, air.R: 4, air.H: 1, air.W: 4})
@set_option(air.P, P_ATM)
def airprop(*args):
    """Wrapper for HumidAirProp.HAPropsSI function that catches exceptions.

    Rarely, the HumidAirProp.HAPropsSI humid air property calculation
    method fails to converge at random states (presumably due to numerical
    solver errors). In order to prevent the FDD algorithm from stopping due
    to one of these thrown exceptions, the original function is wrapped in
    a try-except statement.  When a ValueError exception is thrown by
    HAPropsSI, a NaN is returned instead.

    """
    try:
        return HAPropsSI(*args)
    except ValueError:
        return nan


@approximate_memoize({ref.T: 3, ref.P: 0, ref.Q: 4, ref.H: 1, air.D: 2})
@set_option('R410A')
def refprop(*args):
    """Wrapper for CoolProp.PropsSI function that catches exceptions.

    Rarely, the CoolProp.PropsSI humid air property calculation
    method fails to converge at random states (presumably due to numerical
    solver errors). In order to prevent the FDD algorithm from stopping due
    to one of these thrown exceptions, the original function is wrapped in
    a try-except statement.  When a ValueError exception is thrown by
    PropsSI, a NaN is returned instead.

    """
    try:
        return PropsSI(*args)
    except ValueError:
        return nan


@approximate_memoize({ref.T: 3, ref.P: 0})
@set_option('R410A')
def phase(*args):
    """Wrapper for CoolProp.PhaseSI function that catches exceptions.

    Rarely, the CoolProp.PhaseSI humid air property calculation
    method fails to converge at random states (presumably due to numerical
    solver errors). In order to prevent the FDD algorithm from stopping due
    to one of these thrown exceptions, the original function is wrapped in
    a try-except statement.  When a ValueError exception is thrown by
    PhaseSI, a NaN is returned instead.

    """
    try:
        return PhaseSI(*args)
    except ValueError:
        return nan
