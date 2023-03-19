with open("C:/Users/Mon Pepe/Desktop/hr_system.txt") as employes:
    for employe in employes:
        #print(employe)

        eachEmployee=employe.split()
        print(f"{eachEmployee[0]} (Id: {eachEmployee[1]}), {eachEmployee[2]} -${format(int(eachEmployee[3]),'.2f')}")