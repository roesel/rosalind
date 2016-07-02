from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '')

def maxvalkey(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]+"\n"+str( format(v[v.index(max(v))], '.6f') )

def getGCcontent(buffer):
    return buffer.replace("G", "C").count("C")/len(buffer)*100

results = {}
datafile = open('rosalind_'+rid+'.txt', 'r').read().split(">") #(, "r") as datafile:
for line in datafile[1:]:
    split = line.split("\n", 1)
    id = split[0]
    data = split[1].replace("\n", "")
    results[id] = getGCcontent(data)
            
print maxvalkey(results)
            
            
