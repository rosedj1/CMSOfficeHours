"""
PURPOSE:
  This code returns the value of integration when the User 
  specifies a function and the integration bounds. 
SYNTAX: python this_script.py
NOTES:  None.
AUTHOR: Jake Rosenzweig
CREATED:  2020-08-13
MODIFIED: 2020-08-13

Example:
    user_defined_function = 2 * sin(x)
    your_integrator(user_defined_function, 0, np.pi)  # (fn, x_min, x_max)
    # returns: 4.0
"""
import numpy as np
import argparse

#--- User-defined/Global variables. 
# x_min = 0.0
# x_max = np.pi
# def fn(x):
#     return 2 * np.sin(x)
fn = lambda x : 2 * np.sin(x)
# Use "left" corner, "right" corner, or "center" of top of rectangle for area calculation.

#--- Script functions.
def parse_options():
    """Your typical flag parser."""
    parser = argparse.ArgumentParser(description='Integration bounds')
    parser.add_argument('--x_min', dest='x_min', default=None, type=float, help='lower intgration bound')
    parser.add_argument('--x_max', dest='x_max', default=None, type=float, help='upper intgration bound')
    parser.add_argument('--n_rect', dest='n_rect', default=10000, type=int, help='number of rectangles')
    help_str = """'left', 'right', 'center' (part of rectangle that touches curve)"""
    parser.add_argument('--mode', dest='mode', default="center", type=str, help=help_str)
    args = parser.parse_args()
    return args

def unpack_flags():
    """Return a tuple of the User-specified flags."""
    args = parse_options()
    x_min = args.x_min
    x_max = args.x_max
    if x_min is None or x_max is None: 
        raise ValueError
    n_rect = args.n_rect
    mode = args.mode
    return (x_min, x_max, n_rect, mode)

def calc_area(width_arr, height_arr):
    """Sum the area of rectangles by doing width*height for each rectangle."""
    assert len(width_arr) == len(height_arr)
    return np.dot(width_arr, height_arr)

def get_width_arr(x_min, x_max, n_rect):
    """Divide the x-axis up into n_rect rectangles and store the width of each rectangle."""
    rect_width = (x_max - x_min) / n_rect
    rect_width_arr = np.ones(n_rect) * rect_width
    return rect_width_arr

def get_height_arr(x_min, x_max, fn, mode="center"):
    """
    User's choice of "mode" determines which part of top of rectangle to use for height.
    
    Parameters
    ----------
    x_vals : array of floats
        The bin edges of all rectangles.
    fn : ufunc
        A 1-dim User-defined function of x (like f(x)).

    Returns
    -------
    h_arr : array of floats
        The "heights" of the sides of each rectangle, based on mode chosen. 
        len(h_arr) = x_vals - 1
    """ 
    x = np.linspace(x_min, x_max, n_rect+1)      # Edges of rectangles. len = n_rect + 1

    if "left" in mode:
        x_vals = x[:-1]
    elif "right" in mode:
        x_vals = x[1:]
    elif "center" in mode:
        x_vals = (x[:-1] + x[1:]) / 2.0
    else: 
        raise ValueError(f"`mode` ({mode}) not understood.")
    h_arr = fn(x_vals)
    return h_arr

def integrate(fn, x_min, x_max, n_rect=10000, mode="center"):
    """
    Return the approximate area under a curve by summing thin rectangles.

    Parameters
    ----------
    fn : 1-dim function
        Your typical f(x) function. Examples: fn = np.sin(x), fn = x**2, fn = 1 / x
    x_min : float
        Lower bound of integration.
    x_max : float
        Upper bound of integration.
    n_rect : int, optional
        The number of rectangles used to calculate area.

    Returns
    -------
    area : float
        The approximate area under the curve.
    """
    assert n_rect > 0
    width_arr = get_width_arr(x_min, x_max, n_rect)
    height_arr = get_height_arr(x_min, x_max, fn, mode=mode) 
    area = calc_area(width_arr, height_arr)
    return area     

#--- When you do: python this_script.py, then this code will be run over:
if __name__ == "__main__":
    # This is the logical, sequential call to the main functions. 
    x_min, x_max, n_rect, mode = unpack_flags()
    area = integrate(fn, x_min, x_max, n_rect=n_rect)
    print(f"[INFO] Integral of function from x_min={x_min:.6f} to x_max={x_max:.6f} is: {area:.6f}")
    print(f"[INFO]   (Method chosen:   '{mode}')")
    print(f"[INFO]   (Rectangles used: '{n_rect}')")