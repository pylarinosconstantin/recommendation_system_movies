import pandas as pd
import matplotlib.pyplot as plt
import math



#eisagogi stoixeion
#o pinakas twn xristwn
U=pd.read_csv("users.csv","\t")
#o pinakas twn tainion
M=pd.read_csv("movies.csv","\t", encoding="ISO-8859-1")
#o pinakas twn vathmologiwn
R=pd.read_csv("ratings.csv",";", encoding="ISO-8859-1")


#synartisi pou vriskei tin omoiotita metaxi dio xriston

def common(id1,id2):
    d=0
    #parnoume tin lista twn xristwn
    LU=list(U["user_id"])
    try:
        #elegxoume an yparxoun oi dyo xristes
        idx1=LU.index(id1)
        idx2=LU.index(id2)
        #koitame ta koina xaraktiristika diladi ilikia , filo, epaggelma
        if(U["age_desc"][idx1]==U["age_desc"][idx2]):
            d=d+3
        if(U["gender"][idx1]==U["gender"][idx2]):
            d=d+1
        if(U["occ_desc"][idx1]==U["occ_desc"][idx2]):
            d=d+1
            
        if(U["occupation"][idx1]==U["occupation"][idx2]):
            d=d+1
           
       
        #an exouem koina metrame poses koines tainies exoun
        if(d>3):
            #pairnoume tis tainies tou protou xristi
            R1=R[R["user_id"]==id1]
            #parinoume tis tainies tou defterou xristi
            R2=R[R["user_id"]==id2]
            
            #vriskoume tis koines
            R3=R1[R1["movie_id"].isin(list(R2["movie_id"]))]
            #an oi tainies exoun mia sxetika koini vatmologis (idio gousto)
            for m in list(R3["movie_id"]):
                rr1=R1[R1["movie_id"]==m]
                rr2=R2[R2["movie_id"]==m]
                if(abs(rr1["rating"].iloc[0]-rr2["rating"].iloc[0])<2):
                    #tote afxanoume kata mia posotita to d 
                    d=d+0.5
            
    except:
        d=0
        
    #epistrefoume tin omoiotita
    return d    


def ncommon(id1,id2):
    return common(id1,id2)/common(id1,id1)

#kirios programma
while(True):
    #dimoume to menou
    print("1. Recommend a movie for a user")
    print("2. Show Plots of Data")
    print("3. Exit")
    print("----------------------------------------")
    choice=input("Give choice:")
    
    #an dosei 1
    if(choice=="1"):    
            try:
                #zitame gia poion xristi theloume na paroume apotelesmata
                idu=int(input("give user id:"))
                #parinoume tin lista ton xriston kai psaxnoume 
                
                UL=list(U["user_id"])
                #to xristi mas sti lista
                inx=UL.index(idu)
                
                #pairnoume tin ilsta me to dianisma me tis kalyuteres tainies
                L={}
                for i in UL:
                    print(i,end=" ")
                    if(i!=idu):
                        L[i]=common(idu,i)
                
                
                L2=sorted(L.items(), key=lambda x: x[1], reverse=True)
                x=L2[0][0]
                R1=R[R["user_id"]==idu]
                R2=R[R["user_id"]==x]
                try:
                    R3=R2[~R2["movie_id"].isin(list(R1["movie_id"]))]
                    R4=R3[R3["rating"]>=4]
                    for m in list(R4["movie_id"]):
                        mm=M[M["movie_id"]==m]
                        print(mm["title"].iloc[0])
                except:
                   print("error")
                
            except:
                print("user not found")
    if(choice=="2"):
        #provoli stoixeiwn plithismou

        plt.hist(U["gender"])
        plt.show()
        
        plt.hist(U["age"])
        plt.show()
        
        C={}
        Mv=[]
        for m in range(len(M)):
           
            mm=M["genres"][m]
            kat=mm.split("|")
            x=[]
            x.append(M["movie_id"][m])
            x.append(kat)
            Mv.append(x)
            for cc in kat:
                try:
                    C[cc]=C[cc]+1
                except:
                    C[cc]=1
        
        plt.bar(range(len(C)), list(C.values()), align='center')
        plt.xticks(range(len(C)), list(C.keys()))
        plt.show()
    
    if(choice=="3"):
        break

