import datetime


def create_schedule():
    new_schedule = {"parent name": ["Alma", "Ana", "Avi"],
                    "phone": [5014452973, 5012345443, 5312938883],
                    "date": [datetime.date(2024, 12, 6), datetime.date(2024, 10, 20), datetime.date(2024, 10, 14)],
                    "day": ["friday", "sunday", "monday"],
                    "hour": ["8:00", "13:00", "20:00"],
                    "city": ["Tel Aviv", "Petah Tikva", "Ramat Gan"],
                    "comments": ["3 children, 4, 5, 8", "1 child, 10 months", "2 children, 2, 6"],
                    "volunteers": ["sign up now!", "sign up now!", "sign up now!"]}
    return new_schedule


def add_request_line(schedule, request):
    schedule["parent name"].append(request[0])
    schedule["phone"].append(request[1])
    schedule["date"].append(request[2])
    schedule["day"].append(request[3])
    schedule["hour"].append(request[4])
    schedule["city"].append(request[5])
    schedule["comments"].append(request[6])
    schedule["volunteers"].append("sign up now!")


def remove_past_events(schedule):
    for i in schedule["date"]:
        if i < datetime.date.today():
            schedule["date"].remove(i)
