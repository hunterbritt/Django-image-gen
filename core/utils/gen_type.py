


def get_generation_type(gen_type: str = None, url: str =None):
    """ 
        This is a helper function used to determined the generation type 
    """
    match (gen_type):
        case "HD":
            hd_url = url
            return hd_url
        case "FAST":
            fast_url = url
            return fast_url
        case "BASE":
            base_url = url
            return base_url
        case _:
            default_url = url
            return default_url
