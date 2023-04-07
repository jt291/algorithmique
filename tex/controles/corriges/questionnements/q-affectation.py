# -*- coding: utf-8 -*-
 
annee           = 365*24*60*60
anneeLumiere    = 9.46053e15
atmosphere      = 1.01325e5
baril           = 0.15891
calorie         = 4.184
centimetre      = 1.0e-2
electronVolt    = 1.602189e-19
faraday         = 9.6487e4
foot            = 30.48e-2
franklin        = 3.33564e-10
frigorie        = 4.186e3
gallon          = 3.78541e-3
kilometreHeure  = 1.0e3/(60*60)
litre           = 1.0e-3
inch            = 2.54e-2
mile            = 1.609344e3
minute          = 60
noeud           = 0.514444
parsec          = 3.0857e16
pica            = 4.2175e-3
seconde         = 1
torr            = 133.3224

#-----------------------------------------------------------------------
def conversion(a1,a2) :
    print('a1 , a2 = ',eval(a1),',',eval(a2))
    print('n' + a2.title() + ' = n' + a1.title() + ' * a1/a2')
    print()
    return

#-----------------------------------------------------------------------
conversion('annee','minute')
conversion('anneeLumiere','mile')
conversion('baril','gallon')
conversion('anneeLumiere','parsec')
conversion('litre','gallon')
conversion('parsec','inch')
conversion('inch','pica')
conversion('mile','foot')
conversion('frigorie','calorie')
conversion('centimetre','pica')
conversion('electronVolt','frigorie')
conversion('franklin','faraday')
conversion('baril','litre')
conversion('parsec','foot')
conversion('annee','seconde')
conversion('electronVolt','calorie')
conversion('atmosphere','torr')
conversion('parsec','anneeLumiere')
conversion('foot','inch')
conversion('noeud','kilometreHeure')
conversion('mile','inch')
conversion('anneeLumiere','pica')
conversion('inch','foot')
conversion('litre','baril')
