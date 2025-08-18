{% macro note() -%}
!!! note "Note"
    {{ caller() }}
{%- endmacro %}

{% macro tip() -%}
!!! tip "Tip"
    {{ caller() }}
{%- endmacro %}

{% macro caution() -%}
!!! caution "Caution"
    {{ caller() }}
{%- endmacro %}
