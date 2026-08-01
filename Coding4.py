# ask agent for details
name = input("Enter your name, agent:")
gadget = input("Enter your faviurite Gadget:")

#agent details
agent_no = 15
height_m = 175 
speed_rating = 8.8
mission_count = 19
is_active = False

# print each detail along with its datatype
print("Name:",name,"type:",type(name))
print("Gadget:",gadget,"type:",type(gadget))
print("Agent No:",agent_no,"type:",type(agent_no))
print("Height in metres:",height_m,"type:",type(height_m))
print("Speed Rating:",speed_rating,"type:",type(speed_rating))
print("Mission count:",mission_count,"type:",type(mission_count))
print("Is Active:",is_active,"type:",type(is_active))

agent_no_text = str(agent_no)
height_m_text = str(height_m)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
status_text= str(is_active)

print("Agent No as text:",agent_no,"type:",type(agent_no_text))
print("Height in metres as text:",height_m,"type:",type(height_m_text))
print("Speed Rating as text:",speed_rating,"type:",type(speed_rating_text))
print("Mission count as text:",mission_count,"type:",type(mission_count_text))
print("Status as text:",is_active,"type:",type(status_text))

