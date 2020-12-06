total_hour = 0
total_min = 0
total_sec = 0

while True:

    time = input("시간을 입력하세요. \n : ")
    total_min += int(time[:2])
    print(total_min)
    total_sec += int(time[2:])
    print(total_sec)

    if total_sec >= 60:
        total_sec -= 60
        total_min += 1

    if total_min >= 60:
        total_min -= 60
        total_hour += 1

    if total_min < 10:
        total_min = "0" + str(total_min)

    if total_sec < 10:
        total_sec = "0" + str(total_sec)

    print(f"총 플레이 타임은 {total_hour}:{total_min}:{total_sec} 입니다.")