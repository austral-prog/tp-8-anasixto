def get_coordinate(record):

    return record[1]


def convert_coordinate(coordinate):

    number = coordinate[0]
    letter = coordinate[1]

    return (number, letter)


def create_record(azara_record, rui_record):

    treasure, treasure_coordinate = treasure_pair
    location, location_coordinate, quadrant = location_record

    formated_treasure_coordinate = convert_coordinate(treasure_coordinate)

    if formated_treasure_coordinate == location_coordinate:
        return treasure, tresure_coordinate, location, location_coordinate, quadrant
    else:
        return "not a match"
