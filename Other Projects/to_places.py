from geopy.distance import geodesic

def travelling_distance():
    print("Starting program")
    count = int(input("Enter the number of places you would want to visit: "))
    places_to_visit = []  # Store places
    coordinates = {}  # Store coordinates
    
    for _ in range(count):
        place = input("Enter the town you want to visit: ")
        try:
            latitude = float(input("Enter the latitude of {}: ".format(place)))
            longitude = float(input("Enter the longitude of {}: ".format(place)))
        except ValueError:
            print("Invalid coordinates. Please enter numeric values.")
            return
        
        places_to_visit.append(place)  # Add place to the list
        coordinates[place] = (latitude, longitude)  # Assign coordinates to the place
    
    print("You are visiting:", ", ".join(places_to_visit))  # Print the list of places
    
    current_index = 0  # Initialize the current index to the first place
    
    while True:
        menu_options = input("""Available actions (select word or letters):
                             (N)ext
                             (B)ackward
                             (L)ist Places
                             (D)istance to Place
                             (M)enu
                             (Q)uit: """)
        
        if menu_options == "Next" or menu_options == "N":
            current_index = (current_index + 1) % len(places_to_visit)
            print("Next place:", places_to_visit[current_index])
        elif menu_options == "Backward" or menu_options == "B":
            current_index = (current_index - 1) % len(places_to_visit)
            print("Previous place:", places_to_visit[current_index])
        elif menu_options == "List Places" or menu_options == "L":
            print("Places:", ", ".join(places_to_visit))
        elif menu_options == "Distance to Place" or menu_options == "D":
            place = input("Enter the place to check the distance: ")
            if place in coordinates:
                current_coordinates = coordinates[places_to_visit[current_index]]
                destination_coordinates = coordinates[place]
                
                try:
                    distance = geodesic(current_coordinates, destination_coordinates).kilometers
                    print("Distance from {} to {} is approximately {} kilometers.".format(
                        places_to_visit[current_index], place, distance))
                except ValueError:
                    print("Error calculating distance. Please check the coordinates.")
                    
            else:
                print("Place not found.")
        elif menu_options == "Menu" or menu_options == "M":
            print("Menu:", menu_options)
        elif menu_options == "Quit" or menu_options == "Q":
            print("Program ending")
            break  # Exit the while loop to end the program
        else:
            print("Invalid option, please try again")

travelling_distance()