name = input("Name: ")
marks = int(input("marks: "))


if marks in range(80,100):
    print(f"Hi {name}.Well done by getting {marks}%,you achieved an A")
elif marks >=70:
    print(f"Hi {name}.By getting {marks}%,You achieved a B")
elif marks >=50:
    print(f"Hi {name}.You perfomed averagely by getting {marks}%,You got a C")
elif marks <=49:
    print(f"Hi {name}.By getting {marks}%,you got a D.You should improve")