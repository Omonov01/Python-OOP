import pickle
file = 'experience.txt'

with open(file,'w') as f:
    """" we write information to wxperience.txt file """
    f.write('sanjar'+'\n')
    f.write('2000')
    


talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    """we write information at pickle format """
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    
with open('info','rb') as file:
    """" we read information from pickle format """
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)