from xml.dom import minidom
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
from models.nodes import Node, graphList


def analyzeXML(filename):
    patterns: list = []
    rows: int = 0
    columns: int = 0
    flip: float = 0
    swap: float = 0

    domtree = xml.dom.minidom.parse(filename)
    pisoArtesanal = domtree.documentElement

    pisos = pisoArtesanal.getElementsByTagName('nombre')
    for piso in pisos:
        print('========PISO=================')
        if piso.hasAtrribute('nombre'):
            print('nombre: '.format(piso.getAttribute('nombre')))
