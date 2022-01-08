#%% top

top=Class('top', None)

animal=Class('animal',top)
# Top
machine=Class('machine',top)
mammal=Class('mammal',animal)

# Mammal
whale=Class('whale',mammal)
elephant=Class('elephant',mammal)
human=Class('human',mammal)
mouse=Class('mouse',mammal)

# Machine
toy=Class('toy',machine)

top.print_tree_className()

#%% Class Properties

mammal.new_classProperties('has_legs', 'yes', 0)
mammal.new_classProperties('can_fly', 'no', 0)

whale.new_classProperties('has_legs', 'no', 0)

top.print_tree_properties()

#%% Class Relations
elephant.new_classRelations('hate', 'mouse', 0)

top.print_tree_relations()
#%%

whale.new_classInstances('monstruo')
whale.get_classInstance('monstruo').new_instRelations('hate', 'human', 0)

elephant.new_classInstances('Mrs Jumbo')
elephant.get_classInstance('Mrs Jumbo').new_instProperties('can_fly', 'yes', 0)
elephant.get_classInstance('Mrs Jumbo').new_instRelations('hate', 'the ringmaster', 0)

human.new_classInstances('the ringmaster')
human.new_classInstances('geppeto')
human.get_classInstance('geppeto').new_instRelations('hate', 'monstruo', 0)

mouse.new_classInstances('Mickey')
mouse.new_classInstances('Timothy')

toy.new_classInstances('Pinocchio')

top.print_tree_instances()

#%% a) Mostrar la extensión de la clase animal
updateAfterAnyChange()
print(class_extension(animal))

#%% b) Mostrar la extensión de la propiedad can_fly
updateAfterAnyChange()
print(property_extension('can_fly'))

#%% c) Mostrar las clases a las que pertenece geppeto
updateAfterAnyChange()      
print(clases_of('geppeto'))

#%% d) Añadir la clase insect como hija de animal. 
insect=Class('insect',animal)

# Añadir un individuo llamado ‘Jiminy Cricket’ a la clase insect. 
insect.new_classInstances('Jiminy Cricket')

# Para verificar, muestra de nuevo la extensión de la clase animal.
updateAfterAnyChange()
print(class_extension(animal))

#%% e) Añadir a la clase insect la propiedad can_fly=>no.
insect.new_classProperties('can_fly', 'no', 0)

# Para verificar, muestra de nuevo la extensión de la propiedad can_fly.
updateAfterAnyChange()
print(property_extension('can_fly'))

#%% f) Elimina la clase mouse. 
borrarClase(mouse)
# Para verificar, muestra de nuevo la extensión de la relación hate.
updateAfterAnyChange()
print(relation_extension('hate'))

#%% g) En la clase human, elimina la relación hate=>monstruo. 
human.borrarProperties('hate')

# Para verificar, muestra de nuevo la extensión de la relación hate.
updateAfterAnyChange()
print(relation_extension('hate'))
top.print_tree_relations()

#%% h) Cambia el nombre del individuo ‘the ringmaster’ por ‘circus leader’. 

human.borrarInstance('the ringmaster')
human.new_classInstances('circus leader')

# Para verificar, muestra de nuevo la extensión de la clase animal, y además la extensión de la relación hate.
updateAfterAnyChange()
print(class_extension(animal))
top.print_tree_relations()

#%% i) En la clase mammal, modifica el valor de la propiedad can_fly por yes.

mammal.modificarProperties('can_fly', 'yes')

# Para verificar, muestra la extensión de la propiedad can_fly.
updateAfterAnyChange()
print(property_extension('can_fly'))











