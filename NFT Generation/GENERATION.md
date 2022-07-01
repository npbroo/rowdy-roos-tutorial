# Generating Artwork For 2D NFTs

Generating art for an NFT project may sound like a lot of work. And it can be if the artwork is created incorrectly or the generation process is not well organized. This tutorial aims to cover the basic steps required to generate your own 2D NFTs in a straight forward and easy to understand way.

Every NFT is unique, and if we break down an NFT into its most basic components we discover that it is comprised of a random combination of different traits, separated into different 'trait categories'. When building your own NFT, you must first decide how you want to group your traits. For example, Rowdy Roos has 13 different trait categories: Accessory, Background, Base, Eyes, Hat, Item, Mouth, Pouch, Rank, Shirt, Shoes, Spring, and Tail. These are the unique building blocks that make up each Rowdy Roo.

## Trait Category
Trait categories are unique to each NFT project and often change depending on the artwork and overall design of the NFT. However, every NFT belonging to a single project will have the exact same trait categories. These trait categories don’t determine rarity, they only represent the changing parts of an NFT. 

## Sub-Traits
Each trait category contains a collection of sub-traits. The sub-traits are what change to give each NFT its own unique look and rarity.

![Trait Categories](/NFT%20Generation/images/trait_categories.png)
 
Here, I have included a screenshot from OpenSea which is a popular exchange used to buy an sell NFTs. This also provides us with an easy-to-understand diagram for visualizing trait categories and their sub-traits. In the image above, we can see that the bolded words on the left are the different trait categories and the number beside it represents the number of sub-traits within each trait category.

If we click on the drop-down, we can see all of the different sub-traits for that trait category. In the example below, I chose to list traits for the ‘base’ category. Within this category there are 12 different types of bases which are custom to the Rowdy Roos project. The number to the right of each sub-trait represents the number of NFTs in the collection which have that trait. Here I have selected the ‘Robot’ sub-trait under the 'base' category. This is why we only see Rowdy Roos which have the ‘Robot’ base.

![Sub-Traits](/NFT%20Generation/images/subtraits.png)
 
To the right of the ‘Robot’ sub-trait you can see that there are 400 NFTs in the entire Rowdy Roo collection which has this specific trait. Since the supply of our collection is 10,000 total NFTs, there is a 4% chance that any Rowdy Roo has this trait. This makes it a rare trait. The more rare traits your NFT has, the rarer it is. This can often direclty increase an NFT's perceived value resulting in a potentially higher selling price.

![NFT with Metadata](/NFT%20Generation/images/nft_with_metadata.png)

Here, you can see a Rowdy Roo on the left, with all of the trait categories, and the specific sub-traits this NFT is comprised of. Together, all of the traits on the right make up what is known as the metadata for this Rowdy Roo. By layering these traits, we can generate this unique "kingly" Rowdy Roo.

## Deconstructed NFT

Let’s further deconstruct this NFT and see each of the individual parts that it’s made of.
      
![A Deconstructed NFT](/NFT%20Generation/images/deconstructed.png)

Here you can see all the different traits which can be stacked together to construct this unique NFT. There are many programs online which are available and capable of doing this process automatically. However many are limited and may not have all of the capabilities you need for your project. For Rowdy Roos, we wanted more control over the generation process and is why we built a custom program written with the Python coding language.

## Building your own Generator

When generating NFTs, it is always best to separate the process into two steps: metadata generation and art generation. A project's full metadata file defines all of an NFT's sub-traits in a written format for each NFT in the entire collection. It can be stored in many different file formats, but we will use JSON format for this tutorial. JSON is a standard file format which can be easily read and parsed by coding languages such as Python. Below, I have included a copy of the metadata (in JSON format) for the "kingly" NFT we have deconstructed above.

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

This sample JSON file holds every piece of information we need to be able to build the exact NFT we see above. The NFT is represented by everything inside of the set of curly braces “{}”. Here you can see we have each of the trait categories on the left mapped to its corresponding sub-trait on the right. 

Awesome! we have successfully created a metadata file with exactly one entry. Now this would be great if we wanted to generate just one NFT, however a typical collection often contains thousands of NFTs. The Rowdy Roos collection, for example, 9,999 different NFTs. That's a lot of NFTs! A JSON file containing 9,999 different entries is very long and is not something anybody should write by hand. To see what a full-length metadata file looks like, you can view the inlcuded metadata file I generated for this tutorial series [here](/NFT%20Generation/code/metadata.json).

## Metadata Generation

Pretty cool right? While this file doesn't include the official metadata, it does include 9,999 brand new potential combinations for Rowdy Roos. These brand new, never-before-seen combinations were actually generated on the fly using my [metadata generator](/NFT%20Generation/code/metadata_generator.py), and it only took me a matter of seconds.

So how does the metadata generator work? Well, for each trait category, there is a list of all of the sub-traits' names and their corresponding weights. The weights determine how many times each sub-trait appears in the collection. Since this is a collection of 9,999 NFTs, the weights for each category must add up to 9,999.

Below, I included a snippet of the code which demonstrates sub-traits and their corresponding weights for the 'background' trait category.

```
# sub-traits and their corresponding weights for the 'background' trait category
backgrounds = ["pink", "orange", "purple", "beige", "green", "blue"]
background_weights = [1000, 1500, 1500, 2000, 2000, 1999]
```

The generator works by randomly selecting a sub-trait from each category for all 9,999 NFTs. after it selects a sub-trait, it subtracts 1 from the sub-trait's corresponding weight. This allows for an even distribution of traits across all NFTs and prevents traits from appearing more than the number of times specified in its trait weights.

After it finishes igenerating all of the combinations, it exports them to a JSON file called metadata. Give it a try yourself! Just download Python, and give the [metadata generator](/NFT%20Generation/code/metadata_generator.py) a run. You will have a brand new set of metadata for 9,999 Rowdy Roo NFT combinations.

## Art Generation

Art generation is the second stage in the NFT generation process. Once you have the metadata, it can be used as a set of instructions (or blueprint) which defines how all of the art is generated for your NFT collection going forward. As long as the metadata doesn't change, it can be used with the art generator as many times as you want and will always generate the exact same NFT combinations. This can be very helpful when testing new artwork. Maybe a hat trait didn't fit right the first time so you have to generate all of the artwork again. In this scenario, you could regenerate the NFTs with the exact same combination of traits and fix the hat trait without changing your entire collection.

To see how the art generation process works, I have included the source code for Rowdy Roo's [Art Generator](/NFT%20Generation/code/art_generator.py).

At the top of the art generator file you can see each of the trait names which were previously defined in the metadata generator file. Each trait name is then mapped to the filename containing the artwork for that trait. Below is a snippet from the code for reference.

```
# trait names and their corresponding filename mappings for the 'background' trait category
background_files = {
    "pink":"background2", 
    "orange":"background3", 
    "purple":"background6", 
    "beige":"background1", 
    "green":"background4", 
    "blue":"background5"
}
```

Here, the pink background would be stored in the file 'background2.png', the orange background would be stored in 'background3.png', and so on...

To keep track of the hundreds of different traits, the folder or directory structure must be very well organized. This allows for easy navigation of the traits and cleaner more readable code. Below, I have included an example of the directory structure my art generator was built to run on.

```
generator/
├── art_generator.json
├── metadata.json
└── resources/
    ├── backgrounds/
    │   ├── background1.png
    │   ├── background2.png
    │   └── ...
    ├── bases/
    │   ├── base1.png
    │   ├── base2.png
    │   └── ...
    ├── springs/
    │   ├── spring1.png
    │   ├── spring2.png
    │   └── ...
    ├── springs/
    ├── eyes/
    ├── mouths/
    ├── tails/
    ├── pouches/
    ├── shirts/
    ├── accessories/
    ├── items/
    ├── shoes/
    └── hats/
```

This directory structure contains every single deconstructed sub-trait in a folder corresponding to its trait category. It's important to note that each sub-trait is saved as a png image with a tranparent background of the same size. This makes the sub-traits "stackable" and is very important when generating the artwork.

Based on the directory tree above, if I was to open up the file 'resources/backgrounds/background1.png' it should contain a picture with a pink background. I have not included the art assets in this tutorial due to legal reasons. But the art generator script is open source and can be edited for use with your art and custom project.

The art generator works by scanning the metadata included in the JSON file (generated by the metadata generator). Then, it cycles through each of the 9,999 NFTs represented within the metadata file and stacks the deconstructed traits one at at time to construct a finalized image representing a Rowdy Roo. This is then exported and saved as a jpg image.


## Final Thoughts

For people new to the space or for beginner coders, 2D NFT generation may sound like an advanced topic. I hope that this tutorial can shed some light on the process and maybe even help you to get started on an NFT creation journey of your own. While this tutorial covers my personal method and experience, there are still hundreds of different methods and algorithms out there for generating all types of NFTs such as multi-base NFTs or even animated 3D and 2D NFTs. In the future, these are areas I would like to further explore and possibly even share with you, But until then, cheers!



