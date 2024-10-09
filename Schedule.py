def create_schedule():
    empty_schedule = {"parent name": [], "phone": [], "date": [], "day": [], "hour": [], "city": [],
                      "comments": [], "volunteer": []}
    return empty_schedule

def add_request_line(schedule, request):
    schedule["parent name"].append(request[0])
    schedule["phone"].append(request[1])
    schedule["date"].append(request[2])
    schedule["day"].append(request[3])
    schedule["hour"].append(request[4])
    schedule["city"].append(request[5])
    schedule["comments"].append(request[6])

