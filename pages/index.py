from fasthtml.components import *
from fasthtml.svg import *


content = Body(
    Nav(
        Div(
            Label(
                Svg(
                    Title("menu"),
                    Path(d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"),
                    xmlns="http://www.w3.org/2000/svg",
                    width="20",
                    height="20",
                    viewbox="0 0 20 20",
                    cls="fill-current text-gray-900",
                ),
                fr="menu-toggle",
                cls="cursor-pointer md:hidden block",
            ),
            Input(type="checkbox", id="menu-toggle", cls="hidden"),
            Div(
                Nav(
                    Ul(
                        Li(
                            A(
                                "Shop",
                                href="#",
                                alt="Shopping cart logo",
                                cls="inline-block no-underline hover:text-black hover:underline py-2 px-4",
                            )
                        ),
                        Li(
                            A(
                                "About",
                                href="#",
                                cls="inline-block no-underline hover:text-black hover:underline py-2 px-4",
                            )
                        ),
                        cls="md:flex items-center justify-between text-base text-gray-700 pt-4 md:pt-0",
                    )
                ),
                id="menu",
                cls="hidden md:flex md:items-center md:w-auto w-full order-3 md:order-1",
            ),
            Div(
                A(
                    Svg(
                        Path(
                            d="M5,22h14c1.103,0,2-0.897,2-2V9c0-0.553-0.447-1-1-1h-3V7c0-2.757-2.243-5-5-5S7,4.243,7,7v1H4C3.447,8,3,8.447,3,9v11 C3,21.103,3.897,22,5,22z M9,7c0-1.654,1.346-3,3-3s3,1.346,3,3v1H9V7z M5,10h2v2h2v-2h6v2h2v-2h2l0.002,10H5V10z"
                        ),
                        xmlns="http://www.w3.org/2000/svg",
                        width="24",
                        height="24",
                        viewbox="0 0 24 24",
                        cls="fill-current text-gray-800 mr-2",
                    ),
                    "NORDICS",
                    href="#",
                    cls="flex items-center tracking-wide no-underline hover:no-underline font-bold text-gray-800 text-xl",
                ),
                cls="order-1 md:order-2",
            ),
            Div(
                A(
                    Svg(
                        Circle(fill="none", cx="12", cy="7", r="3"),
                        Path(
                            d="M12 2C9.243 2 7 4.243 7 7s2.243 5 5 5 5-2.243 5-5S14.757 2 12 2zM12 10c-1.654 0-3-1.346-3-3s1.346-3 3-3 3 1.346 3 3S13.654 10 12 10zM21 21v-1c0-3.859-3.141-7-7-7h-4c-3.86 0-7 3.141-7 7v1h2v-1c0-2.757 2.243-5 5-5h4c2.757 0 5 2.243 5 5v1H21z"
                        ),
                        xmlns="http://www.w3.org/2000/svg",
                        width="24",
                        height="24",
                        viewbox="0 0 24 24",
                        cls="fill-current hover:text-black",
                    ),
                    href="#",
                    cls="inline-block no-underline hover:text-black",
                ),
                A(
                    Svg(
                        Path(
                            d="M21,7H7.462L5.91,3.586C5.748,3.229,5.392,3,5,3H2v2h2.356L9.09,15.414C9.252,15.771,9.608,16,10,16h8 c0.4,0,0.762-0.238,0.919-0.606l3-7c0.133-0.309,0.101-0.663-0.084-0.944C21.649,7.169,21.336,7,21,7z M17.341,14h-6.697L8.371,9 h11.112L17.341,14z"
                        ),
                        Circle(cx="10.5", cy="18.5", r="1.5"),
                        Circle(cx="17.5", cy="18.5", r="1.5"),
                        xmlns="http://www.w3.org/2000/svg",
                        width="24",
                        height="24",
                        viewbox="0 0 24 24",
                        cls="fill-current hover:text-black",
                    ),
                    href="#",
                    cls="pl-3 inline-block no-underline hover:text-black",
                ),
                id="nav-content",
                cls="order-2 md:order-3 flex items-center",
            ),
            cls="w-full container mx-auto flex flex-wrap items-center justify-between mt-0 px-6 py-3",
        ),
        id="header",
        cls="w-full z-30 top-0 py-1",
    ),
    Div(
        Div(
            Input(
                type="radio",
                id="carousel-1",
                name="carousel",
                aria_hidden="true",
                hidden=True,
                checked="checked",
                cls="carousel-open",
            ),
            Div(
                Div(
                    Div(
                        Div(
                            P(
                                "Stripy Zig Zag Jigsaw Pillow and Duvet Set",
                                cls="text-black text-2xl my-4",
                            ),
                            A(
                                "view product",
                                href="#",
                                cls="text-xl inline-block no-underline border-b border-gray-600 leading-relaxed hover:text-black hover:border-black",
                            ),
                            cls="flex flex-col w-full lg:w-1/2 md:ml-16 items-center md:items-start px-6 tracking-wide",
                        ),
                        cls="container mx-auto",
                    ),
                    style="background-image: url('https://images.unsplash.com/photo-1422190441165-ec2956dc9ecc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1600&q=80');",
                    cls="block h-full w-full mx-auto flex pt-6 md:pt-0 md:items-center bg-cover bg-right",
                ),
                style="height:50vh;",
                cls="carousel-item absolute opacity-0",
            ),
            Label(
                "‹",
                fr="carousel-3",
                cls="prev control-1 w-10 h-10 ml-2 md:ml-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 left-0 my-auto",
            ),
            Label(
                "›",
                fr="carousel-2",
                cls="next control-1 w-10 h-10 mr-2 md:mr-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 right-0 my-auto",
            ),
            Input(
                type="radio",
                id="carousel-2",
                name="carousel",
                aria_hidden="true",
                hidden=True,
                cls="carousel-open",
            ),
            Div(
                Div(
                    Div(
                        Div(
                            P("Real Bamboo Wall Clock", cls="text-black text-2xl my-4"),
                            A(
                                "view product",
                                href="#",
                                cls="text-xl inline-block no-underline border-b border-gray-600 leading-relaxed hover:text-black hover:border-black",
                            ),
                            cls="flex flex-col w-full lg:w-1/2 md:ml-16 items-center md:items-start px-6 tracking-wide",
                        ),
                        cls="container mx-auto",
                    ),
                    style="background-image: url('https://images.unsplash.com/photo-1533090161767-e6ffed986c88?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjM0MTM2fQ&auto=format&fit=crop&w=1600&q=80');",
                    cls="block h-full w-full mx-auto flex pt-6 md:pt-0 md:items-center bg-cover bg-right",
                ),
                style="height:50vh;",
                cls="carousel-item absolute opacity-0 bg-cover bg-right",
            ),
            Label(
                "‹",
                fr="carousel-1",
                cls="prev control-2 w-10 h-10 ml-2 md:ml-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 left-0 my-auto",
            ),
            Label(
                "›",
                fr="carousel-3",
                cls="next control-2 w-10 h-10 mr-2 md:mr-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 right-0 my-auto",
            ),
            Input(
                type="radio",
                id="carousel-3",
                name="carousel",
                aria_hidden="true",
                hidden=True,
                cls="carousel-open",
            ),
            Div(
                Div(
                    Div(
                        Div(
                            P(
                                "Brown and blue hardbound book",
                                cls="text-black text-2xl my-4",
                            ),
                            A(
                                "view product",
                                href="#",
                                cls="text-xl inline-block no-underline border-b border-gray-600 leading-relaxed hover:text-black hover:border-black",
                            ),
                            cls="flex flex-col w-full lg:w-1/2 md:ml-16 items-center md:items-start px-6 tracking-wide",
                        ),
                        cls="container mx-auto",
                    ),
                    style="background-image: url('https://images.unsplash.com/photo-1519327232521-1ea2c736d34d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1600&q=80');",
                    cls="block h-full w-full mx-auto flex pt-6 md:pt-0 md:items-center bg-cover bg-bottom",
                ),
                style="height:50vh;",
                cls="carousel-item absolute opacity-0",
            ),
            Label(
                "‹",
                fr="carousel-2",
                cls="prev control-3 w-10 h-10 ml-2 md:ml-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 left-0 my-auto",
            ),
            Label(
                "›",
                fr="carousel-1",
                cls="next control-3 w-10 h-10 mr-2 md:mr-10 absolute cursor-pointer hidden text-3xl font-bold text-black hover:text-white rounded-full bg-white hover:bg-gray-900 leading-tight text-center z-10 inset-y-0 right-0 my-auto",
            ),
            Ol(
                Li(
                    Label(
                        "•",
                        fr="carousel-1",
                        cls="carousel-bullet cursor-pointer block text-4xl text-gray-400 hover:text-gray-900",
                    ),
                    cls="inline-block mr-3",
                ),
                Li(
                    Label(
                        "•",
                        fr="carousel-2",
                        cls="carousel-bullet cursor-pointer block text-4xl text-gray-400 hover:text-gray-900",
                    ),
                    cls="inline-block mr-3",
                ),
                Li(
                    Label(
                        "•",
                        fr="carousel-3",
                        cls="carousel-bullet cursor-pointer block text-4xl text-gray-400 hover:text-gray-900",
                    ),
                    cls="inline-block mr-3",
                ),
                cls="carousel-indicators",
            ),
            cls="carousel-inner relative overflow-hidden w-full",
        ),
        style="max-width:1600px;",
        cls="carousel relative container mx-auto",
    ),
    Section(
        Div(
            Nav(
                Div(
                    A(
                        "Store",
                        href="#",
                        cls="uppercase tracking-wide no-underline hover:no-underline font-bold text-gray-800 text-xl",
                    ),
                    Div(
                        A(
                            Svg(
                                Path(d="M7 11H17V13H7zM4 7H20V9H4zM10 15H14V17H10z"),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current hover:text-black",
                            ),
                            href="#",
                            cls="pl-3 inline-block no-underline hover:text-black",
                        ),
                        A(
                            Svg(
                                Path(
                                    d="M10,18c1.846,0,3.543-0.635,4.897-1.688l4.396,4.396l1.414-1.414l-4.396-4.396C17.365,13.543,18,11.846,18,10 c0-4.411-3.589-8-8-8s-8,3.589-8,8S5.589,18,10,18z M10,4c3.309,0,6,2.691,6,6s-2.691,6-6,6s-6-2.691-6-6S6.691,4,10,4z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current hover:text-black",
                            ),
                            href="#",
                            cls="pl-3 inline-block no-underline hover:text-black",
                        ),
                        id="store-nav-content",
                        cls="flex items-center",
                    ),
                    cls="w-full container mx-auto flex flex-wrap items-center justify-between mt-0 px-2 py-3",
                ),
                id="store",
                cls="w-full z-30 top-0 px-6 py-1",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1555982105-d25af4182e4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="364",
                        height="364",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1508423134147-addf71308178?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1449247709967-d4461a6a6103?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/reserve/LJIZlzHgQ7WPSh5KVTCB_Typewriter.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1467949576168-6ce8e2df4e13?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1544787219-7f47ccb76574?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1550837368-6594235de85c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            Div(
                A(
                    Img(
                        src="https://images.unsplash.com/photo-1551431009-a802eeec77b1?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&h=400&q=80",
                        alt="Product Name",
                        width="366",
                        height="366",
                        cls="hover:grow hover:shadow-lg",
                    ),
                    Div(
                        P("Product Name", cls=True),
                        Svg(
                            Path(
                                d="M12,4.595c-1.104-1.006-2.512-1.558-3.996-1.558c-1.578,0-3.072,0.623-4.213,1.758c-2.353,2.363-2.352,6.059,0.002,8.412 l7.332,7.332c0.17,0.299,0.498,0.492,0.875,0.492c0.322,0,0.609-0.163,0.792-0.409l7.415-7.415 c2.354-2.354,2.354-6.049-0.002-8.416c-1.137-1.131-2.631-1.754-4.209-1.754C14.513,3.037,13.104,3.589,12,4.595z M18.791,6.205 c1.563,1.571,1.564,4.025,0.002,5.588L12,18.586l-6.793-6.793C3.645,10.23,3.646,7.776,5.205,6.209 c0.76-0.756,1.754-1.172,2.799-1.172s2.035,0.416,2.789,1.17l0.5,0.5c0.391,0.391,1.023,0.391,1.414,0l0.5-0.5 C14.719,4.698,17.281,4.702,18.791,6.205z"
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            viewbox="0 0 24 24",
                            cls="h-6 w-6 fill-current text-gray-500 hover:text-black",
                        ),
                        cls="pt-3 flex items-center justify-between",
                    ),
                    P("£9.99", cls="pt-1 text-gray-900"),
                    href="#",
                ),
                cls="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col",
            ),
            cls="container mx-auto flex items-center flex-wrap pt-4 pb-12",
        ),
        cls="bg-white py-8",
    ),
    Section(
        Div(
            A(
                "About",
                href="#",
                cls="uppercase tracking-wide no-underline hover:no-underline font-bold text-gray-800 text-xl mb-8",
            ),
            Div(
                "Click for a joke",
                cls="myclass",
                hx_get="random_joke",
            ),
            P(
                "This template is inspired by the stunning nordic minimalist design - in particular:",
                Br(),
                A(
                    "Savoy Theme",
                    href="http://savoy.nordicmade.com/",
                    target="_blank",
                    cls="text-gray-800 underline hover:text-gray-900",
                ),
                "created by",
                A(
                    "https://nordicmade.com/",
                    href="https://nordicmade.com/",
                    cls="text-gray-800 underline hover:text-gray-900",
                ),
                "and",
                A(
                    "https://www.metricdesign.no/",
                    href="https://www.metricdesign.no/",
                    target="_blank",
                    cls="text-gray-800 underline hover:text-gray-900",
                ),
                cls="mt-8 mb-8",
            ),
            P(
                "Lorem ipsum dolor sit amet, consectetur",
                A("random link", href="#"),
                "adipiscing elit, sed do\n                eiusmod tempor incididunt ut labore et dolore magna aliqua. Vel risus commodo viverra maecenas accumsan\n                lacus vel facilisis volutpat. Vitae aliquet nec ullamcorper sit. Nullam eget felis eget nunc lobortis\n                mattis aliquam. In est ante in nibh mauris. Egestas congue quisque egestas diam in. Facilisi nullam\n                vehicula ipsum a arcu. Nec nam aliquam sem et tortor consequat. Eget mi proin sed libero enim sed\n                faucibus turpis in. Hac habitasse platea dictumst quisque. In aliquam sem fringilla ut. Gravida rutrum\n                quisque non tellus orci ac auctor augue mauris. Accumsan lacus vel facilisis volutpat est velit egestas\n                dui id. At tempor commodo ullamcorper a. Volutpat commodo sed egestas egestas fringilla. Vitae congue eu\n                consequat ac.",
                cls="mb-8",
            ),
            cls="container py-8 px-6 mx-auto",
        ),
        cls="bg-white py-8",
    ),
    Footer(
        Div(
            Div(
                Div(
                    Div(
                        H3("About", cls="font-bold text-gray-900"),
                        P(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel mi ut felis tempus\n                            commodo nec id erat. Suspendisse consectetur dapibus velit ut lacinia.",
                            cls="py-4",
                        ),
                        cls="px-3 md:px-0",
                    ),
                    cls="flex w-full lg:w-1/2",
                ),
                Div(
                    Div(
                        H3("Social", cls="text-left font-bold text-gray-900"),
                        Div(
                            A(
                                Svg(
                                    Path(
                                        d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"
                                    ),
                                    viewbox="0 0 24 24",
                                    cls="w-6 h-6 fill-current",
                                ),
                                href="#",
                                cls="mx-2",
                            ),
                            A(
                                Svg(
                                    Path(
                                        d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
                                    ),
                                    viewbox="0 0 24 24",
                                    cls="w-6 h-6 fill-current",
                                ),
                                href="#",
                                cls="mx-2",
                            ),
                            A(
                                Svg(
                                    Path(
                                        d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"
                                    ),
                                    viewbox="0 0 24 24",
                                    cls="w-6 h-6 fill-current",
                                ),
                                href="#",
                                cls="mx-2",
                            ),
                            A(
                                Svg(
                                    Path(
                                        d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.162-.105-.949-.199-2.403.041-3.439.219-.937 1.406-5.957 1.406-5.957s-.359-.72-.359-1.781c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.688 0 1.029-.653 2.567-.992 3.992-.285 1.193.6 2.165 1.775 2.165 2.128 0 3.768-2.245 3.768-5.487 0-2.861-2.063-4.869-5.008-4.869-3.41 0-5.409 2.562-5.409 5.199 0 1.033.394 2.143.889 2.741.099.12.112.225.085.345-.09.375-.293 1.199-.334 1.363-.053.225-.172.271-.401.165-1.495-.69-2.433-2.878-2.433-4.646 0-3.776 2.748-7.252 7.92-7.252 4.158 0 7.392 2.967 7.392 6.923 0 4.135-2.607 7.462-6.233 7.462-1.214 0-2.354-.629-2.758-1.379l-.749 2.848c-.269 1.045-1.004 2.352-1.498 3.146 1.123.345 2.306.535 3.55.535 6.607 0 11.985-5.365 11.985-11.987C23.97 5.39 18.592.026 11.985.026L12.017 0z"
                                    ),
                                    viewbox="0 0 24 24",
                                    cls="w-6 h-6 fill-current",
                                ),
                                href="#",
                                cls="mx-2",
                            ),
                            cls="w-full flex items-center py-4 mt-0",
                        ),
                        cls="px-3 md:px-0",
                    ),
                    cls="flex w-full lg:w-1/2 lg:justify-end lg:text-right mt-6 md:mt-0",
                ),
                cls="w-full mx-auto flex flex-wrap",
            ),
            cls="container flex px-3 py-8",
        ),
        cls="container mx-auto bg-white py-8 border-t border-gray-400",
    ),
    cls="bg-white text-gray-600 work-sans leading-normal text-base tracking-normal",
)
