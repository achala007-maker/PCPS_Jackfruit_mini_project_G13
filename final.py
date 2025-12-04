import tkinter as tk
from tkinter import ttk
import sys
import subprocess # to call another python file
import time

def popup():

    home = tk.Tk()
    home.configure(bg="#FFD1DC")
    home.geometry("300x200+500+250")#"widthxheight+x_offset+y_offset"
    home.overrideredirect(True)#create a frameless window

    # frame that will sit in the center
    center_frame = tk.Frame(home, bg="#FFD1DC")
    center_frame.pack(expand=True)

    label = tk.Label(center_frame, text="Initialising Map system",
                     font=("Courier", 15), bg="#FFD1DC")
    label.pack(pady=(0, 2))

    label2 = tk.Label(center_frame, text="........",
                      font=("Courier", 15), bg="#FFD1DC")
    label2.pack(pady=0)

    home.after(1000, home.destroy)#1000milliseconds=1sec
    home.mainloop()

def main_screen():
    
    root = tk.Tk()
    root.title("4Directions")
    root.geometry("600x550+350+50")#"widthxheight+x_offset+y_offset"
    root.configure(bg="#FFD1DC")

    ## data
    places = {}
    with open("Campus_Data_2.csv") as f:
        f.readline() #Removes header
        d1=f.readlines() #List of lines
        line=[]
        for i in d1:
            line=[j.strip() for j in i.strip().split(",")] #Removes space, splits based on comma, stores elements as a list
            if line[0] not in places: #If the place name of a given line does not already exist in the dictionary a new one is created and an empty list is assigned
                places[line[0]]=[]
            places[line[0]].append((line[1],int(line[2]),line[3])) #The block ,floor of the place, name of the place is appended to the list
        #print(places)#Debugging code

    # Load distances
    with open("Campus_Distance_2.csv") as a:
        a.readline()
        d2=a.readlines()
        dist=[]
        lis=[]
        for i in d2:
            lis=[j.strip() for j in i.strip().split(",")]
            dist.append([lis[0],lis[1],float(lis[2])])

    floors = {
        "GJBC": list(range(-3, 9)),               
        "F BLOCK": list(range(0, 11)),             
        "OAT": [0],                                    
        "BE BLOCK": list(range(0, 14)),            
       
        "ENTRANCE": [0]
    }
    # Getting ALL place names for dropdown
    place_names = []
    for place_list in places.values():#Get's list of tuple's
        for _, _, name in place_list:#Unpacking the tuple
            place_names.append(name)
    place_names = list(set(place_names))  # Remove duplicates

    # elements
    title_label = tk.Label(root, text="Select using the dropdown menu:))",
                           bg="#FFD1DC", fg="#E91E63", font=("Arial", 18))
    title_label.pack(pady=20)

    main_frame = tk.Frame(root, bg="#FFD1DC")
    main_frame.pack()

    result_label = tk.Label(root, text="", bg="#FFD1DC", fg="#E91E63",
                            font=("Arial", 14), wraplength=500)
    result_label.pack(pady=25)

    # variables
    chosen_block = tk.StringVar()
    chosen_floor = tk.StringVar()
    chosen_place = tk.StringVar()

    # block dropdown
    block_label = tk.Label(main_frame, text="Select the Block you are in:", bg="#FFD1DC", fg="#E91E63",
                           font=("Arial", 14))
    block_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    block_dropdown = ttk.Combobox(main_frame, values=list(floors.keys()), width=40,
                                  textvariable=chosen_block)
    block_dropdown.grid(row=0, column=1, padx=10, pady=10)

    # floor dropdown
    floor_label = tk.Label(main_frame, text="Select the you are in Floor:", bg="#FFD1DC", fg="#E91E63",
                           font=("Arial", 14))
    floor_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    floor_dropdown = ttk.Combobox(main_frame, width=40, textvariable=chosen_floor)
    floor_dropdown.grid(row=1, column=1, padx=10, pady=10)

    # destination dropdown
    place_label = tk.Label(main_frame, text="Select your Destination:", bg="#FFD1DC", fg="#E91E63",
                           font=("Arial", 14))
    place_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    place_dropdown = ttk.Combobox(main_frame, values=list(places.keys()), width=40,
                              textvariable=chosen_place)
    place_dropdown.grid(row=2, column=1, padx=10, pady=10)

    # functions
    def update_floors(event):
        block = chosen_block.get()
        if block in floors:
            floor_dropdown["values"] = floors[block]

    def get_path_number(start_block, dest_block):#Getting path number for the turtle code 
        paths = {
            ("ENTRANCE", "F BLOCK"): 1,
            ("ENTRANCE", "GJBC"): 2,
            ("ENTRANCE", "BE BLOCK"): 3,
            ("ENTRANCE", "OAT"): 4,
            ("F BLOCK", "GJBC"): 5,
            ("F BLOCK", "ENTRANCE"): 6,
            ("F BLOCK", "OAT"): 7,
            ("F BLOCK", "BE BLOCK"): 8,
            ("GJBC", "ENTRANCE"): 9,
            ("GJBC", "F BLOCK"): 10,
            ("GJBC", "BE BLOCK"): 11,
            ("GJBC", "OAT"): 12,
            ("BE BLOCK", "ENTRANCE"): 13,
            ("BE BLOCK", "F BLOCK"): 14,
            ("BE BLOCK", "GJBC"): 15,
            ("BE BLOCK", "OAT"): 16,
            ("OAT", "ENTRANCE"): 17,
            ("OAT", "F BLOCK"): 18,
            ("OAT", "GJBC"): 19,
            ("OAT", "BE BLOCK"): 20,
        }
        return paths.get((start_block, dest_block))

    def show_location():
        #Input-variables       
        current_block= chosen_block.get()
        current_floor=int(chosen_floor.get())
        selected = chosen_place.get()
        
        #print(f"selected='{selected}', type={type(selected)}")#Debugging code
        
        #---ALGORITHM FOR SHORTEST PATH/ FINDING DESTINATION LOCATION---
        min_dis=max(i[2] for i in dist) #Here i refers to the list of two blocks and the distance, i[2] is the value of the distance
        block_dis=0
        block=""
        floor_same=[]
        floor_diff={}
        min_floor=0  #Stores the FINAL floor
        place_name="" #Stores the place name
        flag=False

        for i in places[selected]:#Assuming that the place that the user enters EXACTLY matches the key.Here values are a list of tuples and hence iterable
            if i[0]==current_block: #This checks whether the place needed is already in the users block if so that is the nearest
                block=current_block
                floor_same.append([i[1],i[2]])
                flag=True
            elif flag==False:
                for j in dist: #Now j is a list of two blocks and the distance between them
                    if current_block in j and i[0] in j:
                        block_dis=j[2] #This holds the distance of the users block and the block considering A canteen not necassarily the nearest
                if block_dis<=min_dis:
                    min_dis=block_dis
                    block=i[0]
        if flag==True:
            difference=abs(floor_same[0][0]-current_floor)
            for i in floor_same:
                if abs(i[0]-current_floor)<=difference:
                    min_floor=i[0]
                    difference=abs(i[0]-current_floor)
                    place_name=i[1]
        else:
        
            for i in places[selected]: #Appends the floor and place name of desired location ONLY from final block
                if i[0]==block:
                    floor_diff[i[1]]=[i[2]]
            min_floor=min(list(floor_diff.keys()))
            place_name=floor_diff[min_floor]

            # Checking if inital block==destination block
        if current_block != block:
            result_label.config(
                text=f"Required Location: {place_name}\nLocated on floor {min_floor} of {block} block\n\n Different block detected - launching campus map...")

            #print("DEBUG start_block:", repr(current_block), "dest_block:", repr(block))
            path_num = get_path_number(current_block, block)
            #print("DEBUG  path_num:", path_num)

            if path_num is not None:
                #print("DEBUG : calling turtle!!!!") 
                subprocess.Popen([sys.executable, 'campuswalk.py', str(path_num)])
        
        else:
            result_label.config(
            text=f"Required Location: {place_name}\nSame block- Go to floor{min_floor}!")

    block_dropdown.bind("<<ComboboxSelected>>", update_floors)

    submit_btn = tk.Button(root, text="Show Result", width=20, bg="#FFD1DC", fg="#E91E63",
                           command=show_location)
    submit_btn.pack(pady=10)


    root.mainloop()
popup()
main_screen()
