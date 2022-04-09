import meilisearch
from django.conf import settings


class SearchIndex:
    index = None

    class Indexes:
        """Available indexes"""

        app = "app"

    def __init__(self, index=None):
        self.index = index or self.Indexes.app

    def get_index(self):
        """Retrieve index"""
        client = meilisearch.Client(
            settings.MEILISEARCH_URL, settings.MEILISEARCH_API_TOKEN
        )
        return client.index(self.index)

    def delete_doc(self, doc):
        self.get_index().delete_document(doc)

    def delete_all(self):
        self.get_index().delete_all_documents()


search_index = SearchIndex().get_index()
