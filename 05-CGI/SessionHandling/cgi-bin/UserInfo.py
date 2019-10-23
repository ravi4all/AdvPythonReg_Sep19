class UserSessionInfo():
    info = {}

    @staticmethod
    def getSession():
        return UserSessionInfo.info

    @staticmethod
    def setSession(value):
        sessId = value[0]
        email = value[1]
        UserSessionInfo.info[sessId] = email