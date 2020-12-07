total_hour, total_min, total_sec, get_min, get_sec = 0, 0, 0, 0, 0

while True:

    time = input("\n강의시간을 입력하세요. \n : ")
    if time == "reset":
        total_hour, total_min, total_sec = 0, 0, 0
        print("############################")
        print("###시간이 리셋되었습니다.###")
        print("############################")
    else:
        input_min = int(time[:2])
        input_sec = int(time[2:])
        if input_min >= 0 and input_sec >= 0 and input_min < 60 and input_sec < 60:
            total_min += input_min
            total_sec += input_sec

            if total_sec >= 60:
                total_sec -= 60
                total_min += 1

            if total_min >= 60:
                total_min -= 60
                total_hour += 1

            if total_min < 10:
                get_min = "0" + str(total_min)
            else:
                get_min = str(total_min)

            if total_sec < 10:
                get_sec = "0" + str(total_sec)
            else:
                get_sec = str(total_sec)

            print(f"총 플레이 타임은 {total_hour}:{get_min}:{get_sec} 입니다.")
        else:
            print("시간값 오류")