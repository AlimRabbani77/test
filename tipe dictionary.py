#dic 
dic = {"sasuke":24,"sakura":23,"hinata":45} 
itms = dic.items() 
for i,j in itms:  
    print(i,":",j)  

#mengupdate 
dic = {"sasuke":24,"sakura":23,"hinata":45} 
dic["sasuke"] = 100 
print(dic) 

#menghapus 
dic = {"sasuke":24,"sakura":23,"hinata":45} 
del dic["sasuke"] 
print(dic) 

#menambahkan 
dic = {"sasuke":24,"sakura":23,"hinata":45} 
dic["kakasi"]=78 
print(dic)