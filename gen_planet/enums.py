from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def values(cls):
        return [v.value for v in cls]


class Plane(BaseEnum):
    MATERIAL = 'Material'
    FEYWILD = 'Feywild'
    SHADOWFELL = 'Shadowfell'
    MECHANUS = 'Mechanus'
    LIMBO = 'Limbo'
    PANDEMONIUM = 'Pandemonium'
    THE_ABYSS = 'The Abyss'
    CARCERI = 'Carceri'
    HADES = 'Hades'
    GEHENNA = 'Gehenna'
    THE_NINE_HELLS = 'The Nine Hells'
    ACHERON = 'Acheron'
    ARCADIA = 'Arcadia'
    MOUNT_CELESTIA = 'Mount Celestia'
    BYTOPIA = 'Bytopia'
    ELYSIUM = 'Elysium'
    THE_BEASTLANDS = 'The Beastlands'
    ARBOREA = 'Arborea'
    YSGARD = 'Ysgard'


class Size(BaseEnum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    HUGE = 'Huge'
    GIANT = 'Giant'


class Density(BaseEnum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


class Gravity(BaseEnum):
    VERY_LIGHT = 'Very Light'
    LIGHT = 'Light'
    MEDIUM = 'Medium'
    HEAVY = 'Heavy'
    VERY_HEAVY = 'Very Heavy'


class Population(BaseEnum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    HUGE = 'Huge'
    GIANT = 'Giant'
    NONE = None


class Conflict(BaseEnum):
    WAR = 'War'
    POLITICAL_LAND_BOUNDARIES = 'Political land boundaries'
    CITIZEN_LAND_BOUNDARIES = 'Citizen land boundaries'
    THEFT = 'Theft'
    CRIME_GANGS = 'Crime - gangs'
    CRIME_SLAVERY = 'Crime - slavery'
    CRIME_DOMESTIC_ABUSE = 'Crime - domestic abuse'
    POLITIAL_POWER_STRUGGLE = 'Politial power struggle'
    NONE = None


class RawMaterials(BaseEnum):
    PRECIOUS_METAL_ORE = 'Precious metal ore'
    PRECIOUS_GEMS = 'Precious gems'
    USEFUL_METAL_ORE = 'Useful metal ore'
    VEGETATION = 'Vegetation'
    WOOD = 'Wood'
    MAGIC = 'Magic metal'
    GAS_MEDICAL = 'Gas - medical'
    FUEL_GAS = 'Fuel - gas'
    FUEL_COAL_LIKE = 'Fuel - coal-like'
    NONE = None


class Economy(BaseEnum):
    RAW_MATERIALS = 'Raw materials'
    MERCHANT = 'Merchant'
    BLACK_MARKET = 'Black market'
    NONE = None
