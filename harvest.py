############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.name = name

        self.code = code

        self.first_harvest = first_harvest

        self.color = color

        self.is_seedless = is_seedless

        self.is_bestseller = is_bestseller



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""


        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    muskmelon.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing(['strawberries', 'mint'])
    
    crenshaw = MelonType('cren', 1996, 'green', True, False, 'crenshaw')
    crenshaw.add_pairing('prosciutto')

    all_melon_types.extend([muskmelon, casaba, crenshaw])

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""


    for item in melon_types:

        print(f"{item.name} pairs well with {item.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}
    
    for melon in melon_types:
        melon_dict[melon.code] = melon.name
    return melon_dict


############
# Part 2   #

############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, typ, shape, color_rate, field, farmer, is_sellable):
        self.pairings = []

        self.typ = typ

        self.shape = shape

        self.color_rate = color_rate

        self.field = field

        self.farmer = farmer

        self.is_sellable = is_sellable

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons():
    """Returns a list of Melon objects."""
    all_melon_types = []
    
    melon1 = Melon("yw", 8, 7, 2, "Sheila", True)
    melon2 = Melon('yw', 3, 4, 2, 'Sheila', False)
    melon3 = Melon("yw", 9, 8, 3, "Sheila", False)


    all_melon_types.extend([melon1, melon2, melon3])

    return all_melon_types

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable == True:
            print(f'from field {melon.field} by {melon.farmer} is sellable')
        if melon.is_sellable == False:
            print(f'from field {melon.field} by {melon.farmer} is not sellable')
