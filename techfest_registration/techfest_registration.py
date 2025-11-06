# Registration Setup
print("Welcome to SMIT TechFest!")
print("Event organized by Ann Gutierrez of APPDAET BTCS1")

num_participants = int(input("How many participants will register?: "))
if num_participants <= 0:
    print("Invalid number of participants.")

# Collect Participant Information
else:
    participants_list = []
    for i in range(num_participants):
        print(f"Participant #{i+1}: ")
        name = input("Enter Participant Name: ")
        track = input("Enter Chosen Track: ")
        participants_list.append({"name": name, "track": track})

    print("\nRegistered Participants:")
    count = 1
    for p in participants_list:
        print(f"{count}. {p['name']} - {p['track']}")
        count = count + 1

# Track Diversity Report

tracks = set()
for p in participants_list:
    tracks.add(p['track'])

print("\nTracks Offered in this Event:")
print(", ".join(tracks))

if len(tracks) < 2:
    print("Not enough variety in tracks.")

# Duplicate Name Detection
participant_names = set()
check_duplicates = set()

for p in participants_list:
    name = p['name']
    if name in participant_names:
        check_duplicates.add(name)
    else:
        participant_names.add(name)

if check_duplicates:
    for name in check_duplicates:
        print(f"\nDuplicate name found: {name}")
else: print("No duplicate names.")


