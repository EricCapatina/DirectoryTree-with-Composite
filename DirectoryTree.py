from abc import abstractmethod
from typing import List

root = 'Desktop'
linie = "│"
newfolder = "├──"
final = "└──"
files = [
        'meetings/2021-01-12/notes.txt',
        'meetings/2020_calendar.xlsx',
        'meetings/2021-01-12/report.pdf',
        'misc/photos/forest_20130430.jpg',
        'misc/photos/sunset_20130412.jpg',
        'scripts/tree.py',
        'meetings/2021-01-24/report.pdf'
]


def swap(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)
    return list


def append_to_tree(node, c):
    if not c:
        return
    if c[0] not in node:
        node[c[0]] = {}
    append_to_tree(node[c[0]], c[1:])


class DirectoryTreeComponent:

    def __init__(self, *args):
        self.name = args[0]


    @abstractmethod
    def show(self, level):
        pass


class DirectoryTreeGroup(DirectoryTreeComponent):

    def __init__(self, *args):
        super().__init__(*args)
        self.children = []

    def show(self, level):
        space = "|  "
        if level == 0:
            print(self.name)
        else:
            print(space * level + newfolder + self.name)
        for component in self.children:
            component.show(level + 1)

    def getItem(self, component):
        self.children.append(component)

    def removeItem(self, component):
        self.children.remove(component)


class DirectoryTreeLeaf(DirectoryTreeComponent):

    def __init__(self, *args):
        super().__init__(*args)

    def show(self, level):
        space = linie + "  " + linie + "  " * (level - 1)
        print(space + linie + "  " + newfolder + self.name)


def tree(root: str, files: List[str]):
    topLevelMenu = DirectoryTreeGroup(root)
    root = {}
    for path in swap(files, 1, 6):
        append_to_tree(root, path.split('/'))
    for i in root:
        index = DirectoryTreeGroup(i)
        topLevelMenu.getItem(index)
        for j in root[i]:
            next = DirectoryTreeGroup(j)
            index.getItem(next)
            for k in root[i][j]:
                file = DirectoryTreeLeaf(k)
                index.getItem(file)
    topLevelMenu.show(0)


tree(root, files)
