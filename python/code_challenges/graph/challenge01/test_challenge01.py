# Write your test here
import pytest
from challenge01 import *

def test_breadth_first_traversal():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    b = graph.add_node('b')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node("h")
    i = graph.add_node("i")
    k = graph.add_node("k")

    graph.add_edge( a,  c)
    graph.add_edge( a,  e)
    graph.add_edge( a,  b)
    graph.add_edge( c,  f)
    graph.add_edge( b,  d)
    graph.add_edge( e,  g)
    graph.add_edge( e,  d)
    graph.add_edge( e,  f)
    graph.add_edge( f,  i)
    graph.add_edge( f,  h)
    graph.add_edge( g, h)
    graph.add_edge( h, k)
    graph.add_edge( i, k)

    result=graph.breadth_first_traversal(a)
    expected=[a, c, e, b, f, g, d, i, h, k]
    assert result == expected



