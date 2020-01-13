import win32con
import win32security


class DatabaseImpersonate:
    def __init__(self):
        self.domain = '<domain>'
        self.login = '<username>'
        self.password = '<password>'
        self.handel = None

    def logon(self):
        self.handel = win32security.LogonUser(self.login,
                                              self.domain,
                                              self.password,
                                              win32con.LOGON32_LOGON_INTERACTIVE,
                                              win32con.LOGON32_PROVIDER_DEFAULT)
        win32security.ImpersonateLoggedOnUser(self.handel)

    def logoff(self):
        win32security.RevertToSelf()
        self.handel.Close()
