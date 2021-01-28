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

    outputFile.write("import React from 'react' \n\n")
    outputFile.write("export default function " + template["templateName"] + "(props) { \n")
    
    currentIndent += 1
    outputFile.write(currentIndent*indentCharacter + "return (\n")
    currentIndent += 1
    for component in template['template']:
        outputFile.write(currentIndent*indentCharacter + "<" + component["component"] + "\n")

        currentIndent += 1
        for arg in component["arguments"].keys():
            outputFile.write(currentIndent*indentCharacter + arg + "='" + component["arguments"][arg] + "'\n")
        currentIndent -= 1
        outputFile.write(currentIndent*indentCharacter + ">\n")
        outputFile.write(currentIndent*indentCharacter + "</" + component["component"] + ">\n")
    #closing parentheses and brackets
    outputFile.write(currentIndent*indentCharacter + "\n)")
    currentIndent -= 1
    outputFile.write(currentIndent*indentCharacter + "\n}")

outputFile.close()
