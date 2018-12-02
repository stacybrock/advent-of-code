# 2015 Day 4 Notes

I got stuck for _way_ too long on this puzzle due to some ignorance about `hashlib`'s `update()` method.

This code does not work as expected:
```python3
secret_key = 'abcdef'
number = 1
md5 = hashlib.md5()
while True:
    md5.update(f"{secret_key}{number}".encode())
    md5hash = md5.hexdigest()
    if md5hash.startswith('00000'):
        return (number, md5hash)
    number += 1
```

The reason is that successive calls to `update()` **add** to the input of previous calls. Let's hear it [from the source](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest):

> `hash.update(data)`

> Update the hash object with the bytes-like object. Repeated calls are equivalent to a single call with the concatenation of all the arguments: `m.update(a); m.update(b)` is equivalent to `m.update(a+b)`.
