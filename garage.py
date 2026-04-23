def enter_garage(garage, car_id, entry_hour):
    if len(garage["cars"]) >= garage["capacity"]: 
        raise ValueError
    if (not type(car_id) is int):
        raise ValueError
    garage["cars"].append(car_id)
    return True