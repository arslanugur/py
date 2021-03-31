from typing import List, Tuple


def kruskal(num_nodes: int, num_edges: int, edges: List[Tuple[int, int, int]]) -> int:
    """
    >>> kruskal(4, 3, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
    [(2, 3, 1), (0, 1, 3), (1, 2, 5)]
    >>> kruskal(4, 5, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
    [(2, 3, 1), (0, 2, 1), (0, 1, 3)]
    >>> kruskal(4, 6, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
    ... (2, 1, 1)])
    [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
    """
    edges = sorted(edges, key=lambda edge: edge[2]) #sorted: en küçük kenardan en büyük kenara, değerler olarak sıralanır

    parent = list(range(num_nodes))

    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []

    for edge in edges:
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            minimum_spanning_tree.append(edge)
            parent[parent_a] = parent_b

    return minimum_spanning_tree


if __name__ == "__main__":  # pragma: no cover
    num_nodes, num_edges = list(map(int, input().strip().split()))
    edges = []

    for _ in range(num_edges):
        node1, node2, cost = [int(x) for x in input().strip().split()]
        edges.append((node1, node2, cost))

    kruskal(num_nodes, num_edges, edges)

    
"""
En Kısa Tarama Ağacı - en kısa yoldan bütün düğümleri dolaşan algo
Kruskal algo edgeler kenarlar üzerinden gider
düğümler nodes v edges kenarlar
edge kavramı üzerinden gidersek ilk etapta sıralamamız gerekiyor
mesela 1 boyutuna sahip değişik yerde bulunan edgeler var  2 3 4 diye gider
algo aslında öncelikle bir edge list oluşturup küçükten büyüğe doğru sıralıyor
ardından bu edgeleri alarak devam ediyor. 
dikkat edilmesi gereken şey mesela x-v:1 dediğimizde x ve v nodeları var ve bunlar birbirine bağlanması söz konusu
visited x ve unvisited v durumu var
mesela x y z w diyelim bunlar ilk etapta sıfırdır ama visit edildikçe 1 olur
edge almak için ya ikisi de unvisited olcak ya da birisi unvisited olcak
şayet ikisi de visited ise o node alınmaz, yani zaten ziyaret edilmiş bir daha ikisine birden edge almaya gerek yok
bu algo en kısa şekilde dolaşarak tarama yapmayı sağlar -en az maliyetli  yol diyebiliriz - maliyetini sonuçların toplamını alarak yapabiliriz
iddiası ise bütün düğümleri dolaşan daha kısa maliyetli bir yol bulunamaz. O yol budur der
ama bir yerden bir yere gitmenin birden fazla yolu varsa eşit maliyetli olabilir
C de kodlarsak pratikte
kenarlara sayı verilir x ve y arasındaki edge
01234567 - edges
uxvyzstw - nodes
dönüşüm tablosu kullanarak çevirirsek
w-v:1
7-2:1 maliyeti 1
u-v:2 maliyet 2
...
graph - undirected graph yani iki yönlü gidilebiliyor
        directed graph olsaydı hangisini hangisinden old sırası önemli olurdu

"""
