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
        self._ships = 0
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
                            'ships': self._ships,
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
    def make_fleets(count=256, **kwargs):
        fs = []

        for i in range(0, count):
            fs.append(Fleet(**kwargs))
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

    def fleets_at_location(self, fleets):
        return [f for f in fleets if f.location == self.location]

    @staticmethod
    def make_worlds(count=256, **kwargs):
        ws = []

        for i in range(0, count):
            ws.append(World(**kwargs))
        return ws


def make_home_world(owner, w: World):
    w.owner = owner
    w.population_limit = 20
    w.population = 10
    w.industry = 10
    w.mines = 10
    w.metal = 20


def make_home_fleet(name, home, fs: [Fleet]):
    for f in fs:
        f.location = home
        f.owner = name


class Player(object):
    neutral = None

    def __init__(self, _game, **kwargs):
        self.name = ""
        self.home = 0
        self.type = "Merchant"
        self.allies = []
        self.at_war = []
        self.fleets = []
        self.worlds = []
        self.score = []
        self.env = {}

        for key, value in kwargs.items():
            if "name" == key:
                self.name = value
            elif "home" == key:
                self.home = value
            elif "type" == key:
                self.type = value
            elif "allies" == key:
                self.allies = value
            elif "at_war" == key:
                self.at_war = value
            elif "fleets" == key:
                self.fleets = [_game["Fleets"][i] for i in value]
            elif "score" == key:
                self.score = value
            elif "env" == key:
                self.env = value

            make_home_world(self.name, _game["Worlds"][self.home])
            make_home_fleet(self.name, self.home, self.fleets)

    @staticmethod
    def make_players(_game):
        return [
            Player(_game, name="Neutral_1", home=1, type="Merchant", allies=None, at_war=False, fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_2", home=20, type="Merchant", allies=None, at_war=False, fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_3", home=40, type="Merchant", allies=None, at_war=False, fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_4", home=80, type="Merchant", allies=None, at_war=False, fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_5", home=100, type="Merchant", allies=None, at_war=False,
                   fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_6", home=120, type="Merchant", allies=None, at_war=False,
                   fleets=[1, 2, 3, 4, 5],
                   score=0, env={}),
            Player(_game, name="Neutral_7", home=140, type="Merchant", allies=None, at_war=False,
                   fleets=[1, 2, 3, 4, 5],
                   score=0, env={})
        ]


game = {"Worlds": World.make_worlds(),
        "Fleets": Fleet.make_fleets()}

game["Players"] = Player.make_players(game)
