def format_days(d):
    if 11 <= d % 100 <= 14:
        return f"{d} days"
    elif d % 10 == 1:
        return f"{d} day"
    elif 2 <=d % 10 <= 4:
        return f"{d} days"
    else:
        return f"{d} days"

def convert(sec):
    d, rem1 = divmod(sec, 86400)
    h, rem2 = divmod(rem1, 3600)
    m, s = divmod(rem2, 60)
    return f"{format_days(d)}, {str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"
seconds = int(input("Enter a seconds: "))
if 0 <= seconds <= 8640000:
    print(convert(seconds))
else:
    print("ERROR!")