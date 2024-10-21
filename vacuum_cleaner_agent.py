def vacuum_world():
    # Initializing goal_state
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    location_input = input("Enter Location of Vacuum (A or B): ").strip().upper()  # User input for location
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    status_input_complement = input("Enter status of other room (0 for Clean, 1 for Dirty): ").strip()

    print("Initial Location Condition:", goal_state)

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A:", cost)
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean.")

        if status_input_complement == '1':
            print("Location B is Dirty.")
            print("Moving right to Location B.")
            cost += 1  # cost for moving right
            print("COST for moving RIGHT:", cost)
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for SUCK:", cost)
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean.")

    elif location_input == 'B':
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for CLEANING:", cost)
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean.")

        if status_input_complement == '1':
            print("Location A is Dirty.")
            print("Moving left to Location A.")
            cost += 1  # cost for moving left
            print("COST for moving LEFT:", cost)
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("COST for SUCK:", cost)
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean.")

    # Done cleaning
    print("GOAL STATE:", goal_state)
    print("Performance Measurement:", cost)

# To run the vacuum world simulation:
vacuum_world()