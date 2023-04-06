# 1 Radian = 180Degrees


def rad_deg(rad):
    deg = rad * 180
    return f"{deg} Degrees"

rad = int(input("Enter your value in radian(s)\n==> "))
print(rad_deg(rad))