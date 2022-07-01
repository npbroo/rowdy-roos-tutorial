# Generating artwork for 2D NFTs

Each NFT is unique and is comprised of a random combination of different traits each belonging to its own trait group. When building an NFT, you must first decide how you want to group your traits. For example, Rowdy Roos has 13 different trait groups: Accessory, Background, Base, Eyes, Hat, Item, Mouth, Pouch, Rank, Shirt, Shoes, Spring, and Tail. These are the unique building blocks that make up each Rowdy Roo.

## Trait Groups
Trait groups are unique to the each NFT project and often change depending on the artwork and overall design of the NFT. However, every NFT belonging to a single project will have the exact same trait groups. These trait groups don’t determine rarity, they only represent the changing parts of an NFT. 

## Sub Groups
Within each trait group there is a collection of sub traits. The sub-traits are what change to give the NFT its own unique look and rarity.

![Trait Groups](/NFT%20Generation/images/trait_groups.png)
 
Here we can see that the bolded words on the left are the different trait groups and the number beside it represents the number of sub-traits within each trait group.

If we click on the drop-down, we can see all of the different sub-traits for that category. In the example below, I chose to list traits for the ‘base’ category. Within this category there are 12 different types of bases which are custom to the Rowdy Roos project. The number to the right of each sub-trait represents the number of NFTs in the collection which have that trait. Here I have selected the ‘Robot’ trait, so we only see Rowdy Roos which have the ‘Robot’ base.

![Trait Groups](/NFT%20Generation/images/subtraits.png)
 
To the right of the ‘Robot’ sub-trait you can see that there are 400 NFTs in the entire Rowdy Roo collection which has this specific trait. Since the supply of our collection is 10,000 total NFTs, there is a 4% chance that any Rowdy Roo has this trait which makes it a very rare trait. 

![Trait Groups](/NFT%20Generation/images/nft_with_metadata.png)

Here you can see a Rowdy Roo on the left and all of the trait categories with the specific sub-traits the NFT is comprised of. Together, all the traits on the right make up the metadata for the Rowdy Roo. By layering these the traits, we can generate this unique kingly Rowdy Roo.

## Deconstructed NFT

Let’s further deconstruct this NFT and see each of the individual parts that it’s made of.
      
![Trait Groups](/NFT%20Generation/images/deconstructed.png)

Here you can see all the individual traits which stack together to make this unique NFT. There are many programs and online software capable of doing this process automatically. But, for Rowdy Roos we wanted more control over the generation process and is why we built a custom program written with the Python coding language.

## Building your own Generator

When generating NFTs, it is always best to separate the process into two steps: metadata generation and art generation. Metadata defines the NFT in a written format for each NFT in the entire collection. It can be stored in many different file formats, but we will use JSON format for this tutorial. JSON is a standard file format which can be easily read and parsed by coding languages such as Python. 

Below is a copy of the metadata (in JSON format) for the NFT we have deconstructed above.

```json
[
    {
            "background": "green",
            "base": "robot",
            "spring": "gold",
            "tail": "none",
            "pouch": "none",
            "eyes": "robot",
            "shirt": "royal robe",
            "accessory": "none",
            "item": "royal staff",
            "shoes": "robot",
            "mouth": "gray beard",
            "hat": "crown",
            "tokenId": 40
    }
]
```

This sample JSON file holds every piece of information we need to be able to build the exact NFT we see above. The NFT is represented by everything inside of the set of curly braces “{}”. Here you can see we have each of the trait categories on the left of the ‘:’ and the corresponding sub-trait on the right of the ‘:’. 

Awesome! we have successfully created a metadata file with exactly one entry. Now this would be great if we wanted to generate just one NFT, however, a typical collection often has thousands of NFTs, and for Rowdy Roos, we have over 9,999 different NFTs. That's a lot of NFTs! A JSON file like that would need 9,999 different entries and would be very long. To see what a metadata file like that looks you can view the sample metadata file I generated for this tutorial series [here](/NFT%20Generation/metadata.json).

Pretty cool right? While this file doesn't include the official metadata, it does include 9,999 brand new potential combinations for Rowdy Roos. These brand new never before seen combinations were actually generated on the fly using my [metadata generator](/NFT%20Generation/metadata_generator.py), and it only takes a matter of seconds.

