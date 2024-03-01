def my_sort(lst: list) -> list:
    new_lst = list()
    new_lst = sorted(lst,key=lambda x : sum([int(digit) for digit in str(x)]))
    return (new_lst)

user_lst = list()
num = int(input("How many numbers do you wanna enter? -> "))
for _ in range(num):
    try:
        n = int(input("n = "))
        assert(n > 0)
    except:
        print("Iltimos butun musbat son kiriting")
    else:
        user_lst.append(n)
print(user_lst)
print(my_sort(user_lst))
