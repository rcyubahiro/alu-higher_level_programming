#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result_list.append(0)
                continue
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not isinstance(num1, (int, float)) or not isinstance(
                num2, (int, float)
            ):
                print("wrong type")
                result_list.append(0)
                continue
            if num2 == 0:
                print("division by 0")
                result_list.append(0)
                continue
            result_list.append(num1 / num2)
        except Exception as e:
            print("error:", e)
            result_list.append(0)
        finally:
            continue
    return result_list
