from flask import jsonify, request
from flask_restx import Model
from flask_restx.fields import Boolean, DateTime, Integer, List, Nested, String, Url
from flask_restx import marshal

pagination_model = pagination_model = Model(
    "Pagination",
    {
        "has_prev": Boolean,
        "has_next": Boolean,
        "page": Integer,
        "total_pages": Integer(attribute="pages"),
        "items_per_page": Integer(attribute="per_page"),
        "total_items": Integer(attribute="total"),
    }
)

class PaginationUtils:
    @staticmethod
    def paginate(query, schema):
        args = request.args

        page = 1
        size = 20

        try:
            page = int(args.get("page"))
            size = int(args.get("size"))
        except:
            pass

        pagination = query.paginate(page, size, error_out=False)
        pagination_data = marshal(pagination, pagination_model)

        data = marshal(pagination.items, schema)

        return jsonify({
            "data": data,
            "pagination": pagination_data
        })



