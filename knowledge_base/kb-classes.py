#%%

#https://www.youtube.com/watch?v=4r_XR9fUPhQ

#%% class Instances
class Instances:
    def __init__(self, instName, classContainer):
        self.classContainer = classContainer
        self.instName = instName
        self.instProperties = []
        self.instRelations = []
    
    def new_instProperties(self, name, instProperty, preferencia):
        self.instProperties.append([name, instProperty, preferencia])
    
    def new_instRelations(self, name, relationObject, preferencia):
        self.instRelations.append([name,relationObject,preferencia])

    def eliminarPropiedad(self, valorElimnar):
        for datos in self.instProperties:
            if datos[0] == valorElimnar:
                self.instProperties.remove(datos)

    def eliminarRelaciones(self, valorElimnar):
        for datos in self.instRelations():
            if datos[0] == valorElimnar:
                self.instRelations.remove(datos)   
    
    def modificarPropiedad(self, propiedad, nuevoValor):
        for id,datos in enumerate(self.instProperties):
            if datos[0] == propiedad:
                self.instProperties[id][1] = nuevoValor
    def modificarRelaciones(self, relacion, nuevoValor):
        for id,datos in enumerate(self.instRelations()):
            if datos[0] == relacion:
                self.instRelations[id][1] = nuevoValor
        
#%%
class Class:
    def __init__(self, className, classParent = None):
        self.className = className
        self.classParent = classParent
        self.classProperties = []
        self.classRelations = []
        self.classInstances = []
        self.classChilds = []
        
        if classParent != None:
            classParent.classChilds.append(self)
       
    def add_child(self, child):
        child.classParent=self
        self.classChilds.append(child)
    
    def get_classParentName(self):
        if self.classParent==None:
            parentName='None'
        else: 
            parentName=self.classParent.get_className()
        return parentName

    def new_classProperties(self, name, isTrue, preferencia):
        self.classProperties.append([name,isTrue,preferencia])
        
    def delete_classProperties(self, name, isTrue, preferencia):
        self.classProperties.append([name,isTrue,preferencia])
    
    def new_classRelations(self, name, isTrue, preferencia):
        self.classRelations.append([name,isTrue,preferencia])
             
    def new_classInstances(self, name):
        self.classInstances.append(Instances(name, self))
        
    def get_classInstance(self, name):
        for instance in self.classInstances:
            if instance.instName==name:
                return instance
    
    def list_classInstances(self):
        aux=[]
        for instance in self.classInstances:
            aux.append(instance.instName)
        return aux
    
    def list_childs(self):
        aux=[]
        for instance in self.classChilds:
            aux.append(instance.className)
        return aux
    
    def to_print(self):
        print('Name: ', self.className)
        print('Instances: ', self.list_classInstances())
          
    def print_tree_className(self):
        spaces = ' ' * self.get_level() * 5
        spaces = spaces + '|__ '
        print(spaces + self.className)
        if self.classChilds:
            for child in self.classChilds:
                child.print_tree_className()
    
    def print_tree_properties(self):
        spaces = ' ' * self.get_level() * 5
        spaces = spaces + '|__ '
        print(spaces + self.className + str(self.classProperties))
        if self.classChilds:
            for child in self.classChilds:
                child.print_tree_properties()
                
    def print_tree_relations(self):
        spaces = ' ' * self.get_level() * 5
        spaces = spaces + '|__ '
        print(spaces + self.className + str(self.classRelations))
        if self.classChilds:
            for child in self.classChilds:
                child.print_tree_relations() 
    
    def print_tree_instances(self):
        spaces = ' ' * self.get_level() * 5
        spaces = spaces + '|__ '
        print(spaces + self.className + str(self.list_classInstances()))
        if self.classChilds:
            for child in self.classChilds:
                child.print_tree_instances()
    
    def get_level(self):
        level = 0
        p = self.classParent
        while p: 
            level+=1
            p=p.classParent
        return level
    
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<Borrar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

    
    def borrarProperties(self, propiedadBorrar):
        for propiedades in self.classProperties:
            if(propiedades[0]==propiedadBorrar):
                self.classProperties.remove(propiedades)
    def borrarRelations(self, propiedadBorrar):
        for relaciones in self.classRelations:
            if(relaciones[0]==propiedadBorrar):
                self.classRelations.remove(relaciones)

    
    #.....................................................................................
    #Borrar para instancias
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
    
    def borrarInstance(self, objeto):
        bandera = False
        for instance in range(len(self.classInstances)):
            #print(self.classInstances[instance].instName)
            if bandera==True:
                return
            if self.classInstances[instance].instName==objeto:
                self.classInstances.remove(self.classInstances[instance])
                bandera= True

    def borrarInstancePropiedades(self, objeto):
        for instance in range(len(self.classInstances)):
            #print(self.classInstances[instance].instName)
            self.classInstances[instance].eliminarPropiedad(objeto)
    
    def borrarInstanceRelaciones(self, objeto):
        for instance in range(len(self.classInstances)):
            #print(self.classInstances[instance].instName)
            self.classInstances[instance].eliminarRelaciones(objeto)
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    #//////////////////////////////////////////////////////////////////////////////
    # modificar propiedad, relacion de clase
    def modificarProperties(self, propiedad, nuevoValor):
        for id,propiedades in enumerate(self.classProperties):
            if(propiedades[0]==propiedad):
                self.classProperties[id][1] = nuevoValor
    def modificarRelations(self, relacion, nuevoValor):
        for id,relaciones in enumerate(self.classRelations):
            if(relaciones[0]==relacion):
                self.classRelations[id][1]=nuevoValor
    def modificarInstancia(self, objeto, nuevoObjeto):
        bandera = False
        for instance in range(len(self.classInstances)):
            if bandera==True:
                return
            if self.classInstances[instance].instName==objeto:
                self.classInstances[instance] = nuevoObjeto
                bandera= True

    def modificarInstanciaPropiedades(self, propiedad, nuevoValor):
        for instance in range(len(self.classInstances)):
            self.classInstances[instance].modificarPropiedad(propiedad,nuevoValor)
    
    def modificarInstanciaRelaciones(self, relacion, nuevoValor):
        for instance in range(len(self.classInstances)):
            self.classInstances[instance].modificarRelaciones(relacion,nuevoValor)
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
#%%


  