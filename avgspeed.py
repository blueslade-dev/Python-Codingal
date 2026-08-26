a = 10
b = 20
c = 30
avg = (a+b+c)/3
if avg > a and avg > b and avg>c:
    print(f"All are cycling slower than {avg}km/h")
elif avg>a and avg>b:
    print(f"Cyclists a and b are cycling slower than {avg}km/h")
elif avg>a and avg>c:
    print(f"Cyclists a and c are cycling slower than {avg}km/h")
elif avg>a:
    print(f"Cyclists a is cycling slower than {avg}km/h")
elif avg> b and avg>c:
    print(f"Cyclists b and c are cycling slower than {avg}km/h")
elif avg>b:
    print(f"Cyclist b is cycling slower than {avg}km/h")
elif avg>c:
    print(f"Cyclist c is cycling slower than {avg}km/h")

