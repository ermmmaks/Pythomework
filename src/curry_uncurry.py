def sum_args(*args):
    return sum(args)

def curry(func, arity):
    if arity < 1:
        raise ValueError("Арность должна быть положительной")

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        
        def next_curried(*next_args):
            return curried(*args, *next_args)
        return next_curried
    
    return curried

def uncurry(curried_func, arity):
    if arity < 1:
        raise ValueError("Арность должна быть положительной")
    
    def uncurried(*args):
        result = curried_func
        for arg in args:
            result = curried_func(arg)
        return result

    return uncurried
