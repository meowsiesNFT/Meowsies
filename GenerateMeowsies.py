from PIL import Image
import random

"""
example metadata - just so we know the structure and can modify if needed
{
    "name": "meowsies #45",
    "description": "Meowsies project",
    "tokenId" : "45",
    "image": "",
    "attribute": [
        {
            "trait_type": "Hat",
            "value": "Top Hat"
        },
        {
            "trait_type": "Whiskers",
            "value": "Grey"
        }
    ]
}
"""

for loopCounter in range(0,801):
    #initialize our string for our trait metadata
    attributeMetadata = ""

    #background layer
    randomNum = random.randint(1,1) #We didn't like our background colors, so in the end, we set the white background to always be there (random number between 1 and 1...so always 1)
    background = Image.open("./SourceLayers/Background" + str(randomNum) + ".png")
    traitValues = ["white","pink","blue","green"]
    attributeMetadata = '{"trait_type":"Background","value":"' + traitValues[randomNum-1] + '"},'

    #fur layer
    randomNum = random.randint(2,11) #our diamond fur is image #1, so skip it in the random number generator here because we only want it chosen by our special 5% logic
    #5% of the time, re-assign the fur random number to be 1 instead of the random number chosen
    if random.random() <= .05:
        randomNum = 1
    foreground = Image.open("./SourceLayers/Fur" + str(randomNum) + ".png")
    background.paste(foreground, (0, 0), foreground)
    traitValues = ["rainbow","gizmo","light brown","dark brown","purple","blue","pink","green","yellow","orange","red"]
    attributeMetadata = attributeMetadata + '{"trait_type":"Fur","value":"' + traitValues[randomNum-1] + '"},'

    #add mouthbling (sometimes)
    #we found that we needed this layer to be below the body outline to look correct in the final image, so moved it up here so it is added before the body outline layer
    if random.random() <= .5:
        randomNum = random.randint(1,3)
        foreground = Image.open("./SourceLayers/MouthBling" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0),foreground)
        traitValues = ["mouse","lollipop","tongue"]
        attributeMetadata = attributeMetadata + '{"trait_type": "MouthBling","value": "' + traitValues[randomNum-1] + '"},'

    #body outline layer
    foreground = Image.open("./SourceLayers/BodyOutline.png")
    background.paste(foreground, (0, 0), foreground)

    #add facebling (sometimes)
    if random.random() <= .6:
        randomNum = random.randint(1,5)
        foreground = Image.open("./SourceLayers/FaceBling" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0),foreground)
        traitValues = ["blush","lots freckles","bandage","some freckles","few freckles"]
        attributeMetadata = attributeMetadata + '{"trait_type": "FaceBling","value": "' + traitValues[randomNum-1] + '"},'

    #eyes layer
    randomNum = random.randint(1,9)
    foreground = Image.open("./SourceLayers/Eyes" + str(randomNum) + ".png")
    background.paste(foreground, (0, 0), foreground)
    traitValues = ["grumpy","closed happy","closed","confused","meh","happy open","angry","sad","open"]
    attributeMetadata = attributeMetadata + '{"trait_type":"Eyes","value":"' + traitValues[randomNum-1] + '"},'

    #add claws (sometimes)
    if random.random() <= .5:
        randomNum = random.randint(1,3)
        foreground = Image.open("./SourceLayers/Claws" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0),foreground)
        traitValues = ["rainbow","pink","tan"]
        attributeMetadata = attributeMetadata + '{"trait_type": "Claws","value": "' + traitValues[randomNum-1] + '"},'

    #add earbling (sometimes)
    if random.random() <= .35:
        randomNum = random.randint(1,4)
        foreground = Image.open("./SourceLayers/EarBling" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0),foreground)
        traitValues = ["studs","double hoop both","double hoop single","single hoop"]
        attributeMetadata = attributeMetadata + '{"trait_type": "EarBling","value": "' + traitValues[randomNum-1] + '"},'

    #add neckbling (sometimes)
    if random.random() <= .35:
        randomNum = random.randint(1,2)
        foreground = Image.open("./SourceLayers/NeckBling" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0),foreground)
        traitValues = ["pendant","pearls"]
        attributeMetadata = attributeMetadata + '{"trait_type": "NeckBling","value": "' + traitValues[randomNum-1] + '"},'

    #hat layer (sometimes)
    if random.random() < .6:
        randomNum = random.randint(1,10)
        foreground = Image.open("./SourceLayers/Hat" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0), foreground)
        traitValues = ["mohawk","party hat","stocking cap","chef hat","top hat","tiny top hat","crown","wizard hat","bonnet","baseball cap"]
        attributeMetadata = attributeMetadata + '{"trait_type":"Hat","value":"' + traitValues[randomNum-1] + '"},'

    #whiskers layer (sometimes)
    if random.random() < .6:
        randomNum = random.randint(1,3)
        foreground = Image.open("./SourceLayers/Whiskers" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0), foreground)
        traitValues = ["multicolor","white","grey"]
        attributeMetadata = attributeMetadata + '{"trait_type":"Whiskers","value":"' + traitValues[randomNum-1] + '"},'

    #eyesbling layer (sometimes)
    if random.random() < .15:
        randomNum = random.randint(1,1) #yeah, we only have one, no need for random number, but making all your code sections identical helps troubleshoot and fix things later, so do it anyway
        foreground = Image.open("./SourceLayers/EyesBling" + str(randomNum) + ".png")
        background.paste(foreground, (0, 0), foreground)
        traitValues = ["glasses"]
        attributeMetadata = attributeMetadata + '{"trait_type":"EyesBling","value":"' + traitValues[randomNum-1] + '"},'

    #New logic for removing last comma in our attributes string (the last attribute in our metadata should not have a commma, because that would indicate there are more attributes)
    #We found that we had no easy way to identify which trait was added last...so we just check if the last character of our string is a comma, and if so, remove the last character
    #In reality, in our code above we ALWAYS add a comma, so we will always have a comma as last character, but I added this code just you know how to do it if you needed to
    if attributeMetadata[-1] == ',':
        attributeMetadata = attributeMetadata[:-1]

    #save the final image
    background.save("./FinishedFiles/FinalImages/" + str(loopCounter) + ".png")

    #save the metadata file
    f = open("./FinishedFiles/MetadataFiles/" + str(loopCounter) + ".json", "w")
    f.write('{"name":"meowsies #' + str(loopCounter) + '","description":"Meowsies living on the blockchain. Learn how to make your own NFTs with me.","tokenId":"' + str(loopCounter) + '","image":"ipfs://bafybeiac4whoa6w7zrxcis3mgohkxadpdfdycvj4na7kwcmsxjgje3pigi/' + str(loopCounter) + '.png","attribute":[' + attributeMetadata + ']}')
    f.close()

    #save the unrevealed metadata file
    f = open("./FinishedFiles/UnrevealedMetadataFiles/" + str(loopCounter) + ".json", "w")
    f.write('{"name":"meowsies #' + str(loopCounter) + '","description":"Meowsies living on the blockchain. Learn how to make your own NFTs with me.","tokenId":"' + str(loopCounter) + '","image":"ipfs://bafybeiac4whoa6w7zrxcis3mgohkxadpdfdycvj4na7kwcmsxjgje3pigi"}')
    f.close()

