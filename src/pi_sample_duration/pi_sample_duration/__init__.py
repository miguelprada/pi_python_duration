from .version import __version__
from .compute_duration import compute_duration, store_result
# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
    'compute_duration',
    'store_result',
]
