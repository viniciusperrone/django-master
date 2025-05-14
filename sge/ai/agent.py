import json
from django.core import serializers
from django.conf import settings
from openai import OpenAI

from products.models import Product
from outflows.models import Outflow

from ai import prompts


class SGEAgent:

    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY,

        )

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()


        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows),
        })


    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT.replace('{{data}}', self.__get_data())
                }
            ]
        )

        result = response.choices[0].message.content

        return result
