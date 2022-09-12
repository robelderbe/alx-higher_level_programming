#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    count = 0
=======
     count = 0
>>>>>>> 2f479ab9cc953e599ab4e5772bb870bc594187c1

        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
            except:
                break
            else:
                count += 1

        print()
        return (count)
