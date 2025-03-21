def double(x):
    print("Now in name 1")
    return 2*x
print("__name__:",__name__)

if __name__ == "__main__":
    a = double(20)
    print(a)