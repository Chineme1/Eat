from bs4 import BeautifulSoup
import requests

def scrape_all(loc): #give it the address
    page = requests.get(loc)
    soup = BeautifulSoup(page.text, 'lxml')
    locationid = ""
    name = ""
    address =""
    line1 = ""

    #print(soup)
    if(str(soup).lower().find("freefood")> -1 or str(soup).lower().find("free food") >-1):
        if(str(soup).lower().find("locationid")> -1):
            astr =str(soup).lower().find("locationid")
            start =12
            tmpstr =""
            while True:
                if(str(soup).lower()[astr+start]==","):
                    break
                tmpstr += str(soup).lower()[astr+start]
                astr+=1
            
        locationid = tmpstr
        astr += start

        #name
        astr+=8 #to miss the "name:" part and go to something else
        start =0
        tmpstr=""
        while True:
            if(str(soup).lower()[astr+start]==","):
                break
            tmpstr += str(soup).lower()[astr+start]
            astr+=1
        
        name = tmpstr

        #address
        astr+=1
        tmpstr=""
        while True:
            if(tmpstr[len(tmpstr)-5:]=="line1"):
                break
            tmpstr += str(soup).lower()[astr+start]
            astr+=1
        
        address= tmpstr[tmpstr.find(":")+1:len(tmpstr)-7]

        #StartOn
        strts=""
        tmpstr = ""
        astr = str(soup).lower().find("startson")
        astr+=10
        while True and astr != 9:
            if(str(soup).lower()[astr]==","):
                break
            tmpstr += str(soup)[astr]
            astr+=1

        strts=tmpstr

        #Endson
        ends=""
        tmpstr = ""
        astr = str(soup).lower().find("endson")
        astr+=8
        while True and astr != 7:
            if(str(soup).lower()[astr]==","):
                break
            tmpstr += str(soup)[astr]
            astr+=1

        ends=tmpstr

        #location
        location=""
        astr= str(soup).lower().find("strong>location:")
        astr+= 16
        tmpstr=""
        while True and astr!= 15:
            if(tmpstr[len(tmpstr)-7:]=="</span>"):
                tmpstr = tmpstr.split('>')[2]
                tmpstr = tmpstr.split('<')[0]
                break
            tmpstr += str(soup).lower()[astr]
            astr+=1
        location=tmpstr

        #title shit
        title=""
        astr= str(soup).lower().find("imageurl")
        tmpstr = ""
        while True:
            if(tmpstr[len(tmpstr)-4:]=="name"):
                break
            tmpstr += str(soup).lower()[astr]
            astr+=1

        astr+=3
        tmpstr=""
        while True:
            if(tmpstr[len(tmpstr)-1:]==","):
                break
            tmpstr += str(soup)[astr]
            astr+=1
        title= tmpstr[:len(tmpstr)-2]
        #print("Free Food Available")
        #print("title: ", title)

        final_location = ""
        if(location !=""):
            final_location = location
        else:
            if(locationid !="null" and locationid !=""):
                final_location = locationid
            
            if(len(final_location)>0):
                final_location += "\n"
    
            if(address !="null" and address != ""):
                final_location += address
            
            if(len(final_location)>0):
                final_location += "\n"

            if(name != "null" and name != ""):
                final_location += name

                

        '''print("locationid: ",locationid)
        print("address: ", address)
        print("name: ",name)
        print("Location: ", location)
        print("Start Time: ", strts)
        print("End Time: ", ends)
        print("Final Location: ", final_location)'''
        return [title, final_location, strts, ends]
    else:
        #print("No free food")
        return None


