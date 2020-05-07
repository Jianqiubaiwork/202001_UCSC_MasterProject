import csv

from apps.bail_judgement.models import *

SRC_CSV_PATH = 'media/compas_test.csv'

def run():
    fhand = open(SRC_CSV_PATH)
    reader = csv.reader(fhand)

    BailJudgementModel.objects.all().delete()

    for row in reader:
        print(row)

        # first = BailJudgementModel.objects.get_or_create(first=row[2])
