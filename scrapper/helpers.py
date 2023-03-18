from bs4 import BeautifulSoup


def get_all_data(soup_obj: BeautifulSoup = None, html_tag: str = None, attrs: dict = None) -> list:
    """
    :param soup_obj: BeautifulSoup class object.
    :param html_tag: HTML tag name.
    :param attrs: HTML tag attributes in dictionary format.
    :return: Required data in string format or empty string in case of exception.
    """
    try:
        return soup_obj.find_all(html_tag, attrs=attrs)
    except Exception as e:
        return list()


def get_required_data(soup_obj: BeautifulSoup = None, html_tag: str = None, attrs: dict = None) -> str:
    """
    :param soup_obj: BeautifulSoup class object.
    :param html_tag: HTML tag name.
    :param attrs: HTML tag attributes in dictionary format.
    :return: Required data in string format or empty string in case of exception.
    """
    try:
        return soup_obj.find(html_tag, attrs=attrs).string.strip()
    except Exception as e:
        return ''


def get_required_data_from_nested_tags(
        soup_obj: BeautifulSoup = None,
        outer_html_tag: str = None,
        inner_html_tag: str = None,
        outer_tag_attrs: dict = None
) -> str:
    """
    :param soup_obj: BeautifulSoup class object.
    :param outer_html_tag: HTML tag name.
    :param inner_html_tag: HTML tag name.
    :param outer_tag_attrs: HTML tag attributes in dictionary format.
    :return: Required data in string format or empty string in case of exception.
    """
    try:
        return soup_obj.find(outer_html_tag, attrs=outer_tag_attrs).find(inner_html_tag).string.strip()
    except Exception as e:
        return ''
