# Code is pass is telling python that this function is empty,
# Indentation is important and the .format is
def format_position(lat, long):
    formatedPosition = "Lat: {} - Long: {}".format(lat, long)
    return formatedPosition
    # pass


def format_position1(lat, long):
    global pattern
    pattern = "Lat: {} - Long: {}"
    formattedPosition1 = pattern.format(lat, long)
    return formattedPosition1


# rint(test)
print(format_position(-52.33, 120.00))