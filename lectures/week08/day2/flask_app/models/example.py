"""
# Magical Alchemist Game

# Game Description:
# In this whimsical adventure, players take on the role of a magical alchemist navigating enchanted gardens
# to gather humorous herbs and create delightful potions. Each location offers unique ingredients, and once
# a combination is collected, the Potion Brewery becomes available, allowing players to brew potions with
# unexpected and comical effects. Essence points are earned or lost based on successful potion brewing and
# amusing outcomes.

"""

# List of Locations with IDs
locations = [
    {"id": 1, "name": "Herb Haven"},
    {"id": 2, "name": "Giggle Grove"},
    {"id": 3, "name": "Enchanted Meadow"},
    {"id": 4, "name": "Crystal Orchards"}
]

# List of Herbs with IDs, Corresponding Location IDs, and Essence Points
herbs = [
    {"id": 1, "name": "Mystical Mint", "location_id": 1, "essence_points": 3},
    {"id": 2, "name": "Laughing Lavender", "location_id": 1, "essence_points": 2},
    {"id": 3, "name": "Ticklish Thistle", "location_id": 2, "essence_points": 4},
    {"id": 4, "name": "Joyful Jasmine", "location_id": 2, "essence_points": 5},
    {"id": 5, "name": "Giggling Gillyweed", "location_id": 1, "essence_points": 3},
    {"id": 6, "name": "Whimsical Whisker Hairs", "location_id": 2, "essence_points": 2},
    {"id": 7, "name": "Silly Sproutlings", "location_id": 3, "essence_points": 4},
    {"id": 8, "name": "Enchanted Evergreen", "location_id": 3, "essence_points": 3},
    {"id": 9, "name": "Crystalized Cactus", "location_id": 4, "essence_points": 5},
    {"id": 10, "name": "Mystic Marigold", "location_id": 4, "essence_points": 4}
]

# List of Potions with IDs, Containing Ingredients, and Essence Points
potions = [
    {"id": 1, "name": "Levity Elixir", "ingredients": [{"Mystical Mint": 1}, {"Laughing Lavender": 2}], "essence_points": 10},
    {"id": 2, "name": "Serious Silliness Syrup", "ingredients": [{"Ticklish Thistle": 3}, {"Joyful Jasmine": 4}], "essence_points": 15},
    {"id": 3, "name": "Euphoria Emanation Elixir", "ingredients": [{"Giggling Gillyweed": 5}, {"Whimsical Whisker Hairs": 6}], "essence_points": -5},
    {"id": 4, "name": "Gleeful Glitter Goblet", "ingredients": [{"Silly Sproutlings": 7}, {"Enchanted Evergreen": 8}], "essence_points": 8},
    {"id": 5, "name": "Crystal Clear Calm", "ingredients": [{"Crystalized Cactus": 9}, {"Mystic Marigold": 10}], "essence_points": 12}
]

# List of Potential Potion Outcomes with IDs and Essence Points
outcomes = [
    {"id": 1, "name": "Joyful Jiggle Jamboree", "essence_points": 8},
    {"id": 2, "name": "Serene Chuckle Cascade", "essence_points": 5},
    {"id": 3, "name": "Levitation Libation", "essence_points": 12},
    {"id": 4, "name": "Silly Spectacle Spill", "essence_points": -3},
    {"id": 5, "name": "Giggly Glitch Geyser", "essence_points": -8},
    {"id": 6, "name": "Chuckling Critter Conundrum", "essence_points": -10},
    {"id": 7, "name": "Whimsical Whirlwind", "essence_points": 15},
    {"id": 8, "name": "Mystic Merriment", "essence_points": 10},
    {"id": 9, "name": "Crystal Cheer", "essence_points": 12},
    {"id": 10, "name": "Enchanted Euphony", "essence_points": 14}
]
