"""Elastic search python script."""
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q, Search


def searching(title="", category=""):
    """Connect to the elasticsearch server."""
    client = Elasticsearch()
    q = Q(
        "bool", should=[Q("match", title=title), Q("match", category=category)]
    )
    s = Search(using=client, index="researches").query(q)[0:20]
    response = s.execute()
    search = get_results(response)
    return search


def get_results(response):
    """Return the search results."""
    results = []
    for hit in response:
        results_tuple = (hit.title, hit.category)
        results.append(results_tuple)
    return results
