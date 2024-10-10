
community = {
    "Maani": ["Maayan Caspi" ,"0544724643" ,"woman" ,"18" ,"4"],
    "Mayush": ["Maya Livshits" ,"0502135049" ,"woman" ,"18" ,"2"],
    "Libbyyy" :["Libby Matsk" ,"0545678322" ,"woman" ,"18" ,"6"],
    "MyLightLior": ["Lior Hagai" ,"0548889471" ,"woman" ,"18" ,"3"]
}

def is_in_community(name):
    if(name in community.keys()):
        return True
    return False


def get_member_full_name(name):
    return community[name][0]

def get_member_phone_number(name):
    return community[name][1]

def get_member_gender(name):
    return community[name][2]

def get_member_age(name):
    return community[name][3]

def get_member_years_of_experience(name):
    return community[name][4]

def community_member_info(name):
    return ("community member: ", name, "\nfull name: ", community[name][0], "\nphone number: ", community[name][1],
            "\ngender: ", community[name][2], "\nage: ", community[name][3], "\nyears of experience: ",
            community[name][4])