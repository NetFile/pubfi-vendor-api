from dataclasses import dataclass
import yaml

@dataclass
class Config:
    baseUrl: str
    vendorKey: str
    vendorSecret: str
    filingId: str
    filerAuthId: str
    filerAuthPassword: str

    def __init__(self, c):
        self.baseUrl = c['baseUrl']
        self.vendorKey = c['vendorKey']
        self.vendorSecret = c['vendorSecret']
        self.filingId = c['filingId']
        self.filerAuthId = c['filerAuthId']
        self.filerAuthPassword = c['filerAuthPassword']


def read_config():
    try:
        with open("../../config.yaml", 'r') as file:
            yamlConfig = yaml.safe_load(file)

        return Config(yamlConfig)

    except Exception as err:
        print(f'Error reading config: {err}')
        raise err

