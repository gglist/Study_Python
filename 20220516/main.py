# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

languages=['python', 'perl', 'c', 'java', 'c++']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    for lang in languages:
        if lang in ['python', 'perl']:
            print("%6s need interpreter" % lang)
        elif lang in ['c', 'java']:
            print("%6s need compiler" % lang)
        else:
            print("should not reach hear %s" % lang)
    grade = {"국어":80, "영어":75, "수학":55}
    sum = 0;
    num = 0;
    for value in grade.values():
        sum += value
        num += 1
        print("%d : %d sum %d" %(num, value, sum))
    avg = sum / num
    print("average is %d" %avg)

    jumin = "881120-1068234"
    birth = jumin[:jumin.find('-')]
    id = jumin[jumin.find('-') + 1:]
    print("birthday is %s" %birth)
    print("id is %s" % id)

    li = ['Life', 'is', 'too', 'short']
    print("%s" % (" ".join(li)))

    a = "Life is too short, you need python"

    if "wife" in a:
        print("wife")
    elif "python" in a and "you"  in a:
        print("python")
    elif "shirt" not in a:
        print("shirt")
    elif "need" in a:
        print("need")
    else:
        print("none")

    hight = 100
    bound = 3/5

    for val in range(10):
        hight = hight * bound
        print(round(hight, 4))

    number = 358

    rem = rev = 0
    while number >= 1:
        rem = number % 10
        rev = rev * 10 + rem
        number = number // 10

    print(rev)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
