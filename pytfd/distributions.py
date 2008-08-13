_distributions = ['stft', 'sm', 'pwd', 'wd']

for _dist in _distributions:
    _module = __import__('pytfd.%s'%_dist, globals(), locals(), [''])
    globals()[_dist] = getattr(_module, _dist)

__all__ = _distributions
