'''
A solucao do problema consiste em transformar o Grafo não dirigido em 
um grafo dirigido onde todos os nos com valor k menor que C apontam apenas
para o no k + 1.

Por exemplo, no primeiro caso de teste, a tabela de adjacência fica,
para o grafo original:

0 | 1 2 3
1 | 0 2 3
2 | 0 1 3
3 | 0 1 2

Como C no primeiro caso é 3, então o alvo é a cidade número 2,
assim a tabela de adjacência fica:

0 | 1
1 | 2
2 | 0 1 3
3 | 0 1 2

Aí é só executar o algoritimo de dijkstra sobre o novo grafo.
'''

from data_struct import GRAPH , HEAP_MIN
from sys import maxsize

def get_input( ):

    while True:

        seq = input()
        if seq == "0 0 0 0":
            break

        N , M , C , K = map( int , seq.split() )

        G = GRAPH()
        for i in range( N ):
            G.add_node( i )

        for j in range( M ):
            u , v , w = map( int , input().split() )
            G.add_edge( u , v , w )

        yield G , C , K

def init_globals( K ):

    global ACM , NXT

    #--------------------------------------------------
    # peso acumulado de cada vertice na busca em largura
    # iniciando em K
    ACM = [ maxsize ]*250
    ACM[ K ] = 0
    
    #--------------------------------------------------
    # O no ancestral na busca de dijkstra.
    NXT = [ None ]*250
    NXT[ K ] = K

def relax( u , v , w ):
    
    #--------------------------------------------------
    # verifica se a aresta u , v é melhor que a conexão
    # atual do vértice v
    v1 = ACM[ u ] + w( u , v )
    v2 = ACM[ v ]

    if v1 < v2:
        ACM[ v ] = v1
        NXT[ v ] = u

def main( G , C , K ):
    
    '''
    Execução de um algoritimo de dijkstra. Com o twist
    descrito no inicio desse arquivo.
    '''

    tab = G.Adj_tab()
    for v in range( C - 1 ):
        tab[ v ] = [ v + 1 ]

    init_globals( K )
    H = HEAP_MIN()
    for u in G.nodes:
        H[ u ] = ACM[ u ]
    
    w = lambda x , y : G.edge_val( x , y )
    while H:
        u, _  = H.pop()
        for v in tab[ u ]:
            if H[v] is None: continue
            relax( u , v , w )
            H[ v ] = ACM[ v ]
    return ACM[ C - 1 ]

if __name__ == "__main__":

    S = get_input()
    for G , C , K in S:
        result = main( G , C , K )
        print( result )
