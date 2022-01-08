def updateAfterAnyChange():    
    nodesList=get_all_nodes(top, childList=[])
    instList=get_all_instances(top)
    
    dictPropertiesInst={}
    dictRelationsInst={}
    # i=instList[0]
    for i in instList:
        dictPropertiesInst[i.instName] = appendInstanceElements(i, 'properties')
        dictRelationsInst[i.instName] = appendInstanceElements(i, 'relations')
    
        
    #%% Properties and Relations dictionary of Instances with the hereditaric  
    dictPropertiesClass={}
    dictRelationsClass={}
    # i=instList[0]
    for i in nodesList:
        dictPropertiesClass[i.className] = appendClassElements(i, 'properties')
        dictRelationsClass[i.className] = appendClassElements(i, 'relations')

#%% La extensión de una clase
def class_extension(classObject):
    nodesList=get_all_nodes(classObject, childList=[])
    class_extension=[]
    for i in nodesList:
        class_extension.append(i.className)
    return class_extension

#q1=class_extension(animal)

#%% La extensión de una propiedad
def property_extension(propertyName):
    listOfKeys = []    
    for item in dictPropertiesInst.items():
        for elem in item[1]:
            # print(elem[1])
            if elem[0] == propertyName:
                listOfKeys.append([item[0],elem[1]])  
    return listOfKeys

#q2=property_extension('can_fly')

#%% La extensión de una relación
def relation_extension(relationName):
    listOfKeys = []    
    for item in dictRelationsInst.items():
        for elem in item[1]:
            # print(elem[1])
            if elem[0] == relationName:
                listOfKeys.append([item[0],elem[1]])  
    return listOfKeys

#q3=relation_extension('engraver')
#%% Todas las propiedades de un objeto
def properties_of_individual(name):
    return dictPropertiesInst[name]

#q4=properties_of_individual('selenografia_alzate_jcb')

#%% Todas las propiedades de una clase
def properties_of_class(name):
    return dictPropertiesClass[name]

# q5=properties_of_class('selenografia_alzate')

#%% Todas las relaciones de un objeto
def relations_of_individual(name):
    return dictRelationsInst[name]

#q6=relations_of_individual('selenografia_alzate_jcb')

#%% Todas las relaciones de un objeto o clase
def relations_of_class(name):
    return dictRelationsClass[name]

#q7=relations_of_class('selenografia_alzate')

#%% Todas las clases a las que pertenece un objeto

def clases_of(name):
    listParents=[]
    for inst in instList:
        if inst.instName==name:
            p=inst.classContainer
            while p: 
                listParents.append(p.className)
                p=p.classParent
    return listParents
            
#q8=clases_of('selenografia_alzate_jcb')











    