def odometer(reading, reading_defect_at):
    diff_per_ten = 1  # 10-1
    diff_per_hundred = 19  # (10*10)-(9*9)
    diff_per_thousand = 271  # 19*9 + 100
    diff_per_ten_thousand = 3439  # 19*9*9 + 1000

    reading_list = list(str(reading))
    actual_reading = 0

    for counter, value in enumerate(reading_list):
        single_reading = int(value)

        if int(value) >= reading_defect_at:
            actual_reading -= (10 ** len(reading_list[counter + 1:]))
            single_reading -= 1

        actual_reading += int(reading_list[counter]) * (10 ** len(reading_list[counter + 1:]))

        if len(reading_list[counter + 1:]) == 1:
            actual_reading -= single_reading * diff_per_ten
        elif len(reading_list[counter + 1:]) == 2:
            actual_reading -= single_reading * diff_per_hundred
        elif len(reading_list[counter + 1:]) == 3:
            actual_reading -= single_reading * diff_per_thousand
        elif len(reading_list[counter + 1:]) == 4:
            actual_reading -= single_reading * diff_per_ten_thousand

    print(actual_reading)


ODOMETER_DEFECT_AT = 4
ODOMETER_READING = 56287

odometer(ODOMETER_READING, ODOMETER_DEFECT_AT)


###
# Sample Results
# 100 - 81
# 399 - 323
# 599 - 404
# 56287 - 30120
###
