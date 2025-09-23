{% include "callouts.md" %}

{% macro stable() -%}
<span style="background-color:#28a745;color:white;padding:2px 6px;border-radius:4px;font-size:0.85em;">Stable</span>
{%- endmacro %}

{% macro preview() -%}
<span style="background-color:#17a2b8;color:white;padding:2px 6px;border-radius:4px;font-size:0.85em;">Preview</span>
{%- endmacro %}

{% macro archived() -%}
<span style="background-color:#6c757d;color:white;padding:2px 6px;border-radius:4px;font-size:0.85em;">Archived</span>
{%- endmacro %}
