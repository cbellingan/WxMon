from dataclasses import dataclass

class System:
    """
    Interface to system info required
    """
    @staticmethod
    def getmac(interface):
        "Return the mac address of the provided interface, only works on linux."
        try:
            # This isn't portable but is only expected to run on a pi
            mac = open('/sys/class/net/'+interface+'/address').readline()
        except: #TODO better failure handling here.
            mac = "00:00:00:00:00:00"
        return mac[0:17]


class Config:
    """
    Config handler, for now using a python modules to contain settings.
    """
    def __init__(self, service: str) -> None:
        import config as config_module
        self._service = service
        self.config = getattr(config_module, self._service)

    def list_attributes(self):
        return dir(self.config)


@dataclass
class Creds:
    """Primary interface to credentials"""
    username: str = None
    password: str = None

    @classmethod
    def get_creds(cls, service: str):
        cfg = Config(service).config
        return Creds(username=cfg.username, password=cfg.password)


