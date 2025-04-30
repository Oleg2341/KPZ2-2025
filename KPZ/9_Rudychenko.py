import graphviz
from graphviz import Digraph
import subprocess
import os

def open_in_vscode(filepath):
    subprocess.run(['code', filepath], shell=True)

def create_interaction_diagram():
    diagram = Digraph(comment='Interaction Diagram')
    diagram.node('T', 'Trader')
    diagram.node('TS', 'Trading System')
    diagram.node('O', 'Order')
    diagram.node('SE', 'Stock Exchange')
    diagram.node('M', 'Module')
    diagram.edge('T', 'TS', 'ЗапитПозики (сума, умови)')
    diagram.edge('TS', 'O', 'СтворитиБорг (сума, відсотки)')
    diagram.edge('O', 'SE', 'РезервуватиКошти()')
    diagram.edge('SE', 'T', 'НадатиПозиченіКошти()')
    diagram.edge('T', 'M', 'ПовернутиБорг (сума, відсотки)')
    diagram.edge('M', 'SE', 'ЗакритиБорг()')
    diagram.edge('SE', 'O', 'ОновитиСтатусБоргу()')
    path = diagram.render('diagram1', format='png', cleanup=True)
    open_in_vscode(path)

def create_collaboration_diagram():
    diagram = Digraph(comment='Collaboration Diagram')
    diagram.node('T', 'Trader')
    diagram.node('TS', 'Trading System')
    diagram.node('O', 'Order')
    diagram.node('SE', 'Stock Exchange')
    diagram.node('M', 'Module')
    diagram.edge('T', 'TS', 'ЗапитПозики (сума, умови)')
    diagram.edge('TS', 'O', 'СтворитиБорг (сума, відсотки)')
    diagram.edge('O', 'SE', 'РезервуватиКошти()')
    diagram.edge('SE', 'T', 'НадатиПозиченіКошти()')
    diagram.edge('T', 'M', 'ПовернутиБорг (сума, відсотки)')
    diagram.edge('M', 'SE', 'ЗакритиБорг()')
    diagram.edge('SE', 'O', 'ОновитиСтатусБоргу()')
    path = diagram.render('diagram2', format='png', cleanup=True)
    open_in_vscode(path)

create_interaction_diagram()
create_collaboration_diagram()
