def gen_lst_and_tpl (nums):
    lst = nums.split (',')
    tpl = tuple (lst)

    print (lst, tpl)


nums = input ("Enter the numbers with comma between them\n==> ")
gen_lst_and_tpl (nums)



# Another Solution


def lst_tpl ():
    values=input()
    l=values.split(",")
    t=tuple(l)

    print(l)
    print(t)


lst_tpl ()