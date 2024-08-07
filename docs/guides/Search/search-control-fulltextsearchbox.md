---
title: "Search Control – fulltextSearchBox"
slug: "search-control-fulltextsearchbox"
hidden: false
createdAt: "2022-09-13T14:45:40.782Z"
updatedAt: "2022-09-13T14:49:33.433Z"
---

[block:callout]
{
  "type": "warning",
  "body": "VTEX has two search options - VTEX search and VTEX Intelligent Search. This article refers to the VTEX search. To learn more about the VTEX Intelligent Search application, see <a href = \"https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb\">this track</a>."
}
[/block]
The `<vtex.cmc:fullTextSearchBox />` control is responsible for generating the search box. Besides the search filed, the control renders a combo for restricting a search in one department. Below we have an example of the control with no application of CSS:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-cru.png)

Search is a functionality that must be available on all the pages of a store. That is why it is suggested inserting the control inside a [subtemplate](https://help.vtex.com/en/tutorial/subtemplates--tutorials_577). The search control is used within the subtemplate of the store header.

**HTML rendered by the control**

```html
<fieldset class="busca">
  <legend>Buscar no site</legend>
  <label>Buscar</label>
  <select id="ftDept4aceafb578de4c7caf31e06bcc8d45b9">
    <option value="">Todo o site</option>
    <option value="1000000">Integracao</option>
    <option value="1">Eletrodomésticos</option>
    <option value="3">Moda</option>
  </select>
  <input type="hidden" id=ftIdx4aceafb578de4c7caf31e06bcc8d45b9 value="" />
  <input id="ftBox4aceafb578de4c7caf31e06bcc8d45b9" class="fulltext-search-box" type="text" size="20" accesskey="b" />
  <input id="ftBtn4aceafb578de4c7caf31e06bcc8d45b9" type="button" value="Buscar" class="btn-buscar" />
</fieldset>
```

The autocomplete functionality is already provided for in this control, and it is only necessary to customize its CSS. Autocomplete is activated as soon as a client inputs three characters in the search field. Below is the html generated by the autocomplete:

```html
<ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" role="listbox" aria-activedescendant="ui-active-menuitem" style="z-index: 10; top: -3334px; left: 667.5px; display: none; position: relative; width: 507px;">
  <li class="ui-menu-item" role="menuitem"><a class="ui-corner-all" tabindex="-1">adidas em Modelos</a></li>
  <li class="ui-menu-item" role="menuitem"><a class="ui-corner-all" tabindex="-1">adidas em Tênis</a></li>
  <li class="ui-menu-item" role="menuitem"><a class="ui-corner-all" tabindex="-1">adidas em Lançamentos</a></li>
  <li class="ui-menu-item" role="menuitem"><a class="ui-corner-all" tabindex="-1">adidas em Masculino</a></li>
  <li class="ui-menu-item" role="menuitem">
    <a class="ui-corner-all" tabindex="-1">
      <img src="http://www.authenticfeet.com.br/arquivos/ids/188460-25-25/Mini-Bola-Brazuca-WC-14-Glider.jpg" width="25" height="25" alt="Mini-Bola-Brazuca-WC-14-Glider"> minibola adidas brazuca glider - copa do mundo
    </a>
  </li>
  <li class="ui-menu-item" role="menuitem">
    <a class="ui-corner-all" tabindex="-1">
      <img src="http://www.authenticfeet.com.br/arquivos/ids/189014-25-25/Tenis-adidas-Springblade-Feminino.jpg" width="25" height="25" alt="Tenis-adidas-Springblade-Feminino">
      tênis adidas springblade feminino
    </a>
  </li>
  <li class="ui-menu-item" role="menuitem">
    <a class="ui-corner-all" tabindex="-1">
      <img src="http://www.authenticfeet.com.br/arquivos/ids/188855-25-25/Tenis-adidas-Dynamic-Fusion-50-Feminino.jpg" width="25" height="25" alt="Tenis-adidas-Dynamic-Fusion-50-Feminino">
      tênis adidas dynamic fusion 50 feminino
    </a>
  </li>
</ul>
```

## Examples of how the control can be customized

**Example 1**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-autocomplete-560x318.png)

**Example 2**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-exemplo-560x43.png)

**Example 3**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-exemplo1.png)
