# coding:utf-8

def printing_models(unprinted_models, completed_models=[]):
    while unprinted_models:
        completed_model = unprinted_models.pop()
        completed_models.append(completed_model)
    return completed_models


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


a = ['iphone case', 'robot pendant', 'dodecahedron']
b = []
printing_models(a, b)
show_completed_models(b)

