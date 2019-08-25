attendees = ["Ken", "Aleena", "Greg"]

print("There are", len(attendees), "attendees currently.")

attendees.append("Josh")

print("There are", len(attendees), "attendees currently.")

attendees_extra = ["Paul", "Garya", "Jo"]

attendees.extend(attendees_extra)

print("There are", len(attendees), "attendees currently.")

#make new list from 2
all_guests = attendees + attendees_extra

print(all_guests)