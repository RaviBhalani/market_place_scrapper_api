from random import choice

from bs4 import BeautifulSoup
from requests import get
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from scrapper.constants import (
    DIV,
    CLASS,
    SPAN,
    TOTAL_PRODUCTS_ATTR,
    ANCHOR,
    ALL_PRODUCTS_IN_PAGE_ATTR,
    HREF,
    ID,
    NAME_ATTR,
    PRICE_ATTR,
    RATING_ATTR,
    REVIEW_ATTR,
    AVAILABILITY_ATTR, SUCCESS_MESSAGE, FAILURE_MESSAGE
)
from scrapper.helpers import get_required_data, get_required_data_from_nested_tags, get_all_data
from scrapper.serializers import ScrapperListSerializer
from scrapper.settings import USER_AGENT_LIST, LANGUAGE, AMAZON_INDIA_URL, PRODUCT_URL_KEY, WEBSITE_PAGE_KEY, PARSER


class ScrapperViewSet(GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return ScrapperListSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        if serializer.is_valid():

            # Pick a random user agent to avoid getting block by Amazon.
            headers = ({'User-Agent': choice(USER_AGENT_LIST), 'Accept-Language': LANGUAGE})
            page = str(serializer.validated_data['page'])

            # Split incoming product name and join the words of the product with plus in between to form the URL
            # required by Amazon.
            product_word_list = serializer.validated_data['product'].split(' ')
            product_url_value = product_word_list[0]
            for word in product_word_list[1:]:
                product_url_value += '+' + word

            url = AMAZON_INDIA_URL + PRODUCT_URL_KEY + product_url_value + WEBSITE_PAGE_KEY + page
            web_page = get(url, headers=headers)

            soup_obj = BeautifulSoup(web_page.content, PARSER)

            # Fetch total products from the web page.
            total_products = get_required_data_from_nested_tags(
                soup_obj=soup_obj,
                outer_html_tag=DIV,
                inner_html_tag=SPAN,
                outer_tag_attrs={CLASS: TOTAL_PRODUCTS_ATTR}
            )
            if total_products:
                total_products = total_products.split(' ')[3]

            product_data = {'page': int(page), 'total_products': total_products, 'product_list': list()}

            # Fetch all the products in a given page number.
            products = get_all_data(soup_obj=soup_obj, html_tag=ANCHOR, attrs={CLASS: ALL_PRODUCTS_IN_PAGE_ATTR})
            product_list = [link.get(HREF) for link in products]

            # Fetch details of individual product.
            for product in product_list:
                new_webpage = get(AMAZON_INDIA_URL + product, headers=headers)
                soup_obj = BeautifulSoup(new_webpage.content, PARSER)

                product_data['product_list'].append({
                    'Name': get_required_data(soup_obj=soup_obj, html_tag=SPAN, attrs={ID: NAME_ATTR}),
                    'Price': get_required_data(soup_obj=soup_obj, html_tag=SPAN, attrs={CLASS: PRICE_ATTR}),
                    'Rating': get_required_data(soup_obj=soup_obj, html_tag=SPAN, attrs={CLASS: RATING_ATTR}),
                    'Total Reviews': get_required_data(soup_obj=soup_obj, html_tag=SPAN, attrs={ID: REVIEW_ATTR}),
                    'Availability': get_required_data_from_nested_tags(
                        soup_obj=soup_obj,
                        outer_html_tag=DIV,
                        inner_html_tag=SPAN,
                        outer_tag_attrs={ID: AVAILABILITY_ATTR}
                    )
                })

            if product_data['product_list']:
                product_data['message'] = SUCCESS_MESSAGE
            else:
                product_data['message'] = FAILURE_MESSAGE
            return Response(status=HTTP_200_OK, data=product_data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)
