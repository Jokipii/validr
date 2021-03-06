from validr import T, Compiler, modelclass, asdict


@modelclass
class Model:
    user = T.dict(userid=T.int.min(0).max(9).desc("UserID"))
    tags = T.list(T.int.min(0))
    style = T.dict(
        width=T.int.desc("width"),
        height=T.int.desc("height"),
        border_width=T.int.desc("border_width"),
        border_style=T.str.desc("border_style"),
        border_color=T.str.desc("border_color"),
        color=T.str.desc("color"),
    )
    optional = T.str.optional.desc("unknown value")


compiler = Compiler()
default = compiler.compile(T(Model))


def model(value):
    return asdict(Model(value))


CASES = {"default": default, "model": model}
