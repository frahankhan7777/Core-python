try:
    a = 10
    b = 5
    c = a / b
    print("division:", c)
except ZeroDivisionError as e:
    print("exection:", e)

except ValueError:
    print("please number hi dal na hai")

except Exception as e:
    print("Exception:", e)
else:
    print("else block executed ")

finally:
    print("finally bloc executed")

