import random
import json

# array of traits and rarities

backgrounds = ["pink", "orange", "purple", "beige", "green", "blue"]
background_weights = [1000, 1500, 1500, 2000, 2000, 1999]

bases = ["gold", "trippy", "zombie", "robot", "silver", "orange", "blue", "purple", "pink", "beige", "brown"]
base_weights = [100, 200, 300, 400, 800, 1000, 1000, 1000, 1000, 2000, 2199]

springs = ["gold", "red", "black", "gray", "white"]
spring_weights = [500, 1000, 1500, 3000, 3999]

tails = ["dragon", "flaming", "trippy", "festive", "ninja", "roolex", "pizza", "bow tie", "mini roo", "spike cuff", "handcuffs", "none"]
tail_weights = [100, 200, 200, 300, 400, 400, 400, 500, 500, 500, 500, 5999]

pouches = ["designer", "cheetah", "golden", "silver", "plaid", "black", "none"]
pouch_weights = [200, 300, 300, 500, 700, 1000, 6999]

eyes = ["laser", "robot", "flaming", "clout goggles", "shutter shades", "circle shades", "mask", "shades", "eyepatch", "monocle", "tired", "glasses", "wink", "closed", "open"]
eye_weights = [300, 300, 300, 500, 500, 500, 500, 600, 600, 600, 700, 700, 1200, 1200, 1499]

shirts = ["royal robe", "supersuit", "wizard robe", "knight armor", "samurai armor", "pirate tunic", "hype", "rocker", "angel robe", "poncho", "thief", "boxing robe", "ninja", "#1 Dad", "racing jacket", "gold chain", "hippie", "coconut bra", "bow tie", "overalls", "Playbobl robe", "tank top", "suit", "tattered", "orange hoodie", "green hoodie", "blue hoodie", "pink hoodie", "orange", "green", "blue", "pink", "none"]
shirt_weights = [20, 40, 40, 40, 40, 60, 60, 100, 100, 100, 200, 200, 200, 200, 200, 300, 300, 300, 400, 400, 400, 400, 400, 400, 500, 500, 500, 500, 600, 600, 600, 600, 699]

accessories = ["sword", "roomen", "cash", "coins", "pizza", "broccoli", "baby roo", "none"]
accessory_weights = [200, 200, 300, 300, 500, 500, 1000, 6999]

items = ["royal staff", "ray gun", "sword", "mini roo", "wizard staff", "club", "guitar", "boxing gloves", "Playbobl magazine", "ninja star", "money bag", "briefcase", "hook", "cutlass", "racing flag", "pitchfork", "water bottle", "pizza", "frying pan", "fidget spinner", "none"]
item_weights = [50, 75, 75, 200, 300, 300, 300, 400, 400, 500, 500, 600, 600, 600, 600, 700, 700, 700, 700, 700, 999]

shoes = ["rocket boots", "knight boots", "ice skates", "flippers", "rain boots", "clown", "robot", "rainbow", "LOAFers", "brown loafers", "black loafers", "bunny slippers", "slippers", "sandals", "tattered", "flip flops", "orange", "green", "blue", "pink", "black", "white", "none"]
shoe_weights = [50, 75, 75, 100, 100, 200, 300, 300, 300, 400, 400, 400, 500, 500, 500, 500, 700, 700, 700, 700, 800, 800, 899]

mouths = ["golden grill", "fire breathing", "Fu Manchu mustache", "brown beard", "grey beard", "mustache", "mustache tongue", "closed pipe", "pucker pipe", "tongue", "closed straw", "closed joint", "pucker straw", "pucker joint", "closed mouth", "open mouth", "pucker"]
mouth_weights = [100, 100, 200, 300, 300, 400, 500, 700, 700, 800, 800, 800, 800, 800, 900, 900, 899]

hats = ["crown", "wizard", "jester", "viking helmet", "santa", "samurai helmet", "pirate", "chef", "trippy mowhawk", "cheese", "conical", "soda hat", "boxing headgear", "captain", "horns", "halo", "hippie", "mohawk", "cop", "greek leaves", "pizza slice", "ice ceam", "#1 Dad", "top hat", "farmer", "propeller cap", "racing cap", "earring", "scrunchie", "headband", "baseball cap", "backwards cap", "none"]
hat_weights = [50, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 400, 400, 400, 400, 500, 500, 500, 500, 500, 599]

# all array lengths and corresponding weight array lengths match
# all values of the weight arrays add up to 9999
# all names are distinct

# CREATE THE TRAIT COMBOS:
# the combo list stores all combinations for the for loop in create_combo
combo_list = [
        [backgrounds, background_weights, "background"],
        [bases, base_weights, "base"],
        [springs, spring_weights, "spring"],
        [tails, tail_weights, "tail"],
        [pouches, pouch_weights, "pouch"],
        [eyes, eye_weights, "eyes"],
        [shirts, shirt_weights, "shirt"],
        [accessories, accessory_weights, "accessory"],
        [items, item_weights, "item"],
        [shoes, shoe_weights, "shoes"],
        [mouths, mouth_weights, "mouth"],
        [hats, hat_weights, "hat"]
    ]

traits = []

# sums all of the integers in an array
def sum(trait_weights):
    sum = 0
    for num in trait_weights:
        sum = sum + num
    return sum

# gets the index of a new trait to add in a completely randomized and unbiased way
def getIndex(x, trait_weights):
    sum = 0
    index = 0
    for num in trait_weights:
        sum = sum + num
        if x <= sum:
            return index
        index = index + 1
    return "not found"

# creates a random trait combo
def createCombo(tokenId):
    
    trait = {}
    for combo in combo_list:

        # pick a random background trait
        trait_list = combo[0]
        trait_weights = combo[1]
        trait_name = combo[2]
        x = random.randrange(sum(trait_weights))
        i = getIndex(x, trait_weights)
        trait[trait_name] = trait_list[i]
        trait_weights[i] = trait_weights[i] - 1
        if(trait_weights[i] <= 0):
            trait_list.pop(i)
            trait_weights.pop(i)
    
    trait["tokenId"] = tokenId
    return trait

# generate all 9999 combos
index = 1
while len(backgrounds) + len(bases) + len(springs) + len(tails) + len(pouches) + len(eyes) + len(shirts) + len(accessories) + len(items) + len(shoes) + len(mouths) + len(hats) > 0:
    new_trait_combo = createCombo(index)
    traits.append(new_trait_combo)
    print(index)
    index = index + 1


# write metadata to json file
with open('metadata.json', 'w') as outfile:
    json.dump(traits, outfile, indent=4)