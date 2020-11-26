import pathlib
import os
import json
import re
Path = str(pathlib.Path().absolute()).replace('\src','') + '/dataset/'
filelist = os.listdir(Path)

######  Tratamento Datasets #####
DatasetWords =[]
for i in filelist:
 d={}
 with open(Path + i, 'r') as f:
    for ln in f: 
            wds = re.sub("[^0-9a-zA-Z]+", " ", ln)
            wds = wds.rstrip().lower().split()
            for w in wds:
                if d.get(w,-1) == -1: 
                 d[w]= d.get(w,i)
 
 DatasetWords.append(d)
 
MergedDatasets = {k:v for x in DatasetWords for k,v in x.items()}


#### Criação do dicionário de Dados ####
c = 1 
WordDictionary = {}
for wd in MergedDatasets.keys():
    WordDictionary[wd]= WordDictionary.get(wd,c)
    c = c + 1 

# Gerado arquivo json do dicionário para facilitar a visualização #
with open( 'WordDictionary.json', 'w') as dmp:  
    json.dump(WordDictionary,dmp,indent=2)     
      

## Function que vasculha as palavras dos DataSets ##
def SearchWord(pWord):  
  FoundList=[]
  for x in DatasetWords :
    n = x.get(pWord)
    if n!= None:
        FoundList.append(n)
  return FoundList


## Criando o Index ##
Index = {}
for idx in WordDictionary.items() :
    DocumentList = SearchWord(idx[0])
    SortedList = sorted(DocumentList,key=int)
    Index[idx[1]]= Index.get(idx[1],SortedList)
        
        
with open( 'index.json', 'w') as fjs:  
   json.dump(Index,fjs,indent=2)
        
    