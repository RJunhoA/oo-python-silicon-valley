from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:
    all = []
    def __init__(self, name, founder, domain):
        self.name = name
        self.founder = founder
        self.domain = domain
        Startup.all.append(self)

    def pivot(self, domain, name):
        self.domain = domain
        self.name = name

    @classmethod
    def find_by_founder(cls, founder):
        for startup in cls.all:
            if startup.founder == founder:
                return startup
            
    @classmethod
    def domains(cls):
        return {s.domain for s in cls.all}