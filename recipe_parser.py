def ingrid_list():
    with open('./test/Панкейки.md') as f:
        f.readline()
        text = f.read()

    #получение списка ингридиентов
    header_spliter = '## '
    text = text.split(header_spliter, maxsplit=2)
    body = text[1].split('\n')
    rest_card = text[2] #оставшаяся карта в отдельной переменной
    ingrid = list()
    for line in body:
        if line.startswith('-'):
            ingrid.append(line[1:].strip().split(maxsplit=2))
    text_ing = ''
    for c in ingrid:
        c.extend([0, 0, 0, 0])
        text_ing += ' '.join(c)
    with open('./test/panki.md', 'w') as t:
        t.write()
    return ingrid


def main():
    print(ingrid_list())


if __name__ == '__main__':
    main()
