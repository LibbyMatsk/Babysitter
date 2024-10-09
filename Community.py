
community = {
    "Maani": ["Maayan Caspi","0544724643","woman","18","4"],
    "Mayush": ["Maya Livshits","0502135049","woman","18","2"],
    "Libbyyy":["Libby Matsk","0545678322","woman","18","6"],
    "MyLightLior": ["Lior Hagai","0548889471","woman","18","3"]
}

def is_in_community(name):
    if(name in community.keys()):
        return True
    return False


def community_member_info(name):
        return ("community member: ",name,"  full name: ",community[name][0],"  phone number: ",community[name][1],
                "  gender: ", community[name][2],"  age: ", community[name][3],"  years of experience: ", community[name][4] )
   