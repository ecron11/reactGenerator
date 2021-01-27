import json

#Parse the input JSON template into a python dictionary
templateFile = open("template.json", "r")
template = json.loads(templateFile.read())
templateFile.close()

outputFile = open("./reactFiles/" + template["templateName"] +".js", "w")

    # if template["templateType"] == "reactFunctional":
        

outputFile.close()
