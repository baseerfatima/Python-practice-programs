def dat(year):
    if year<=1917:
        if year%4==0:
            print(f"13.09.{year}")
        else:
            print(f"11.09.{year}")
    if year==1918:
        print(f".09.{year}")
    