def log(sequence, message, *values):
    print(type(values))
    if not values:
            print(f"{sequence} - {message}")
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f"{sequence} - {message}: {values_str}")


log(1, "Favorites", 7, 33)
