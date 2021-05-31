from src.create_folds import create_folds


def main():
    print("What do you want?")
    print("1. Create Kfold")
    case = int(input("Choice: "))
    switch(case)


def switch(case):
    switcher = {1: create_folds}
    func = switcher.get(case, lambda: print("Not valid argument"))
    func()


if __name__ == "__main__":
    main()
