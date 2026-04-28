class Routes:
    BASE_URL = "https://dummyjson.com"

    #product
    GET_ALL_PRODUCTS  = "/products"
    GET_PRODUCT_BY_ID = "/products/{id}"
    GET_PRODUCTS_WITH_LIMIT = "/products?limit={limit}"
    GET_PRODUCTS_SORTED = "/products?sortBy=price&order={order}"
    GET_ALL_CATEGORIES = "/products/categories"
    GET_PRODUCTS_BY_CATEGORY = "/products/category/{category}"
    CREATE_PRODUCT = "/products/add"
    UPDATE_PRODUCT = "/products/{id}"
    DELETE_PRODUCT = "/products/{id}"

    #cart
    GET_ALL_CARTS = "/carts"
    GET_CART_BY_ID = "/carts/{id}"
    GET_USER_CART = "/carts/user/{userId}"
    CREATE_CART = "/carts/add"
    UPDATE_CART = "/carts/{id}"
    DELETE_CART = "/carts/{id}"

    #users
    GET_ALL_USERS = "/users"
    GET_USER_BY_ID = "/users/{id}"
    GET_USERS_WITH_LIMIT = "/users?limit={limit}"
    GET_USERS_SORTED = "/users?sortBy=firstName&order={order}"
    CREATE_USER = "/users/add"
    UPDATE_USER = "/users/{id}"
    DELETE_USER = "/users/{id}"

    #Auth
    CREATE_LOGIN = "/auth/login"
    GET_CURRENT_USER = "/auth/me"