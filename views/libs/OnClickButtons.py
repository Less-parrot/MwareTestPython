from views.libs.PushData import PushData

class OnClickButtons:

    
    def ActionnPushUser(e, ipServer):
        PushData("pushuser", ipServer)
        
    def ActionnPushSms(e, ipServer):
        PushData("pushsms", ipServer)

    def ActionnPushApp(e, ipServer):
        PushData("pushapp", ipServer)

    def ActionnGetIp(e, ipServer):
        PushData("getip", ipServer)
        
    def ActionnGetUser(e, ipServer):
        PushData("getuser", ipServer)

    def ActionnGetSms(e, ipServer):
        PushData("getsms", ipServer)

    def ActionnGetApp(e, ipServer):
        PushData("getapp", ipServer)
        
        

