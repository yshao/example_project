from fasthtml.common import *
from fasthtml.fastapp import fast_app

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML on Vercel!", P("Welcome to FastHTML deployed on Vercel!"))

serve()
