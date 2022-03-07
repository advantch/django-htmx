import django_tables2 as tables


class SearchMetricsTable(tables.Table):

    id = tables.Column()
    client_ip = tables.Column()
    user_id = tables.Column()
    url = tables.Column()
    search_term = tables.Column()

    class Meta:
        row_attrs = {
            "data-id": lambda record: record.id,
            "hx-get": lambda record: reverse("record-preview", args=[record.id]),
            "hx-trigger": "click",
            "hx-target": "#record-preview",
        }
