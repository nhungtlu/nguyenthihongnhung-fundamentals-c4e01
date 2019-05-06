hangtonkho = {
    'vang' : 500,
    'tui' : ['da lua', 'twine', 'da quy'],
    'balo' : ['xylophone', 'dao gam','bedroll','o banh my']
}
hangtonkho['tui'] = ''
print(hangtonkho)

hangtonkho['tui'] = ['vo so', 'qua mong la','lint']
print(hangtonkho)

del hangtonkho['balo'][1]
print(hangtonkho)

hangtonkho['vang'] += 50
print(hangtonkho)
