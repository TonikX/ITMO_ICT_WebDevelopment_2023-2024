## Utility-функции

### Декоратор `threaded`

```python
def threaded(daemon: bool = False):
    def _threaded(func):
        def thread_wrapper(*args, **kwargs):
            t = Thread(target=func, args=args, kwargs=kwargs, daemon=daemon)
            t.start()
        return thread_wrapper
    return _threaded
```
Принимает параметр `daemon`, равный `False` по умолчанию. 
Далее запускает отдельный поток с декорируемой функцией