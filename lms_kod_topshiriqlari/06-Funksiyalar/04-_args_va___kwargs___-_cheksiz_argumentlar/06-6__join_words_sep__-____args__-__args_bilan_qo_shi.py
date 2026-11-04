def join_words(sep='-', *args):
    return sep.join(args)
sep = input()
sozlar = input().split()
print(join_words(sep, *sozlar))