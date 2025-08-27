# dictionary of rooms, their valid directions, and items contained
room_map = {
    'Foyer': {'East': 'Great Hall', 'North': 'Carport'},
    'Carport': {'East': 'Guest House', 'South': 'Foyer', 'Item': 'Bloody Tire Iron'},
    'Great Hall': {'North': 'Guest House', 'South': 'Kitchen', 'West': 'Foyer', 'East': 'Master Bedroom',
                   'Item': 'Polaroid'},
    'Guest House': {'South': 'Great Hall', 'West': 'Carport', 'East': 'Boat House', 'Item': 'Wallet'},
    'Boat House': {'West': 'Guest House', 'Item': 'Half Smoked Cigarette'},
    'Kitchen': {'North': 'Great Hall', 'West': 'Library', 'East': 'Bathroom', 'Item': "Guest List"},
    'Library': {'East': 'Kitchen', 'Item': 'Confession Letter'},
    'Bathroom': {'West': 'Kitchen', 'North': 'Master Bedroom', 'Item': 'Bloody Sweater'},
    'Master Bedroom': {'West': 'Great Hall', 'South': 'Bathroom', 'Item': 'Body'}
}