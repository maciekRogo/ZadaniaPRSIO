"""Napisz prosty dekorator timing_decorator , który będzie mierzył czas wykonania funkcji.
Zastosuj go do funkcji slow_function() , która wykonuje operację trwającą kilka sekund
(np. time.sleep(3) ), aby wyświetlić, ile czasu zajmuje jej wykonanie."""
import time

def timing_decorator(func):
    def wrapper():
        start = time.perf_counter()
        print(f"Przed wywołaniem funkcji")
        func()
        end = time.perf_counter()
        print(f"Po wywołaniu funkcji {end-start}")

    return wrapper
@timing_decorator
def slow_function():
    time.sleep(3)

slow_function()