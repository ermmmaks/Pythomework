def sum_args(*args):
    return sum(args)

def curry(func, arity):
    if arity < 0:
        raise ValueError("Арность должна быть неотрицательной")

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        
        def next_curried(*next_args):
            return curried(*args, *next_args)
        return next_curried
    
    return curried

def uncurry(curried_func, arity):
    if arity < 0:
        raise ValueError("Арность должна быть неотрицательной")
    
    def uncurried(*args):
        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried

