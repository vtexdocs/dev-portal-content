---
title: "Search Control – fulltextSearchBox"
slug: "search-control-fulltextsearchbox"
hidden: false
createdAt: "2022-09-13T14:45:40.782Z"
updatedAt: "2022-09-13T14:49:33.433Z"
---

The `<vtex.cmc:fullTextSearchBox />` control is responsible for generating the search box for [VTEX Legacy CMS Portal](https://help.vtex.com/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj). This control includes a search input field and a dropdown for restricting searches to specific departments. Below is an example of the control without any applied CSS styling:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-cru.png)

> ⚠️ VTEX offers two search solutions: VTEX Search and VTEX Intelligent Search. This guide specifically covers VTEX Search. For more information on VTEX Intelligent Search, refer to [this track](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb).

Search functionality is a crucial feature that should be accessible on all store pages. As a best practice, include this control in a [subtemplate](https://help.vtex.com/en/tutorial/subtemplates--tutorials_577) within the store's header.

## HTML rendered by the control

The `fullTextSearchBox` control generates the following HTML structure:

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

## Autocomplete feature

The `fullTextSearchBox` control includes a built-in autocomplete feature, which activates when a user types at least three characters in the search field. Customizing the autocomplete requires applying your own CSS. Below is an example of the HTML output for autocomplete:

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

## CSS customization examples

The `fullTextSearchBox` control allows for extensive customization using CSS. Here are some examples:

**Example 1**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-autocomplete-560x318.png)

**Example 2**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-exemplo-560x43.png)

**Example 3**
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/Search/controle-busca-exemplo1.png)
