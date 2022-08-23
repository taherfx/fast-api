# @app.get("/blog")
# def index(limit : int = 10, published: bool = True, sort: Optional[str] = None):
#     if published:
#         return f"{limit} list all published blogs"
#     else:
#         return f"{limit} list all blogs"

# @app.get('/blog/unplulished')
# def unplublished():
#     return "all unplublished blog"

# @app.get("/blog/{id}")
# def fetch_id(id: int):
#     return {"data": id}

# @app.get("/blog/{id}/comments")
# def comments(id):
#     return {"data": {1,2,3,4}}