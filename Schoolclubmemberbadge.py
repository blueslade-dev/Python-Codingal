club_member_name = input("Enter your name:")
school_club_name = input("Enter your school club name:")

member_no = 5
pts_earned = 387
event_count = 88
meeting_hours = 2.5
is_active = True

print("Club Member name:",club_member_name,"type:",type(club_member_name))
print("School club name:",school_club_name,"type:",type(school_club_name))
print("Member number:",member_no,"type:",type(member_no))
print("Points earned:",pts_earned,"type:",type(pts_earned))
print("Event count:",event_count,"type:",type(event_count))
print("Metting Hours:",meeting_hours,"type:",type(meeting_hours))
print("Status:",is_active,"type:",type(is_active))

a = str(club_member_name)
b = str(school_club_name)
c = str(member_no)
d = str(pts_earned)
e = str(event_count)
f = str(meeting_hours)
g = str(is_active)

x = club_member_name[0:3]
y = club_member_name[-1::]
z = x + y

print("Badge code: ",z)
print("Secret club code: ", school_club_name[::-1])


print("Club Member name:",a)
print("School club name:",b)
print("Member number:",c)
print("Points earned:",d)
print("Event count:",e)
print("Meeting Hours:",f)
print("Status:",g)