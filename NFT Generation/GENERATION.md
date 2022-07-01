# Generating artwork for 2D NFTs

Each NFT is unique and is comprised of a random combination of different traits each belonging to its own trait group. When building an NFT, you must first decide how you want to group your traits. For example, Rowdy Roos has 13 different trait groups: Accessory, Background, Base, Eyes, Hat, Item, Mouth, Pouch, Rank, Shirt, Shoes, Spring, and Tail. These are the unique building blocks that make up each Rowdy Roo.

## Trait Groups
Trait groups are unique to the each NFT project and often change depending on the artwork and overall design of the NFT. However, every NFT belonging to a single project will have the exact same trait groups. These trait groups don’t determine rarity, they only represent the changing parts of an NFT. 

## Sub Groups
Within each trait group there is a collection of sub traits. The sub-traits are what change to give the NFT its own unique look and rarity.
 
Here we can see that the bolded words on the left are the different trait groups and the number beside it represents the number of sub-traits within each trait group.

If we click on the drop-down, we can see all of the different sub-traits for that category. In the example below, I chose to list traits for the ‘base’ category. Within this category there are 12 different types of bases which are custom to the Rowdy Roos project. The number to the right of each sub-trait represents the number of NFTs in the collection which have that trait. Here I have selected the ‘Robot’ trait, so we only see Rowdy Roos which have the ‘Robot’ base.
 
To the right of the ‘Robot’ sub-trait you can see that there are 400 NFTs in the entire Rowdy Roo collection which has this specific trait. Since the supply of our collection is 10,000 total NFTs, there is a 4% chance that any Rowdy Roo has this trait which makes it a very rare trait. 

  

Here you can see a Rowdy Roo on the left and all of the trait categories with the specific sub-traits the NFT is comprised of. Together, all the traits on the right make up the metadata for the Rowdy Roo. By layering these the traits, we can generate this unique kingly Rowdy Roo.

## Deconstructed NFT

Let’s further deconstruct this NFT and see each of the individual parts that it’s made of.
      
   

Here you can see all the individual traits which stack together to make this unique NFT. There are many programs and online software capable of doing this process automatically. But, for Rowdy Roos we wanted more control over the generation process and is why we built a custom program written with the Python coding language.

## Building your own Generator

When generating NFTs, it is always best to separate the process into two steps: metadata generation and art generation. Metadata defines the NFT in a written format for each NFT in the entire collection. It can be stored in many different file formats, but we will use JSON format for this tutorial. JSON is a standard file format which can be easily read and parsed by coding languages such as Python. 

Below is a copy of the metadata (in JSON format) for the NFT we have deconstructed above.
