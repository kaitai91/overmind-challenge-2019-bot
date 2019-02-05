
# Racial macro management module
# (c) kaitai
# Includes Townhalls, Production Buildings, Workers, Tech tree, and more
# TODO: Add unit production
# TODO: think whether text strings are sensible and maybe remove them
# TODO: more consistent way of using variables vs functions

from sc2 import Race
from sc2.ids.unit_typeid import *
from sc2.ids.ability_id import *

#NOTE: race_workers,race_townhalls and race_gas available for bot (following three will complement the file)
TOWN_HALL_TYPES = {Race.Protoss: UnitTypeId.NEXUS, Race.Terran: UnitTypeId.COMMANDCENTER, Race.Zerg: UnitTypeId.HATCHERY}
GAS_BUILDINGS = {Race.Protoss: UnitTypeId.ASSIMILATOR, Race.Terran: UnitTypeId.REFINERY, Race.Zerg: UnitTypeId.EXTRACTOR}
WORKER_TYPES = {Race.Protoss: UnitTypeId.PROBE, Race.Terran: UnitTypeId.SCV, Race.Zerg: UnitTypeId.DRONE}

#TODO: check UnitTypeIds for swarmhost
GATE_UNITS = {"Zealot": UnitTypeId.ZEALOT, "Sentry": UnitTypeId.SENTRY, "Stalker": UnitTypeId.STALKER,
              "Adept": UnitTypeId.ADEPT, "High Templar": UnitTypeId.HIGHTEMPLAR, "Dark Templar": UnitTypeId.DARKTEMPLAR}
ROBO_UNITS = {"Observer": UnitTypeId.OBSERVER, "Warp Prism": UnitTypeId.WARPPRISM, "Immortal": UnitTypeId.IMMORTAL,
              "Colossus": UnitTypeId.COLOSSUS, "Disruptor": UnitTypeId.DISRUPTOR}
STARGATE_UNITS = {"Phoenix": UnitTypeId.PHOENIX, "Oracle": UnitTypeId.ORACLE, "Void Ray": UnitTypeId.VOIDRAY,
                  "Tempest": UnitTypeId.TEMPEST, "Carrier": UnitTypeId.CARRIER}

BARRACKS_UNITS = {"Marine": UnitTypeId.MARINE, "Marauder": UnitTypeId.MARAUDER, "Reaper": UnitTypeId.REAPER,
                  "Ghost": UnitTypeId.GHOST}
FACTORY_UNITS = {"Hellion": UnitTypeId.HELLION, "Siege Tank": UnitTypeId.SIEGETANK, "Widow Mine": UnitTypeId.WIDOWMINE,
                 "Hellbat": UnitTypeId.HELLIONTANK, "Thor": UnitTypeId.THOR, "Cyclone": UnitTypeId.CYCLONE}
STARPORT_UNITS = {"Viking": UnitTypeId.VIKINGFIGHTER, "Medivac": UnitTypeId.MEDIVAC, "Raven": UnitTypeId.RAVEN,
                  "Banshee": UnitTypeId.BANSHEE, "Battlecruiser": UnitTypeId.BATTLECRUISER,
                  "Liberator": UnitTypeId.LIBERATOR}

HATCHERY_UNITS = {"Larva": UnitTypeId.LARVA, "Queen": UnitTypeId.QUEEN}
LARVA_UNITS = {"Drone": UnitTypeId.DRONE, "Overlord": UnitTypeId.OVERLORD, "Mutalisk": UnitTypeId.MUTALISK,
               "Zergling": UnitTypeId.ZERGLING, "Infestor": UnitTypeId.INFESTOR, "Roach": UnitTypeId.ROACH,
               "Swarm Host": UnitTypeId.SWARMHOSTMP, "Hydralisk": UnitTypeId.HYDRALISK, "Viper": UnitTypeId.VIPER,
               "Corruptor": UnitTypeId.CORRUPTOR, "Ultralisk": UnitTypeId.ULTRALISK}
# what (zerg) unit morphs into which (specified) unit
MORPH_UNITS = {UnitTypeId.OVERSEER: UnitTypeId.OVERLORD, UnitTypeId.BANELING: UnitTypeId.ZERGLING,
               UnitTypeId.RAVAGER: UnitTypeId.ROACH, UnitTypeId.LURKERMP: UnitTypeId.HYDRALISK,
               UnitTypeId.BROODLORD: UnitTypeId.CORRUPTOR}
MORPH_BUILDINGS = {UnitTypeId.HIVE: UnitTypeId.LAIR, UnitTypeId.LAIR: UnitTypeId.HATCHERY,
                   UnitTypeId.GREATERSPIRE: UnitTypeId.SPIRE}

MORPH = {
    #protoss

    #terran

    #zerg
    UnitTypeId.HATCHERY: AbilityId.UPGRADETOLAIR_LAIR, UnitTypeId.LAIR: AbilityId.UPGRADETOHIVE_HIVE,
    UnitTypeId.SPIRE: AbilityId.UPGRADETOGREATERSPIRE_GREATERSPIRE,

    UnitTypeId.OVERLORD: AbilityId.MORPH_OVERSEER, UnitTypeId.ZERGLING: AbilityId.MORPHZERGLINGTOBANELING_BANELING,
    UnitTypeId.ROACH: AbilityId.MORPHTORAVAGER_RAVAGER, UnitTypeId.HYDRALISK: AbilityId.MORPH_LURKER,
    UnitTypeId.CORRUPTOR: AbilityId.MORPHTOBROODLORD_BROODLORD, UnitTypeId.OVERLORDTRANSPORT: AbilityId.MORPH_OVERSEER
}
#secondary morph command(s) for units with more morph abilities (such as overlord)
MORPH2 = {
    # protoss

    # terran

    # zerg
    UnitTypeId.OVERLORD: AbilityId.MORPH_OVERLORDTRANSPORT
}

#commands to change mode (such as siegetank siege mode, observer stationary mode, prism phasing mode etc.
TRANSFORM = {
    # protoss
    UnitTypeId.GATEWAY: AbilityId.MORPH_WARPGATE, UnitTypeId.WARPGATE: AbilityId.MORPH_GATEWAY,

    UnitTypeId.OBSERVER: AbilityId.MORPH_SURVEILLANCEMODE,
    UnitTypeId.WARPPRISM: AbilityId.MORPH_WARPPRISMPHASINGMODE,

    UnitTypeId.OBSERVERSIEGEMODE: AbilityId.MORPH_OBSERVERMODE,
    UnitTypeId.WARPPRISMPHASING: AbilityId.MORPH_WARPPRISMTRANSPORTMODE,

    # terran
    UnitTypeId.SUPPLYDEPOT: AbilityId.MORPH_SUPPLYDEPOT_LOWER, UnitTypeId.HELLION: AbilityId.MORPH_HELLBAT,
    UnitTypeId.SIEGETANK: AbilityId.SIEGEMODE_SIEGEMODE, UnitTypeId.LIBERATOR: AbilityId.MORPH_LIBERATORAGMODE,
    UnitTypeId.VIKINGFIGHTER: AbilityId.MORPH_VIKINGASSAULTMODE,

    UnitTypeId.SUPPLYDEPOTLOWERED: AbilityId.MORPH_SUPPLYDEPOT_RAISE, UnitTypeId.HELLIONTANK: AbilityId.MORPH_HELLION,
    UnitTypeId.SIEGETANKSIEGED: AbilityId.UNSIEGE_UNSIEGE, UnitTypeId.LIBERATORAG: AbilityId.MORPH_LIBERATORAAMODE,
    UnitTypeId.VIKINGASSAULT: AbilityId.MORPH_VIKINGFIGHTERMODE,

    # zerg
    UnitTypeId.OVERSEER: AbilityId.MORPH_OVERSIGHTMODE,

    UnitTypeId.OVERSEERSIEGEMODE: AbilityId.MORPH_OVERSEERMODE,
}

UNITS_BY_FACILITY = \
    {Race.Protoss: {UnitTypeId.GATEWAY: GATE_UNITS, UnitTypeId.WARPGATE: GATE_UNITS,
                    UnitTypeId.ROBOTICSFACILITY: ROBO_UNITS, UnitTypeId.STARGATE: STARGATE_UNITS},
     Race.Terran: {UnitTypeId.BARRACKS: BARRACKS_UNITS, UnitTypeId.FACTORY: FACTORY_UNITS, UnitTypeId.STARPORT: STARPORT_UNITS},
     Race.Zerg: {UnitTypeId.HATCHERY: HATCHERY_UNITS, UnitTypeId.LARVA: LARVA_UNITS}}
# add these if needed UnitTypeId.LAIR: HATCHERY_UNITS, UnitTypeId.HIVE: HATCHERY_UNITS,

PROD_B_TYPES = \
    {Race.Protoss: {UnitTypeId.GATEWAY, UnitTypeId.WARPGATE, UnitTypeId.ROBOTICSFACILITY, UnitTypeId.STARGATE},
    Race.Terran: {UnitTypeId.BARRACKS, UnitTypeId.FACTORY, UnitTypeId.STARPORT},
    Race.Zerg: {UnitTypeId.HATCHERY, }}
# TECH_B_TYPES = \
#     {Race.Protoss: {UnitTypeId.NEXUS, UnitTypeId.PYLON, UnitTypeId.GATEWAY, UnitTypeId.CYBERNETICSCORE,
#                     UnitTypeId.ROBOTICSFACILITY, UnitTypeId.STARGATE, UnitTypeId.TWILIGHTCOUNCIL },
#     Race.Terran: {UnitTypeId.BARRACKS, UnitTypeId.FACTORY, UnitTypeId.STARPORT},
#     Race.Zerg: {UnitTypeId.HATCHERY, }}
# primary, [secondary]
SUPPLY_UNITS = {Race.Protoss: {UnitTypeId.PYLON, UnitTypeId.NEXUS},
                Race.Terran: {UnitTypeId.SUPPLYDEPOT, UnitTypeId.COMMANDCENTER},
                Race.Zerg: {UnitTypeId.OVERLORD, UnitTypeId.HATCHERY}}

AIR_TECH = \
    {Race.Protoss: {UnitTypeId.STARGATE},
     Race.Terran: {UnitTypeId.STARPORT},
     Race.Zerg: {UnitTypeId.SPIRE}}

#
TECH_TREE = {
    Race.Protoss: {
        UnitTypeId.NEXUS: {
            UnitTypeId.FORGE: {
                UnitTypeId.PHOTONCANNON: None
            },
            UnitTypeId.GATEWAY: {
                UnitTypeId.CYBERNETICSCORE: {
                    UnitTypeId.ROBOTICSFACILITY: {
                        UnitTypeId.ROBOTICSBAY: None
                    },
                    UnitTypeId.STARGATE: {
                        UnitTypeId.FLEETBEACON: None
                    },
                    UnitTypeId.TWILIGHTCOUNCIL: {
                        UnitTypeId.TEMPLARARCHIVE: None,
                        UnitTypeId.DARKSHRINE: None
                    },
                },
            },
        },
    },
    Race.Terran: {
        UnitTypeId.COMMANDCENTER: {
            UnitTypeId.ENGINEERINGBAY: {
                UnitTypeId.MISSILETURRET: None,
                UnitTypeId.SENSORTOWER: None},
        },
        UnitTypeId.SUPPLYDEPOT: {
            UnitTypeId.BARRACKS: {
                UnitTypeId.BUNKER: None,
                UnitTypeId.FACTORY: {
                    UnitTypeId.ARMORY: None,
                    UnitTypeId.GHOSTACADEMY: None,
                    UnitTypeId.STARPORT: {
                        UnitTypeId.FUSIONCORE: None
                    },
                },
            },
        },
    },
    Race.Zerg: {
        UnitTypeId.HATCHERY: {
            UnitTypeId.EVOLUTIONCHAMBER: None,
            UnitTypeId.SPAWNINGPOOL: {
                UnitTypeId.ROACHWARREN: None,
                UnitTypeId.BANELINGNEST: None,
                UnitTypeId.SPINECRAWLER: None,
                UnitTypeId.SPORECRAWLER: None,
                UnitTypeId.LAIR: {
                    UnitTypeId.NYDUSNETWORK: None,
                    UnitTypeId.HYDRALISKDEN: {
                        UnitTypeId.LURKERDENMP: None,
                    },
                    UnitTypeId.SPIRE: {
                        UnitTypeId.GREATERSPIRE: None,  # NOTE: in 2 places
                    },
                    UnitTypeId.INFESTATIONPIT: {
                        UnitTypeId.HIVE: {
                            UnitTypeId.GREATERSPIRE: None,  # NOTE: in 2 places
                            UnitTypeId.ULTRALISKCAVERN: None,
                        },
                    },

                },
            },
        },
    },  #MORE RACES
}


####ACTIONS

# TODO: simplify if needed
def train_unit(race, unit, building):  # <-pass building/larva
    """Action to train units

        For zerg pass larva instead of building
    """
    action = None
    if race == Race.Protoss:
        action = lambda: building.train(unit)
    elif race == Race.Terran:
        action = lambda: building.train(unit)

    elif race == Race.Zerg:
        action = lambda: building.train(unit)  # <-make larva("building") to unit

    return action


def goal_air_unit(race):
    goal_units = None
    if race == Race.Protoss:
        goal_units = (STARGATE_UNITS["Void Ray"], STARGATE_UNITS["Carrier"])
    elif race == Race.Terran:
        goal_units = (STARPORT_UNITS["Viking"], STARPORT_UNITS["Battlecruiser"])
    elif race == Race.Zerg:
        goal_units = (LARVA_UNITS["Mutalisk"], LARVA_UNITS["Mutalisk"])  # mutas are good

    return goal_units


def get_supply_args(race):
    if race == Race.Protoss:
        return (UnitTypeId.PROBE, UnitTypeId.PYLON)
    elif race == Race.Terran:
        return (UnitTypeId.SCV, UnitTypeId.SUPPLYDEPOT)
    elif race == Race.Zerg:
        return (UnitTypeId.LARVA, UnitTypeId.OVERLORD)

    return None


# example: get_available_buildings(Race.Protoss,[UnitTypeId.NEXUS, UnitTypeId.GATEWAY])
def get_available_buildings(race, buildings_ready):
    tree = TECH_TREE[race]
    building_set = set(buildings_ready)
    return search_tree(tree, building_set)


# recursive dict search tree "all children of the keys"
def search_tree(dict_tree, keys):
    found_keys = []
    for k in set(dict_tree.keys()):
        if dict_tree[k]:
            if k in set(keys):
                found_keys.extend(search_tree(dict_tree[k], keys))
    found_keys.extend(list(dict_tree.keys()))

    return found_keys


#returns tech path for given building or none if no tech path available/defined
def get_tech_path_needed(race, building):
    tree = TECH_TREE[race]
    found, path = search_path(tree, building)
    if found:
        return path
    else:
        return None


# recursive tree search "path to key"
# return path includes given key if path was found
# returns 2 GREATERSPIREs since it has two required tech paths
def search_path(dict_tree, key):
    found_keys = []
    found = False
    for k in set(dict_tree.keys()):
        path = []
        if k == key:
            found_keys.append(k)
        elif dict_tree[k]:
            _, path = search_path(dict_tree[k], key)
            if len(path) > 0:
                found_keys.append(k)
                found_keys.extend(path)
                # could use break statement if there was only one path to certain tech
                # however, greater spire needs two routes
                # (tech trees are small, I don't think the optimization is needed atm)
    if len(found_keys) > 0:
        found = True
    #print(found_keys)

    return found, found_keys

