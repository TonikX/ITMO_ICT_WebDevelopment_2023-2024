def LocateCalculate(data):
    if data[2] == 0:
        return (data[0] ** 2 + data[1] ** 2) ** 0.5
    elif data[1] == 0:
        return (data[2] ** 2 - data[0] ** 2) ** 0.5
    return (data[2] ** 2 - data[1] ** 2) ** 0.5

def CheckMessage(data):
    try:
        val_tuple = tuple(map(int, data.split()))
    except ValueError:
        print('Something went wrong with input')
        return False
    for i in val_tuple:
        if i < 0:
            print('Sides can not be negative')
            return False
    if (val_tuple[2] <= val_tuple[1] or val_tuple[2] <= val_tuple[0]) and val_tuple[2] != 0:
        print('Hypothenus can not be shorter than cathetus')
        return False
    return val_tuple