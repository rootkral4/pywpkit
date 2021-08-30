import pywpkit


def main() -> None:
    """
    Example of wbrowsermethod function
    """
    kit = pywpkit.wpkit()

    kit.wbrowsermethod(
        "90537xxxxxxx",
        "wbrowser") # morethanone=["90537xxxxxxx","90537xxxxxxx"]
