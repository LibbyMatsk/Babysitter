List_of_evecuees = ["Eva", "Yuval", "Maya", "Emma", "Tom", "Avi"]
list_of_requests = []

def check_if_in_list(name):
    for name_of_evecuee in List_of_evecuees:
        if name == name_of_evecuee:
            return True
        else:
            return False


def create_array(name, phone, date, day, hours, city, comments):
    array = [name, phone, date, day, hours, city, comments]
    return array


def create_babysiter_request():
    pass