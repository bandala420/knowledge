
#%% function for getting all the nodes. 

def get_all_nodes(node, childList=[]):
    if len(node.classChilds)==0:
        childList.append(node)
        return childList
    else:
        childList.append(node)
        for child in node.classChilds:
            get_all_nodes(child, childList)  
        
        return childList



#%% Getting all the instances
def get_all_instances(node):
    nodesList=get_all_nodes(node, childList=[])
    
    instList=[]
    for i in nodesList:
        if i.classInstances:
            for j in i.classInstances:
                instList.append(j)
                # print(j.instName)

    return instList



#%% Append all the properties from a instances
def appendInstanceElements(inst, element):
    listRes=[]
    if element=='properties':
        listRes.append(inst.instProperties)
    elif element=='relations':
        listRes.append(inst.instRelations)
    p = inst.classContainer
    while p: 
        if element=='properties':
            item=p.classProperties
        elif element=='relations': 
            item=p.classRelations
            
        listRes.append(item)
        p=p.classParent
    
    flat_list = []
    for sublist in listRes:
        for item in sublist:
            flat_list.append(item)
    
    flat_list_noDup = []
    for item in flat_list:
        if item[0] not in [i[0] for i in flat_list_noDup]:
            flat_list_noDup.append(item)
        
    return flat_list_noDup

# propertiesInst=appendInstanceElements(instList[0], 'properties')
# relationsInst=appendInstanceElements(instList[0], 'relations')
            
#%% Properties and Relations dictionary of Instances with the hereditaric  


#%% Append all the properties from a class
def appendClassElements(node, element):
    listRes=[]
    p = node
    while p:
        if element=='properties':
            item=p.classProperties
        elif element=='relations': 
            item=p.classRelations            
        listRes.append(item)
        p=p.classParent
    
    flat_list = []
    for sublist in listRes:
        for item in sublist:
            flat_list.append(item)
    
    flat_list_noDup = []
    for item in flat_list:
        if item[0] not in [i[0] for i in flat_list_noDup]:
            flat_list_noDup.append(item)
        
    return flat_list_noDup

# propertiesClass=appendClassElements(instList[0].classContainer, 'properties')
# relationsClass=appendClassElements(instList[0].classContainer, 'relations')        


