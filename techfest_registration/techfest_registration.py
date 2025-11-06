# Registration Setup
print("Welcome to SMIT TechFest!")
print("Event organized by Ann Gutierrez of APPDAET BTCS1")

num_participants = int(input("How many participants will register?: "))
if num_participants <= 0:
    print("Invalid number of participants.")

# Collect Participant Information
else:
    participants = []
    for i in range(num_participants):
        print(f"Participant #{i+1}: ")
        name = input("Enter Participant Name: ")
        track = input("Enter Chosen Track: ")

        participant = {"name": name, "track": track}
        participants.append(participant)

    print("\nRegistered Participants:")
    for i in range(len(participants)):
        print(f"{i+1}. {participants[i]['name']} - {participants[i]['track']}")

# Track Diversity Report