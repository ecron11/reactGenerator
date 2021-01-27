import json

#Parse the input JSON template into a python dictionary
templateFile = open("template.json", "r")
template = json.loads(templateFile.read())
templateFile.close()

outputFile = open("./reactFiles/" + template["templateName"] +".js", "w")

    ## React Functional component generator
if template["templateType"] == "reactFunctional":
    outputFile.write("import React from 'react' \n\n")
    outputFile.write("export default function " + template["templateName"] + "(props) { \nreturn (\n")
    
    for component in template['template']:
        outputFile.write("<" + component["component"] + ">\n" + "</" + component["component"] + ">\n")

    #closing parentheses and brackets
    outputFile.write("\n)\n}")

outputFile.close()
