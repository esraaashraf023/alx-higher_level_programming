#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
a = 10
b = 5
r = add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, r))
    r = sub(a, b)
     print('{:d} - {:d} = {:d}'.format(a, b, r))
     r = mul(a, b)
      print('{:d} * {:d} = {:d}'.format(a, b, r))
      r = div(a, b)
       print('{:d} / {:d} = {:d}'.format(a, b, r))
