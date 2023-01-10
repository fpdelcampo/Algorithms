class Node:
    def __init__(self, value=0, children=[]) -> None:
        self.value = value
        self.children = children

def recursive_dfs(root, visited, order):
    for i in root.children:
        if i.value not in visited:
            order.append(i.value)
            visited.add(i.value)
            recursive_dfs(i, visited, order)
    return order

def iterative_dfs(root, vertices):
    visited = [False for _ in range(vertices)]
    stack = [] # As we add a node, we try to "remove" it
    stack.append(root)
    order = []
    while len(stack)!=0:
        next = stack.pop()
        if not visited[next.value-1]:
            order.append(next.value)
            visited[next.value-1] = True
            for i in next.children:
                if not visited[i.value-1]:
                    stack.append(i)
    return order

def iterative_bfs(root, vertices):
    visited = [False for _ in range(vertices)]
    queue = [] # As we add a node, we try to "remove" it
    queue.append(root)
    order = []
    while len(stack)!=0:
        next = queue.pop(0)
        if not visited[next.value-1]:
            order.append(next.value)
            visited[next.value-1] = True
            for i in next.children:
                if not visited[i.value-1]:
                    queue.append(i)
    return order


def main():
    """
    
    Initialize the graph and test the algorithm
    
    """

    Node1 = Node(1, [])
    Node2 = Node(2, [])
    Node3 = Node(3, [])
    Node4 = Node(4, [])
    Node5 = Node(5, [])
    Node6 = Node(6, [])
    Node7 = Node(7, [])
    Node8 = Node(8, [])
    
    Node1.children.extend([Node2, Node3, Node4, Node5, Node6, Node7])
    Node2.children.extend([Node1, Node3, Node5, Node7])
    Node3.children.extend([Node1, Node2, Node4])
    Node4.children.extend([Node1, Node3])
    Node5.children.extend([Node1, Node2])
    Node6.children.extend([Node1, Node7, Node8])
    Node7.children.extend([Node1, Node2, Node6])
    Node8.children.extend([Node6, Node7])

    order = recursive_dfs(Node1, set([Node1.value]), [Node1.value])
    print(order)

    order = iterative_dfs(Node1, 8)
    print(order)

    order = iterative_dfs(Node1, 8)
    print(order)

if __name__ == "__main__":
    main()
