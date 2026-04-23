def enter_garage(garage, car_id, entry_hour):
    if len(garage["cars"]) >= garage["capacity"]: 
        raise ValueError
    if car_id in garage["cars"]:
        raise ValueError
    if (not type(entry_hour) is int):
        raise TypeError
    garage["cars"][car_id] = entry_hour
    return True

def exit_garage(garage, car_id):
    del garage["cars"][car_id]
    return True

def get_available_spots(garage):
    return garage["capacity"] - len(garage["cars"])