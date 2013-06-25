import csv
import codecs
from django.core.management.base import BaseCommand, CommandError

from inventory.models import Part, Place

MAPPING = [
	{'path': '*/egg',
	 ''},
]

def do_mapping(mapping=MAPPING):
	pass

def add_list(model, attribute, list):
	attr = getattr(model, attribute)
	for element in list:
		attr.add(element)

def add_single(model, attribute, value):
	pass
		
class Command(BaseCommand):
    args = '<filename>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        filename = args[0]
        self.stdout.write('Starting import of file "%s"' % filename)
        try:
            with open(filename, 'rb') as csvfile:
                reader = self.UnicodeDictReader(csvfile)
                for row in reader:

                    # Create list that describes the complete path to a place
                    # as tuples. Looks like [('place name', 'place type'), ...]
                    path_names = ['Room', 'Modul', 'Col', 'Row', 'Depth']
                    path = zip([row[x] for x in path_names ], path_names)

                    # recurse into the constructed path and get the place
                    place = self.get_or_create_place(path)

                    name = row['Name']
                    general = row['General Type']
                    specific = row['Specific Type']
                    from_value = self.to_float(row['From Value'].replace(',','.'))
                    to_value = self.to_float(row['To Value'].replace(',','.'))
                    unit = row['Unit']
                    package = row['Package']
                    note = row['Note']
                    remaining = row['Remaining']

                    # Make nice names
                    if name == '':
                        if specific != '':
                            name = '%s-%s' % (specific, general)
                        else:
                            name = general

                    part = Part.objects.create(name=name,
                                               place=place,
                                               general_type=general,
                                               specific_type=specific,
                                               from_value=from_value,
                                               to_value=to_value,
                                               unit=unit,
                                               package=package,
                                               note=note,
                                               remaining=remaining)
                    part.save()
                    self.stdout.write('Adding %s' % part)

        except Exception, e:
            print e

    def to_float(self, string_value):
        if string_value == '':
            return None
        else:
            try:
                float_value = float(string_value)
            except TypeError:
                self.stdout.write('Warning: Cannot convert %s to float.' % string_value)
                return None

    def get_or_create_place(self, path, parent=None):
        first = path[0]
        rest = path[1:]

        place = None
        name = first[0]
        type = first[1]

        try:
            place = Place.objects.filter(parent=parent).get(name=name)
        except Place.DoesNotExist:
            place = Place.objects.create(name=name, type=type, parent=parent)

        if len(rest) > 0:
            # Sometimes the path ends prematurely.
            if rest[0][0] == '':
                return place
            else:
                return self.get_or_create_place(rest, parent=place)
        else:
            return place

    def UnicodeDictReader(self, utf8_data, **kwargs):
        csv_reader = csv.DictReader(utf8_data, **kwargs)
        for row in csv_reader:
            yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])