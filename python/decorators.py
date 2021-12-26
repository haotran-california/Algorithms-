#DECORATORS
def double_result(fn):
    def wrapper(*args):
        total = 0
        for i in args:
            total += i * 2
        return total

    return wrapper

def only_even_parameters(fn):
    def wrapper(*args):
        for arguement in args:
            if arguement % 2 != 0:
                return ("This function only takes even parameters")
        return fn(*args)

    return wrapper

def log(fn):
    def wrapper(*args):
        file = "dataLog.txt"
        log = open(file, "a")
        query = ""
        for i in args:
            query += str(i) + " "
        log.write(query + "\n")
        return fn

    return wrapper

def timer(fn):
    import time
    def wrapper(*args):
        t1 = time.time()
        print("This timer has started")
        result = fn(*args)
        print(result)
        t2 = time.time()
        time_elapsed = t2 - t1
        print("The time elapsed is ", time_elapsed)
        return result
    return wrapper

#howto set float with an unknown number of arguments
def set_float(fn):
    def wrapper(*args):
        parameters = []
        for i in args:
            parameters.append(float(i))
        return fn(parameters)
    return wrapper

def inital(fn):
    def wrapper(*args):
        result = fn(*args)
        fn.init = True
        if fn.init == True:
        return result
    return wrapper

#higher order function
def html_tag(tag):
    def wrapper(msg):
        return tag + msg + tag
    return wrapper


@inital
def add(a, b, c):
    return a + b + c

result = add(10, 12, 14)


# intro = html_tag("<h1>")
# intro_body = intro("Hello this is the beginning of my essay")
# print(intro_body)
