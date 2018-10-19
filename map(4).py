room_reception = {
    #Name of the room
    "name": "Reception",

    #Description of the room
    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    #Dictionary containing all exits
    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"} 
}

room_admins = {
    #Name of the room
    "name": "MJ and Simon's room",

    #Description of the room
    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    #Dictionary containing all exits
    "exits": {"north": "Reception"}
    
}

room_tutor = {
    #Name of the room
    "name": "your personal tutor's office",

    #Description of the room
    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    #Dictionary containing all exits
    "exits": {"west": "Reception"}
}

room_parking = {
    #Name of the room
    "name": "the parking lot",

    #Description of the room
    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    #Dictionary containing all exits
    "exits": {"east": "Office", "south": "Reception"}
}

room_office = {
    #Name of the room
    "name": "the general office",

    #Description of the room
    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    #Dictionary containing all exits
    "exits": {"west": "Parking"}
}



rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
