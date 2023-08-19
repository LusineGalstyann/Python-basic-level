# task 1

# to implement a difference function, which subtracts one list from another and returns the result.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]
# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    rezult = []
    for i in a:
        if i not in b:
            rezult.append(i)
    return rezult


# task 2
import math
def triangle_type(a, b, c):
    if (a+b>c and a+c>b and b+c>a):
        alpha = round(math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c))),3)
        betta = round(math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c))),3)
        gamma = round(math.degrees(math.acos((b * b - c * c + a * a) / (2 * b * a))),3)
        sum=alpha + betta + gamma
        print (sum)
        if round(sum)!=180:
            return 0
        elif (alpha == 90 or betta == 90 or gamma == 90):
            return 2
        elif alpha<90 and betta<90 and gamma<90:
            return 1
        elif (alpha>90 or betta>90 or gamma>90):
            return 3
    else:
        print("k")
        return 0

print(triangle_type(7,12,8))

