# Graph als Adjazenzliste
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Breitensuche (BFS)
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)  # erstes Element entnehmen
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  # Nachbarn hinzufügen
    return visited

# Tiefensuche (DFS)
def dfs(start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for nachbar in graph[start]:
            dfs(nachbar, visited)
    return visited

# Prüfen, ob ein Pfad zwischen zwei Knoten existiert (DFS)
def gibt_es_pfad(start, ziel, visited=None):
    if visited is None:
        visited = set()
    if start == ziel:
        return True
    visited.add(start)
    for nachbar in graph[start]:
        if nachbar not in visited:
            if gibt_es_pfad(nachbar, ziel, visited):
                return True
    return False

# Tests
print("BFS ab A:", bfs("A"))
print("DFS ab A:", dfs("A"))
print("Pfad von A nach F:", gibt_es_pfad("A", "F"))
print("Pfad von D nach C:", gibt_es_pfad("D", "C"))