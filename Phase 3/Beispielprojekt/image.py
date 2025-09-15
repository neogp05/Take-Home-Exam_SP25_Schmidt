from pgm import read_pgm, write_pgm
from collections import deque


def create_mask(width, height, data, threshold):
    mask = []
    for value_pixel in data:
        if value_pixel < threshold:
            mask.append(0)
        else: mask.append(255)
    return mask 

def create_graph(width, height, mask):
    graph = {}
    for i in range(width*height):
        graph[i] = []
    neighbors = [(-1, 0), (1, 0), (0, -1), (0,1)]
    for y in range(height):
        for x in range(width):
            index = x + y * width
            value = mask[index]

            for dist_x, dist_y in neighbors:
                neighbor_x = x + dist_x
                neighbor_y = y + dist_y
                if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                    neighbor_index = neighbor_x + neighbor_y * width
                    neighbor_value = mask[neighbor_index]
                    if value == neighbor_value:
                        graph[index].append(neighbor_index)
    return graph

def connected_components(graph):
    labels = [None] * len(graph)
    anchors = [None] * len(graph)
    current_label = 0
    
    for node in range(len(graph)):
        if labels[node] is not None:
            continue
        stack = deque()
        stack.append(node)
        while len(stack) != 0:
            new_node = stack.pop()
            if labels[new_node] is not None:
                continue
            labels[new_node] = current_label
            anchors[new_node] = node
            for neighbor in graph[new_node]:
                if labels[neighbor] is not None:
                    continue
                stack.append(neighbor)
        current_label  +=1
    return labels, current_label

def get_size(labels):
    max_label = max(labels)
    size = [0]* (max_label +1)
    for label in labels: 
        size[label] +=1
    return size 

def get_max_intensity(data, labels):
    max_label = max(labels)
    intensity = [0] * (max_label +1)
    for index_pixel, label in enumerate(labels):
        if data[index_pixel] > intensity[label]:
            intensity[label] = data[index_pixel]

    return intensity

def segment(labels, size, intensity): 
    segmentation = []

    for label in labels:
        if label == 0:
            segmentation.append(0)
        elif size[label] < 30:
            segmentation.append(255)
        elif intensity[label] > 220:
            segmentation.append(160)
        else:
            segmentation.append(80)
    return segmentation 

if __name__ == "__main__":
    
    width, height, data = read_pgm('cells.pgm')
 
    mask = create_mask(width, height, data, 60)
    write_pgm(width, height, mask, 'mask.pgm')

   
    graph = create_graph(width, height, mask)

   
    labels, n_components = connected_components(graph)
    write_pgm(width, height, labels, 'labels.pgm')
   

    size = get_size(labels)
    intensity = get_max_intensity(data, labels)

    segmentation = segment(labels, size, intensity)
    write_pgm(width, height, segmentation, 'segmentation.pgm')

    total = width * height
    background = (size[0]/ total) * 100
    
    region_small = sum(1 for i in range(1, len(size)) if size[i] < 30)
    white = sum(1 for i in range(1, len(intensity)) if intensity[i] > 220)

    print(f"Background percentage = {background}")
    print(f"Small Regions = {region_small}")
    print(f"White cells = {white}")