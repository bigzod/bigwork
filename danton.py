danton=("de l'audace, encore de l'audace, toujours de l'audace")
target= ("audace")
def find_second(danton,target):
                s=danton.find(target)
                v=danton.find(danton,s+1)
                return(v)
print (find_second(danton,"audace"))