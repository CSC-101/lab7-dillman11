import convert

def gather_numbers() -> list[float]:
    finish = ""
    floats = []
    while finish != "done":
        finish = input("Type a number and type done when finished: ")
        if convert.str_to_float(finish) != None:
            floats.append(convert.str_to_float(finish))
    return floats

if __name__ == '__main__':
    print(gather_numbers())