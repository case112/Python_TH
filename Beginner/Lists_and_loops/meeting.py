attendees = ["Ken", "Aleena", "Greg"]
attendees.append("Josh")
attendees.extend(["Kyle", "Jo"])
optional_invitees = ["Bob", "Via"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potentional attendees currently.")

#to string
to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)

#back to list
to_line.split(", ")
print(to_line)