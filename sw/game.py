class Player(object):
    neutral = None

    def __init__(self):
        self.name = ""
        self.allies = []
        self.at_war = []
        self.fleets = []
        self.worlds = []
        self.score = []
        self.env = {}


class Population(object):
    default = None

    def __init__(self):
        # native types can be "Organic", "Robot"
        self.native_type = "Organic"
        self.native = 0
        self.hostile = {}


class Fleet(object):
    def __init__(self, **kwargs):
        self._owner = Player.neutral
        self._location = World.neutral
        self._state = {}
        self._ships = {}
        self._cargo = 0
        self._artifacts = []

        for key, value in kwargs.items():
            if "owner" == key:
                self.owner = value
            elif "location" == key:
                self.location = value
            elif "state" == key:
                self.state = value
            elif "ships" == key:
                self.ships = value
            elif "cargo" == key:
                self.cargo = value
            elif "artifacts" == key:
                self.artifacts = value

    def __repr__(self, *args, **kwargs):
        return "{}".format({'owner': self._owner,
                            'state': self._state,
                            'location': self._location,
                            'fleets': self._ships,
                            'artifacts': self._artifacts})

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def ships(self):
        return self._ships

    @ships.setter
    def ships(self, value):
        self._ships = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def artifacts(self):
        return self._artifacts

    @artifacts.setter
    def artifacts(self, value):
        self._artifacts = value

    @staticmethod
    def make_fleets():
        fs = []
        for i in range(1, 255):
            fs.append(Fleet(location=i))

        return fs


class World(object):
    neutral = None

    def __init__(self, **kwargs):
        self._owner = Player.neutral
        self._location = 0
        self._state = {}
        self._population_limit = 0
        self._population = 0
        self._industry = 0
        self._mines = 0
        self._metal = 0
        self._connections = []
        self._artifacts = []

        for key, value in kwargs.items():
            if "owner" == key:
                self.owner = value
            elif "location" == key:
                self.location = value
            elif "state" == key:
                self.state = value
            elif "population_limit" == key:
                self.population_limit = value
            elif "population" == key:
                self.population = value
            elif "industry" == key:
                self.industry = value
            elif "mines" == key:
                self.mines = value
            elif "metal" == key:
                self.metal = value
            elif "connections" == key:
                self.connections = value
            elif "artifacts" == key:
                self.artifacts = value

    @property
    def owner(self):
        return self._owner

    @property
    def location(self):
        return self._location

    @property
    def state(self):
        return self._state

    @property
    def connections(self):
        return self._connections

    @property
    def population_limit(self):
        return self._population_limit

    @property
    def population(self):
        return self._population

    @property
    def industry(self):
        return self._industry

    @property
    def mines(self):
        return self._mines

    @property
    def metal(self):
        return self._metal

    @property
    def artifacts(self):
        return self._artifacts

    @state.setter
    def state(self, value):
        self._state = value

    @owner.setter
    def owner(self, value):
        self._owner = value

    @location.setter
    def location(self, value):
        self._location = value

    @population_limit.setter
    def population_limit(self, value):
        self._population_limit = value

    @population.setter
    def population(self, value):
        self._population = value

    @industry.setter
    def industry(self, value):
        self._industry = value

    @mines.setter
    def mines(self, value):
        self._mines = value

    @metal.setter
    def metal(self, value):
        self._metal = value

    @connections.setter
    def connections(self, value):
        self._connections = value

    @artifacts.setter
    def artifacts(self, value):
        self._artifacts = value

    def __repr__(self, *args, **kwargs):
        return "{}".format({'owner': self._owner,
                            'connections': self._connections,
                            'state': self._state,
                            'population-limit': self._population_limit,
                            'population': self._population,
                            'industry': self._industry,
                            'mines': self._mines,
                            'metal': self._metal
                            })

    def fleets(self, fleets):
        return [f for f in fleets if f.location == self.location]

    @staticmethod
    def make_worlds(**kwargs):
        ws = []

        for i in range(0, 256):
            ws.append(World(location=i, onwer=Player.neutral, state="Idle"))
        return ws
