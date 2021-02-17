# Numba

Compile python functions to make your code faster.

Can play somewhat nicely with Awkward Arrays.

## Examples

```python
import numba as nb

energy = np.random.normal(100, 10, 1000000)
px = np.random.normal(0, 10, 1000000)
py = np.random.normal(0, 10, 1000000)
pz = np.random.normal(0, 10, 1000000)

# Numba lets us compile a function to compute a whole formula in one step.
@nb.jit
# Or
@nb.njit  # Faster.

# Create a function, but don't yet compile.
@nb.
def compute_mass(energy, px, py, pz):
    mass = np.empty(len(energy))
    for i in range(len(energy)):
        mass[i] = np.sqrt(energy[i]**2 - px[i]**2 - py[i]**2 - pz[i]**2)
    return mass
# It will be compiled when called.
compute_mass(energy, px, py, pz)

# When to use nb.vectorize?
@nb.vectorize

# Jim says: A decorator just sends a function to a function
```

## Resources

https://indico.cern.ch/event/985350/
