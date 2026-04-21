{% include "callouts.md" %}

{% macro next_steps(links) -%}
### Next steps
<ul>
{% for text, url in links %}
- <li><a href="{{ url }}">{{ text }}</a></li>
{% endfor %}
</ul>
{%- endmacro %}
