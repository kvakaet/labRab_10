#!usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ABC = {'poiuytrewqlkjhgfdsamnbvcxz'}

    A = {'c', 'f', 'g', 'k'}
    B = {'e', 'f', 'g', 'm', 'q'}
    C = {'h', 'i', 'r', 'w', 'x'}
    D = {'b', 'e', 'j', 'u', 'z'}

    X = A.difference(B).intersection(C.union(D))

    not_B = ABC.difference(B)
    not_C = ABC.difference(C)
    Y = A.difference(D).union(not_C.difference(not_B))
    print(X)
    print(Y)
