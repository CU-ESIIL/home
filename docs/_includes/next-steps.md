{% include "callouts.md" %}

{% macro next_steps(links) -%}
### Next steps
{% for text, url in links %}
- [{{ text }}]({{ url }})
{% endfor %}
{%- endmacro %}
