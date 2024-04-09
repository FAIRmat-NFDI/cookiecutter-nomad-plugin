{% if cookiecutter.variant == "normalizer" -%}
from .normalizer import ExampleNormalizer
{%- endif %}
{% if cookiecutter.variant == "parser" -%}
 from .parser import *
{%- endif %}
{% if cookiecutter.variant == "schema" -%}
 from .schema import *
{%- endif %}
