{% if cookiecutter.include_normalizer  -%}
from .normalizer import ExampleNormalizer
{%- endif %}
{% if cookiecutter.include_parser  -%}
 from .parser import *
{%- endif %}
{% if cookiecutter.include_schema  -%}
 from .schema import *
{%- endif %}
