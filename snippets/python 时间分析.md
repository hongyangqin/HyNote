# python 时间分析

```python
import cProfile
from time_profile import *
import pstats

cProfile.run("timeit_profile()", "timeit")
p = pstats.Stats('timeit')
p.sort_stats('time')
p.print_stats(6)
```

