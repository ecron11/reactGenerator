import json

#Parse the input JSON template into a python dictionary
templateFile = open("template.json", "r")
template = json.loads(templateFile.read())
templateFile.close()

outputFile = open("./reactFiles/" + template["templateName"] +".js", "w")

indentCharacter = "\t"
currentIndent = 0

    ## React Functional component generator
if template["templateType"] == "reactFunctional":
    # Need to add imports for any children react elements

    outputStr = ""

    outputStr +=("import React from 'react' \n\n")
    outputStr +=("export default function " + template["templateName"] + "(props) { \n")
    
    currentIndent += 1
    
    outputStr +=(currentIndent*indentCharacter + "return (\n")
    currentIndent += 1
    
    for component in template['template']:
        outputStr +=(currentIndent*indentCharacter + "<" + component["component"] + "\n")

        currentIndent += 1
        
        for arg in component["arguments"].keys():
            outputStr +=(currentIndent*indentCharacter + arg + "='" + component["arguments"][arg] + "'\n")
        currentIndent -= 1
        
        outputStr +=(currentIndent*indentCharacter + ">\n")
        
        outputStr +=(currentIndent*indentCharacter + "</" + component["component"] + ">\n")
    #closing parentheses and brackets
    currentIndent -= 1
    outputStr +=(currentIndent*indentCharacter + ")\n")
    currentIndent -= 1
    outputStr +=(currentIndent*indentCharacter + " }")

    outputFile.write(outputStr)
outputFile.close()
