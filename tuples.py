def get_coordinate(record):

    return record[1]


def convert_coordinate(coordinate):

    number = coordinate[0]
    letter = coordinate[1]

    return (number, letter)


def create_record(azara_record, rui_record):

    treasure_coordinate = get_coordinate(azara_record)
    location_coordinate = get_coordinate(rui_record)

    if convert_coordinate(treasure_coordinate) == location_coordinate:
        return azara_record + rui_record

    else:
        return "not a match"

    
