import exrex


def passwordGen():
    password = exrex.getone("[A-Z][a-z]{7}\d{2}")
    return password
