class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}

    def insert(self, route):
        self.children[route] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        current_node = self.root

        for path in paths:
            if path not in current_node.children:
                current_node.children[path] = RouteTrieNode()
            current_node = current_node.children[path]

        current_node.handler = handler

    def find(self, paths):
        current_node = self.root

        for path in paths:
            if path not in current_node.children:
                return None
            current_node = current_node.children[path]

        return current_node.handler


class Router:
    def __init__(self, handler, not_found_handler="404"):
        self.routes = RouteTrie()
        self.routes.insert("/", handler)
        self.not_found = not_found_handler

    def add_handler(self, route, handler):
        paths = self.split_path(route)
        self.routes.insert(paths, handler)

    def lookup(self, route):
        paths = self.split_path(route)
        return self.routes.find(paths) or self.not_found

    def split_path(self, route):
        if len(route) == 1:
            return ["/"]
        else:
            return route.strip("/").split("/")


# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))
# root handler

print(router.lookup("/home"))
# not found handler

print(router.lookup("/home/about"))
# about handler

print(router.lookup("/home/about/"))
# about handler

print(router.lookup("/home/about/me"))
# not found handler
