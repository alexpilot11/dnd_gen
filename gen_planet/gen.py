import random
import requests
import sys

from gen_planet.planet import Planet


def main(num):
    for i in range(num):
        Planet().display()
