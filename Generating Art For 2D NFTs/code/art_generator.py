import json
from PIL import Image, ImageOps

# MAPPINGS FOR THE FILENAMES CORRESPONDING TO EACH TRAIT NAME
background_files = {
    "pink":"background2", 
    "orange":"background3", 
    "purple":"background6", 
    "beige":"background1", 
    "green":"background4", 
    "blue":"background5"
}

base_files = {
    "gold":"base7", 
    "trippy":"base9", 
    "zombie":"base10", 
    "robot":"base11", 
    "silver":"base8", 
    "orange":"base3", 
    "blue":"base4", 
    "purple":"base5", 
    "pink":"base6", 
    "beige":"base2", 
    "brown":"base1"
}

spring_files = {
    "gold":"spring3", 
    "red":"spring5", 
    "black":"spring4", 
    "gray":"spring2",
    "white":"spring1"
}

tail_files = {
    "dragon":"tail2", 
    "flaming":"tail5", 
    "trippy":"tail11", 
    "festive":"tail7", 
    "ninja":"tail1", 
    "roolex":"tail4", 
    "pizza":"tail10", 
    "bow tie":"tail3", 
    "mini roo":"tail6", 
    "spike cuff":"tail8", 
    "handcuffs":"tail9", 
    "none":""
}

pouch_files = {
    "designer":"pouch2", 
    "cheetah":"pouch1", 
    "golden":"pouch4", 
    "silver":"pouch3", 
    "plaid":"pouch5", 
    "black":"pouch6", 
    "none":""
}

eye_files = {
    "laser":"eyes11", 
    "robot":"eyes12", 
    "flaming":"eyes21", 
    "clout goggles":"eyes13", 
    "shutter shades":"eyes20", 
    "circle shades":"eyes22", 
    "mask":"eyes7", 
    "shades":"eyes10", 
    "eyepatch":"eyes17", 
    "monocle":"eyes4", 
    "tired":"eyes19", 
    "glasses":"eyes14", 
    "wink":"eyes2", 
    "closed":"eyes3", 
    "open":"eyes1"
}

shirt_files = {
    "royal robe":"shirt29", 
    "supersuit":"shirt18", 
    "wizard robe":"shirt20", 
    "knight armor":"shirt27", 
    "samurai armor":"shirt32", 
    "pirate tunic":"shirt21", 
    "hype":"shirt26", 
    "rocker":"shirt23", 
    "angel robe":"shirt24", 
    "poncho":"shirt28", 
    "thief":"shirt10", 
    "boxing robe":"shirt13", 
    "ninja":"shirt17", 
    "#1 Dad":"shirt30", 
    "racing jacket":"shirt31", 
    "gold chain":"shirt12", 
    "hippie":"shirt19", 
    "coconut bra":"shirt25", 
    "bow tie":"shirt9", 
    "overalls":"shirt11", 
    "Playbobl robe":"shirt14", 
    "tank top":"shirt15", 
    "suit":"shirt16", 
    "tattered":"shirt22",
    "orange hoodie":"shirt5", 
    "green hoodie":"shirt6", 
    "blue hoodie":"shirt7", 
    "pink hoodie":"shirt8", 
    "orange":"shirt1", 
    "green":"shirt2", 
    "blue":"shirt3", 
    "pink":"shirt4", 
    "none":""
}

accessory_files = {
    "sword":"pa5", 
    "roomen":"pa7", 
    "cash":"pa1", 
    "coins":"pa6", 
    "pizza":"pa3", 
    "broccoli":"pa4", 
    "baby roo":"pa2", 
    "none":""
}

item_files = {
    "royal staff":"item18", 
    "ray gun":"item15", 
    "sword":"item20", 
    "mini roo":"item11", 
    "wizard staff":"item8",
    "club":"item10", 
    "guitar":"item13", 
    "boxing gloves":"item4", 
    "Playbobl magazine":"item5", 
    "ninja star":"item1", 
    "money bag":"item2", 
    "briefcase":"item7", 
    "hook":"item9", 
    "cutlass":"item16", 
    "racing flag":"item19", 
    "pitchfork":"item3", 
    "water bottle":"item6", 
    "pizza":"item12", 
    "frying pan":"item14", 
    "fidget spinner":"item17", 
    "none":""
}

shoe_files = {
    "rocket boots":"shoes13", 
    "knight boots":"shoes9", 
    "ice skates":"shoes12", 
    "flippers":"shoes21", 
    "rain boots":"shoes22", 
    "clown":"shoes19", 
    "robot":"shoes14", 
    "rainbow":"shoes16", 
    "LOAFers":"shoes20", 
    "brown loafers":"shoes10", 
    "black loafers":"shoes11", 
    "bunny slippers":"shoes17", 
    "slippers":"shoes1", 
    "sandals":"shoes2", 
    "tattered":"shoes15", 
    "flip flops":"shoes18", 
    "orange":"shoes5", 
    "green":"shoes6", 
    "blue":"shoes7", 
    "pink":"shoes8", 
    "black":"shoes3", 
    "white":"shoes4", 
    "none":""
}

mouth_files = {
    "golden grill":"mouth13", 
    "fire breathing":"mouth14", 
    "Fu Manchu mustache":"mouth17", 
    "brown beard":"mouth15", 
    "grey beard":"mouth16", 
    "mustache":"mouth5", 
    "mustache tongue":"mouth6", 
    "closed pipe":"mouth9", 
    "pucker pipe":"mouth12", 
    "tongue":"mouth2", 
    "closed straw":"mouth7", 
    "closed joint":"mouth8", 
    "pucker straw":"mouth10", 
    "pucker joint":"mouth11", 
    "closed mouth":"mouth1", 
    "open mouth":"mouth3", 
    "pucker":"mouth4"
}

hat_files = {
    "crown":"hat27", 
    "wizard":"hat13", 
    "jester":"hat15", 
    "viking helmet":"hat21", 
    "santa":"hat30", 
    "samurai helmet":"hat32", 
    "pirate":"hat14", 
    "chef":"hat18", 
    "trippy mowhawk":"hat23", 
    "cheese":"hat24", 
    "conical":"hat31", 
    "soda hat":"hat19", 
    "boxing headgear":"hat4", 
    "captain":"hat5", 
    "horns":"hat8", 
    "halo":"hat9",
    "hippie":"hat10", 
    "mohawk":"hat17", 
    "cop":"hat20", 
    "greek leaves":"hat22", 
    "pizza slice":"hat25", 
    "ice ceam":"hat26", 
    "#1 Dad":"hat28", 
    "top hat":"hat1", 
    "farmer":"hat2", 
    "propeller cap":"hat16", 
    "racing cap":"hat29", 
    "earring":"hat3", 
    "scrunchie":"hat6", 
    "headband":"hat7", 
    "baseball cap":"hat11", 
    "backwards cap":"hat12", 
    "none":""
}


# open the metadata file
with open("metadata.json", 'r') as f:
    traits = json.load(f)

# generate the images
for item in traits:

    background_img = Image.open(f'./resources/backgrounds/{background_files[item["background"]]}.png').convert('RGBA')
    base_img = Image.open(f'./resources/bases/{base_files[item["base"]]}.png').convert('RGBA')
    spring_img = Image.open(f'./resources/springs/{spring_files[item["spring"]]}.png').convert('RGBA')
    eyes_img = Image.open(f'./resources/eyes/{eye_files[item["eyes"]]}.png').convert('RGBA')
    mouth_img = Image.open(f'./resources/mouths/{mouth_files[item["mouth"]]}.png').convert('RGBA')

    if(item["tail"] == "none"):
        tail_img = None
    else:
        tail_img = Image.open(f'./resources/tails/{tail_files[item["tail"]]}.png').convert('RGBA')

    if(item["pouch"] == "none"):
        pouch_img = None
    else:
        pouch_img = Image.open(f'./resources/pouches/{pouch_files[item["pouch"]]}.png').convert('RGBA')

    if(item["shirt"] == "none"):
        shirt_img = None
    else:
        shirt_img = Image.open(f'./resources/shirts/{shirt_files[item["shirt"]]}.png').convert('RGBA')

    if(item["accessory"] == "none"):
        accessory_img = None
    else:
        accessory_img = Image.open(f'./resources/accessories/{accessory_files[item["accessory"]]}.png').convert('RGBA')

    if(item["item"] == "none"):
        item_img = None
    else:
        item_img = Image.open(f'./resources/items/{item_files[item["item"]]}.png').convert('RGBA')

    if(item["shoes"] == "none"):
        shoes_img = None
    else:
        shoes_img = Image.open(f'./resources/shoes/{shoe_files[item["shoes"]]}.png').convert('RGBA')

    if(item["hat"] == "none"):
        hat_img = None
    else:
        hat_img = Image.open(f'./resources/hats/{hat_files[item["hat"]]}.png').convert('RGBA')


    #Create each composite
    com = Image.alpha_composite(background_img, base_img) # no need to check if Nonetype here
    com = Image.alpha_composite(com, spring_img) # no need to check if Nonetype here
    
    if tail_img != None:
        com = Image.alpha_composite(com, tail_img)
    
    if pouch_img != None:
        com = Image.alpha_composite(com, pouch_img)
    
    com = Image.alpha_composite(com, eyes_img) # no need to check if Nonetype here

    if shirt_img != None:
        com = Image.alpha_composite(com, shirt_img)
    
    if accessory_img != None:
        com = Image.alpha_composite(com, accessory_img)

    if item_img != None:
        com = Image.alpha_composite(com, item_img)

    if shoes_img != None:
        com = Image.alpha_composite(com, shoes_img)

    com = Image.alpha_composite(com, mouth_img) # no need to check if Nonetype here

    if hat_img != None:
        com = Image.alpha_composite(com, hat_img)


    #Convert to RGB
    rgb_im = com.convert('RGB')
    #display(rgb_im.resize((800,800), Image.NEAREST))

    file_name = "rr" + str(item["tokenId"]) + ".jpg"
    rgb_im.save("./output/" + file_name)
    print(f'{str(item["tokenId"])} done')