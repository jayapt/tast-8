
class tv:
    def __init__(sony,price,inches,OnOffstatus,volume,channel,v=50,c=1):
        sony.price=price
        sony.inches=inches
        sony.OnOffstatus=OnOffstatus
        sony.volume=volume
        sony.channel=channel
        sony.v=v
        sony.c=c
    def decreasevolume(sony):
        if sony.volume>=100:
            sony.volume=sony.volume-10
            print("decreased the tv volume")
    def increasevolume(sony):
        if sony.volume>=0 & sony.volume<=100:
            sony.volume=sony.volume+10
            print("increased the tv volume ",sony.volume)
    def cha(sony):
        if sony.channel<=50:
            print("channel number is",sony.channel)
        else:
            print("invalid channel number")
    def resetTv(sony):
        print("tv reseted to default volume and channel")
        print("the default volume of tv is",sony.v)
        print("the default channel of tv is",sony.c)
    def status(sony):
        print("the sony tv is at channel number", sony.channel , "and volume of tv is",sony.volume)
class Led(tv):
    def __init__(sony,price,inches,ONOffstatus,volume,channel,screenthickness,energyusage,lifespan,refreshrate,viewingangle,backlight):
        super().__init__(price,inches,ONOffstatus,volume,channel)
        sony.screenthickness=screenthickness
        sony.energyusage=energyusage
        sony.lifespan=lifespan
        sony.refreshrate=refreshrate
        sony.viewingangle=viewingangle
        sony.backlight=backlight
        
    def display(sony):
        print("screen thickness is",sony.screenthickness)
        print("energy usage of tv is ",sony.energyusage)
        print("life span of tv is",sony.lifespan)
        print("refreshrate of tv is",sony.refreshrate)
        print("viewing angle of tv is",sony.viewingangle)
        print("backlight of tv is",sony.backlight)
class plasma(Led):
    pass   
t=plasma(50000,55,'onoff',10,30,1,'20kw','20years','0.5sec','31degress','75percent')  
t.increasevolume()
t.decreasevolume()
t.cha()
t.resetTv()
t.status()
t.display()

