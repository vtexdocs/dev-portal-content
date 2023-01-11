---
title: "Rewriter"
slug: "rewriter"
hidden: false
createdAt: "2020-08-31T17:21:31.944Z"
updatedAt: "2021-08-31T23:51:49.853Z"
---
Rewriter is the VTEX IO app responsible for managing the following three main types of [routes](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-routes): product, search, and navigation routes.

The first two are first-class entities in Rewriter, meaning Rewriter identifies these routes and directly forwards them to the rendering pipeline.

Navigation routes, in turn, are client-side defined routes related to custom paths and VTEX IO pre-defined templates, such as department, brand, and category routes. These routes can have a canonical path and a search query string.

In Rewriter, navigation routes are identified by the **internal** type, and routes used to redirect a route from one path to another are identified by the **redirect** type.

Rewriter includes functionalities to:

- Create an internal route.
- Create a canonical path related to an internal route.
- Create a redirect route.
- Delete a canonical path related to an internal route.
- Delete an internal route.
- Delete a redirect route.
- Create translated URLs for cross-border stores.

# Schema overview

## Query
[block:html]
{
  "html": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1083 572\">\n  <defs/>\n  <g id=\"graph0\" class=\"graph\" transform=\"translate(4 567)\">\n    <defs>\n      <style>\n        @import url(&quot;https://fonts.googleapis.com/css?family=Lato|Open+Sans|Oswald|Raleway|Roboto|Indie+Flower|Gamja+Flower&quot;);\n      </style>\n      <style>\n        text{fill:#4c555a;font-family:Roboto;font-size:13px;text-anchor:middle; alignment-baseline:middle}\n      </style>\n      <style>\n        text.texttitle{font-weight:700;}\n      </style>\n      <style>\n        a{fill:#f71963}\n      </style>\n      <style>\n        rect{fill:#fff;stroke:#dfe2e5}\n      </style>\n      <style>\n        rect.title{fill:#f6f8fa}\n      </style>\n      <style>\n        polygon{stroke-width:4;fill:#eee;stroke:#dfe2e5}\n      </style>\n      <style>\n        path{stroke-width:4;fill:none;stroke:#dfe2e5}\n      </style>\n      <style>\n        path.zoom{stroke-width:1;fill:none;stroke:#000}\n      </style>\n      <style>\n        g.edge:hover text{display:block;fill:#f71963}\n      </style>\n      <style>\n        g.edge:hover path{stroke:#ADB0B3}\n      </style>\n      <style>\n        g.edge:hover polygon{fill:#ADB0B3;stroke:#ADB0B3}\n      </style>\n      <style>\n        text.arrow{display:none}\n      </style>\n    </defs>\n<!--Query-->\n    <g id=\"node1\" transform=\"translate(8,-407)\" class=\"node\">\n      <rect width=\"163\" height=\"26\" class=\"title\"/>\n      <text x=\"81.5\" y=\"13\" class=\"texttitle\">\n        Query\n      </text>\n      <rect y=\"26\" width=\"163\" height=\"26\"/>      \n      <text x=\"81.5\" y=\"39\">\n        version: String\n      </text>\n      <rect y=\"52\" width=\"163\" height=\"26\"/>            \n        <text  x=\"81.5\" y=\"65\">\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirect\">\n        redirect: </a>\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#queryredirect\">\n        QueryRedirect!</a>\n        </text>\n      <rect y=\"78\" width=\"163\" height=\"26\"/>            \n        <text x=\"81.5\" y=\"91\">\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#internal\">internal:</a>\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#queryinternal\">QueryInternal!</a>\n      </text>\n    </g>\n\n<!--QueryRedirect-->\n    <g id=\"node2\" transform=\"translate(222,-463)\" class=\"node\">\n      <rect width=\"389\" height=\"26\" class=\"title\"/>      \n      <text x=\"194.5\" y=\"13\" class=\"texttitle\">\n        QueryRedirect\n      </text>\n      <rect y=\"26\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"39\">      \n        get(path:String!, locator:<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>): \n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirect\">Redirect</a>\n      </text>\n      <rect y=\"52\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"65\">      \n        listRedirects(limit:Int, next:String): \n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#listredirectsresponse\">ListRedirectsResponse!</a>\n      </text>\n    </g>\n\n<!--Query&#45;&gt;QueryRedirect-->\n    <g id=\"edge1\" class=\"edge\">\n      <path d=\"M171 -340c52.4 0 108.055 -17.035 152.958 -35.48\"/>\n      <polygon points=\"322.797,-378.789 333.372,-379.432 325.506,-372.334 322.797,-378.789\"/>\n      <text x=\"285\" y=\"-335\" class=\"arrow\">\n        Query: redirect\n      </text>\n    </g>\n\n<!--QueryInternal-->\n    <g id=\"node3\" transform=\"translate(133,-260)\" class=\"node\">\n      <rect width=\"380\" height=\"26\" class=\"title\"/>      \n      <text x=\"190\" y=\"13\" class=\"texttitle\">\n        QueryInternal\n      </text>\n      <rect y=\"26\" width=\"380\" height=\"26\"/>      \n      <text x=\"190\" y=\"39\">\n        get(path:String!, locator:<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>):  <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#internal\">Internal</a>\n      </text>\n      <rect y=\"52\" width=\"380\" height=\"26\"/>\n      <text x=\"190\" y=\"65\">\n        listInternals(limit:Int, next:String):  <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#listinternalsresponse\">ListInternalsResponse!</a>\n      </text>\n      <rect y=\"78\" width=\"380\" height=\"26\"/>  \n      <text x=\"190\" y=\"91\">\n        routes(locator:<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#entitylocator\">EntityLocator</a>): \n        <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#routesbybinding\">[RoutesByBinding!]</a>\n      </text>\n    </g>\n\n<!--Query&#45;&gt;QueryInternal-->\n    <g id=\"edge2\" class=\"edge\">\n      <path d=\"M171-318c53.234 0 108.222 21.066 152.49 44.144\"/>\n      <polygon points=\"325.304 -276.856 332.483 -269.064 322.012 -270.678 325.304 -276.856\"/>\n      <text x=\"285\" y=\"-320\" class=\"arrow\">\n        Query: internal\n      </text>\n    </g>\n\n<!--Redirect-->\n    <g id=\"node4\" transform=\"translate(901,-564)\" class=\"node\">\n      <rect width=\"141\" height=\"26\" class=\"title\"/> \n      <text x=\"70.5\" y=\"13\" class=\"texttitle\">\n        Redirect\n      </text>\n      <rect y=\"26\" width=\"141\" height=\"26\"/>       \n      <text x=\"70.5\" y=\"39\">\n        from: String!\n      </text>\n      <rect y=\"52\" width=\"141\" height=\"26\"/>  \n      <text x=\"70.5\" y=\"65\">\n        to: String!\n      </text>\n      <rect y=\"78\" width=\"141\" height=\"26\"/>       \n      <text x=\"70.5\" y=\"91\">\n        endDate: String\n      </text>\n      <rect y=\"104\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"117\">\n        type:  <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirecttypes\">RedirectTypes!</a>\n      </text>\n      <rect y=\"130\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"143\">\n        binding: String!\n      </text>\n      <rect y=\"156\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"169\">      \n        origin: String\n      </text>\n    </g>\n<!--QueryRedirect&#45;&gt;Redirect-->\n    <g id=\"edge3\" class=\"edge\">\n      <path d=\"M611-423c72.714-50.71 177.892-52.13 267.452-50.693\"/>\n      <polygon points=\"878.553 -477.192 888.448 -473.406 878.351 -470.195 878.553 -477.192\"/>\n      <text x=\"810\" y=\"-490\" class=\"arrow\">\n        QueryRedirect: get\n      </text>\n    </g>\n     \n<!--ListRedirectsResponse-->\n    <g id=\"node5\" transform=\"translate(662,-438)\" class=\"node\">\n      <rect x=\"0\" y=\"0\" width=\"152\" height=\"26\" class=\"title\"/>\n      <text x=\"76\" y=\"13\" class=\"texttitle\">\n        ListRedirectsResponse\n      </text>\n      <rect x=\"0\" y=\"26\" width=\"152\" height=\"26\"/>\n      <text x=\"76\" y=\"39\">\n        routes: <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirect\">[Redirect!]</a>\n      </text>\n      <rect x=\"0\" y=\"52\" width=\"152\" height=\"26\"/>      \n      <text x=\"76\" y=\"65\">\n        next: String\n      </text>\n    </g>\n\n<!--QueryRedirect&#45;&gt;ListRedirectsResponse-->\n    <g id=\"edge4\" class=\"edge\">\n      <path d=\"M611-398h32.844\"/>\n      <polygon points=\"643.974 -401.5 653.974 -398 643.974 -394.5 643.974 -401.5\"/>\n      <text x=\"600\" y=\"-375\" class=\"arrow\">\n        QueryRedirect: listRedirects\n      </text>\n    </g>\n<!--Internal-->\n    <g id=\"node6\" transform=\"translate(871,-361)\" class=\"node\">\n      <rect width=\"202\" height=\"26\" class=\"title\"/> \n      <text x=\"101\" y=\"13\" class=\"texttitle\">\n        Internal\n      </text>\n      <rect y=\"26\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"39\">\n        from: String!\n      </text>\n      <rect y=\"52\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"65\">\n        declarer: String!\n      </text>\n      <rect y=\"78\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"91\">\n        type: String!\n      </text>\n      <rect y=\"104\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"117\">\n        id: String!\n      </text>\n      <rect y=\"130\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"143\">\n        query: JSON\n      </text>\n      <rect y=\"156\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"169\">\n        binding: String!\n      </text>\n      <rect y=\"182\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"195\">\n        endDate: String\n      </text>\n      <rect y=\"208\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"221\">\n        imagePath: String\n      </text>\n      <rect y=\"234\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"247\">\n        imageTitle: String\n      </text>\n      <rect y=\"260\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"273\">\n        routesVersion: Float\n      </text>\n      <rect y=\"286\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"299\">\n        resolveAs: String\n      </text>\n      <rect y=\"312\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"325\">\n        origin: String\n      </text>\n      <rect y=\"338\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"351\">\n        disableSitemapEntry: Boolean\n      </text>\n    </g>\n\n<!--QueryInternal&#45;&gt;Internal-->\n    <g id=\"edge5\" class=\"edge\">\n      <path d=\"M512.49-230h334.915\"/>\n      <polygon points=\"857.611 -230 847.611 -226.5 847.611 -233.5\"/>\n      <text x=\"670\" y=\"-245\" class=\"arrow\">\n        QueryInternal: get\n      </text>\n    </g>\n\n<!--ListInternalsResponse-->\n    <g id=\"node7\" transform=\"translate(600,-221)\" class=\"node\">\n    <rect width=\"150\" height=\"26\" class=\"title\"/> \n      <text x=\"75\" y=\"13\" class=\"texttitle\">\n        ListInternalsResponse\n      </text>\n      <rect y=\"26\" width=\"150\" height=\"26\"/> \n      <text x=\"75\" y=\"39\">\n        routes:  <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#internal\">[Internal!]</a>\n      </text>\n      <rect y=\"52\" width=\"150\" height=\"26\"/> \n      <text x=\"75\" y=\"65\">\n        next: String\n      </text>\n    </g>\n\n<!--QueryInternal&#45;&gt;ListInternalsResponse-->\n    <g id=\"edge6\" class=\"edge\">\n      <path d=\"M511.87 -196c23.329 0 47.75 1.01 71.724 2.596\"/>\n      <polygon points=\"593.872,-192.016 583.494,-189.886 584.43,-196.823\"/>\n      <text x=\"540\" y=\"-220\" class=\"arrow\">\n        QueryInternal: listInternals\n      </text>\n    </g>\n\n<!--RoutesByBinding-->\n    <g id=\"node8\" transform=\"translate(617,-125)\" class=\"node\">\n    <rect width=\"122\" height=\"26\" class=\"title\"/> \n      <text x=\"61\" y=\"13\" class=\"texttitle\">\n        RoutesByBinding\n      </text>\n      <rect y=\"26\" width=\"122\" height=\"26\"/> \n      <text x=\"61\" y=\"39\">\n        binding: String!\n      </text>\n      <rect y=\"52\" width=\"122\" height=\"26\" /> \n      <text x=\"61\" y=\"65\">\n        route: String!\n      </text>\n    </g>\n\n<!--QueryInternal&#45;&gt;RoutesByBinding-->\n    <g id=\"edge7\" class=\"edge\">\n      <path d=\"M512.34-171.493c25.857 0 55.24 25.974 86.66 48.493a251.463 251.463 0 007.254 5.519\"/>\n      <polygon points=\"607.852 -117.396 597.667 -120.316 601.711 -126.03\"/>\n      <text x=\"510\" y=\"-130\" class=\"arrow\">\n        QueryInternal: routes\n      </text>\n    </g>\n\n<!--ListRedirectsResponse&#45;&gt;Redirect-->\n    <g id=\"edge8\" class=\"edge\">\n      <path d=\"M814-397h64.723\"/>\n      <polygon points=\"878.859 -401.5 888.859 -397.5 878.859 -394\"/>\n      <text x=\"880\" y=\"-370\" class=\"arrow\">\n        ListRedirectsResponse: routes\n      </text>\n    </g>\n<!--ListInternalsResponse&#45;&gt;Internal-->\n    <g id=\"edge9\" class=\"edge\">\n      <path d=\"M750.392 -182h97.013\"/>\n      <polygon points=\"847.611,-185.5 857.611,-182 847.611,-178.5 847.611,-185.5\"/>\n      <text x=\"800\" y=\"-155\" class=\"arrow\">\n        ListInternalsResponse: routes\n      </text>\n    </g>\n  </g>\n</svg>"
}
[/block]
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" valign="top"><strong>redirect</strong></td>
<td valign="top"><a href="#queryredirect">QueryRedirect</a>!</td>
<td>Provides <i>redirect</i> routes data.<br>Redirect routes are used to redirect a route from one path to another.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>internal</strong></td>
<td valign="top"><a href="#queryinternal">QueryInternal</a>!</td>
<td>Provides <i>internal</i> routes data.<br>Internal routes are navigation routes.</td>
</tr>
</tbody>
</table>

## Mutation
[block:html]
{
  "html": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1083 572\">\n  <defs/>\n  <g id=\"graph0\" class=\"graph\" transform=\"translate(4 567)\">\n    <defs>\n      <style>\n        @import url(&quot;https://fonts.googleapis.com/css?family=Lato|Open+Sans|Oswald|Raleway|Roboto|Indie+Flower|Gamja+Flower&quot;);\n      </style>\n      <style>\n        text{fill:#4c555a;font-family:Roboto;font-size:13px;text-anchor:middle; alignment-baseline:middle}\n      </style>\n      <style>\n        text.texttitle{font-weight:700;}\n      </style>\n      <style>\n        a{fill:#f71963}\n      </style>\n      <style>\n        rect{fill:#fff;stroke:#dfe2e5}\n      </style>\n      <style>\n        rect.title{fill:#f6f8fa}\n      </style>\n      <style>\n        polygon{stroke-width:4;fill:#dfe2e5;stroke:#dfe2e5}\n      </style>\n      <style>\n        path{stroke-width:4;fill:none;stroke:#dfe2e5}\n      </style>\n      <style>\n        path.zoom{stroke-width:1;fill:none;stroke:#000}\n      </style>\n      <style>\n        g.edge:hover text{display:block;fill:#f71963}\n      </style>\n      <style>\n        g.edge:hover path{stroke:#ADB0B3}\n      </style>\n      <style>\n        g.edge:hover polygon{fill:#ADB0B3;stroke:#ADB0B3}\n      </style>\n      <style>\n        text.arrow{display:none}\n      </style>\n    </defs>\n    <!-- Mutation -->\n    <g transform=\"translate(8,-382)\" class=\"node\"\n       id=\"node1\">\n      <title id=\"mutation\">Mutation</title> <rect width=\"163\" height=\"26\" class=\"title\"/>\n         <text x=\"81.5\" y=\"13\" class=\"texttitle\">\n         Mutation</text>\n      <rect y=\"26\" width=\"163\" height=\"26\"/>      \n         <text x=\"81.5\" y=\"39\">\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n        href=\"#redirect\">redirect</a>\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n        href=\"#mutateredirect\">\n         MutateRedirect!</a></text>\n      <rect y=\"52\" width=\"163\" height=\"26\"/>            \n        <text  x=\"81.5\" y=\"65\">\n        <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#internal\">internal:</a>\n         <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#mutateinternal\">\n          MutateInternal!</a></text>\n    </g>\n    <!-- MutateRedirect -->\n    <g transform=\"translate(250,-516)\"\n       class=\"node\"\n       id=\"node2\"\n       >\n      <title\n         id=\"title41\">MutateRedirect</title><rect width=\"389\" height=\"26\" class=\"title\"/>\n         <text x=\"194.5\" y=\"13\" class=\"texttitle\">\n         MutateRedirect</text>\n      <rect y=\"26\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"39\"> save(route: <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#redirectinput\">RedirectInput</a>!):\n         <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirect\">Redirect</a></text>\n      <rect y=\"52\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"65\"> saveMany(routes: [<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#redirectinput\">RedirectInput</a>!]!): Boolean!</text>\n      <rect y=\"78\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"91\"> delete(path: String! locator: <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>): \n         <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirect\">Redirect</a></text>\n      <rect y=\"104\" width=\"389\" height=\"26\"/>      \n      <text x=\"194.5\" y=\"117\">deleteMany(paths: [String!]! locators: [<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>!]): Boolean!</text>\n    </g>\n    <!-- Mutation&#45;&gt;MutateRedirect -->\n    <g\n       class=\"edge\"\n       id=\"edge1\">\n      <title\n         id=\"title56\">Mutation:redirectport-&gt;MutateRedirect</title>\n      <path\n         id=\"path58\"\n         d=\"M171,-343C223.4,-343 279.055,-360.035 323.958,-378.48\"/>\n      <polygon\n         id=\"polygon60\"\n         points=\"322.797,-381.789 333.372,-382.432 325.506,-375.334 322.797,-381.789\"/>\n      <text\n         class=\"arrow\"\n         y=\"-330\"\n         x=\"270\"\n         id=\"text1040\">Mutation: redirect</text>\n    </g>\n    <!-- MutateInternal -->\n    <g\n       class=\"node\"\n       transform=\"translate(260,-265)\"\n       id=\"node3\">\n      <title\n         id=\"title63\">MutateInternal</title>\n      <rect width=\"380\" height=\"26\" class=\"title\"/>      \n      <text x=\"190\" y=\"13\" class=\"texttitle\">\n      MutateInternal</text>\n      <rect y=\"26\" width=\"380\" height=\"26\"/>      \n      <text x=\"190\" y=\"39\">save(route: <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#internalinput\">InternalInput</a>!): \n         <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#internal\">Internal</a></text>\n      <rect y=\"52\" width=\"380\" height=\"26\"/>\n      <text x=\"190\" y=\"65\">saveMany(routes: [<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#internalinput\">InternalInput</a>!]!): Boolean!</text>\n      <rect y=\"78\" width=\"380\" height=\"26\"/>  \n      <text x=\"190\" y=\"91\">delete(path: String! locator: <a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>): \n         <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#internal\">Internal</a></text>\n      <rect y=\"104\" width=\"380\" height=\"26\"/>  \n      <text x=\"190\" y=\"117\">deleteMany(paths: [String!]! locators: [<a text-anchor=\"middle\" alignment-baseline=\"middle\"\n           href=\"#routelocator\">RouteLocator</a>!]): Boolean!</text>\n    </g>\n    <!-- Mutation:internalport ->MutateInternal -->\n    <g\n       class=\"edge\"\n       id=\"edge2\"\n      <title\n         id=\"title82\">Mutation:internalport-&gt;MutateInternal</title>\n      <path\n         id=\"path84\"\n         d=\"M171,-318C224.234,-318 279.222,-296.934 323.49,-273.856\" />\n      <polygon\n         id=\"polygon86\"\n         points=\"325.304,-276.856 332.483,-269.064 322.012,-270.678 325.304,-276.856\" />\n      <text\n         class=\"arrow\"\n         y=\"-325\"\n         x=\"270\"\n         id=\"text1057\">Mutation: internal</text>\n    </g>\n    <!--Redirect-->\n    <g id=\"node4\" transform=\"translate(895,-564)\" class=\"node\">\n      <rect width=\"141\" height=\"26\" class=\"title\"/> \n      <text x=\"70.5\" y=\"13\" class=\"texttitle\">\n        Redirect\n      </text>\n      <rect y=\"26\" width=\"141\" height=\"26\"/>       \n      <text x=\"70.5\" y=\"39\">\n        from: String!\n      </text>\n      <rect y=\"52\" width=\"141\" height=\"26\"/>  \n      <text x=\"70.5\" y=\"65\">\n        to: String!\n      </text>\n      <rect y=\"78\" width=\"141\" height=\"26\"/>       \n      <text x=\"70.5\" y=\"91\">\n        endDate: String\n      </text>\n      <rect y=\"104\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"117\">\n        type:  <a text-anchor=\"middle\" alignment-baseline=\"middle\" href=\"#redirecttypes\">RedirectTypes!</a>\n      </text>\n      <rect y=\"130\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"143\">\n        binding: String!\n      </text>\n      <rect y=\"156\" width=\"141\" height=\"26\"/>             \n      <text x=\"70.5\" y=\"169\">      \n        origin: String\n      </text>\n    </g>\n    <!-- MutateRedirect&#45;&gt;MutateRedirect -->\n    <g\n       class=\"edge\"\n       id=\"edge3\">\n      <title id=\"title120\">MutateRedirect:deleteport-Redirect</title>\n      <path id=\"path122\" d=\"M638.408988 -423.268995H883.9345079999999\"/>\n      <polygon id=\"polygon124\" points=\"874.039508,-426.724425 883.9345079999999,-422.938425 873.837508,-419.727425 NaN,NaN\"/>\n      <text\n         class=\"arrow\"\n         y=\"-400\"\n         x=\"760\"\n         id=\"text1079\">MutateRedirect: delete</text>\n    </g>\n    <!--Internal-->\n    <g id=\"node6\" transform=\"translate(871,-361)\" class=\"node\">\n      <rect width=\"202\" height=\"26\" class=\"title\"/> \n      <text x=\"101\" y=\"13\" class=\"texttitle\">\n        Internal\n      </text>\n      <rect y=\"26\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"39\">\n        from: String!\n      </text>\n      <rect y=\"52\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"65\">\n        declarer: String!\n      </text>\n      <rect y=\"78\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"91\">\n        type: String!\n      </text>\n      <rect y=\"104\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"117\">\n        id: String!\n      </text>\n      <rect y=\"130\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"143\">\n        query: JSON\n      </text>\n      <rect y=\"156\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"169\">\n        binding: String!\n      </text>\n      <rect y=\"182\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"195\">\n        endDate: String\n      </text>\n      <rect y=\"208\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"221\">\n        imagePath: String\n      </text>\n      <rect y=\"234\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"247\">\n        imageTitle: String\n      </text>\n      <rect y=\"260\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"273\">\n        routesVersion: Float\n      </text>\n      <rect y=\"286\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"299\">\n        resolveAs: String\n      </text>\n      <rect y=\"312\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"325\">\n        origin: String\n      </text>\n      <rect y=\"338\" width=\"202\" height=\"26\"/> \n      <text x=\"101\" y=\"351\">\n        disableSitemapEntry: Boolean\n      </text>\n    </g>\n\n    <!-- MutateInternal&#45;&gt;Internal -->\n    <g\n       class=\"edge\"\n       id=\"edge5\">\n      <title\n         id=\"title208\">MutateInternal:saveport-Internal</title>\n      <path\n         id=\"path210\"\n         d=\"m 640.17993,-230 c 67.21793,0 137.20647,0 207.22513,0\" />\n      <polygon\n         id=\"polygon212\"\n         points=\"847.611,-226.5 847.611,-233.5 857.611,-230\"/>\n      <text\n         class=\"arrow\"\n         y=\"-245\"\n         x=\"750\"\n         id=\"text1115\">MutateInternal: save</text>\n    </g>\n    <!-- MutateInternal&#45;&gt;Internal -->\n    <g\n       class=\"edge\"\n       id=\"edge7\">\n      <title id=\"title252\">MutateInternal:deleteport-Internal</title>\n      <path id=\"path254\" d=\"M639.58 -177.5H846.81\"/>\n      <polygon id=\"polygon256\" points=\"847.01342131345,-181.00056601197 857.0133800773599,-177.50595082727997 847.01689767831,-174.00100372963 NaN,NaN\"/>\n    <text\n         class=\"arrow\"\n         y=\"-155\"\n         x=\"750\">MutateInternal: delete</text>\n    </g>\n    <g\n       id=\"edg4\"\n       class=\"edge\">\n      <title\n         id=\"title120-2\">MutateRedirect:saveport-Redirect</title>\n      <path d=\"M638.409 -473.268995H883.935\" id=\"path122-4\"/>\n      <polygon points=\"873.837,-469.727425 874.039,-476.724425 883.935,-472.938425 NaN,NaN\" id=\"polygon124-8\"/>\n      <text\n         x=\"760\"\n         y=\"-490\"\n         class=\"arrow\">MutateRedirect: save</text>\n    </g>\n  </g>\n</svg>"
}
[/block]
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" valign="top"><strong>redirect</strong></td>
<td valign="top"><a href="#mutateredirect">MutateRedirect</a>!</td>
<td>Updates or deletes <i>redirect</i> routes data according to the provided arguments.
<br>Redirect routes are used to redirect a route from one path to another.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>internal</strong></td>
<td valign="top"><a href="#mutateinternal">MutateInternal</a>!</td>
<td>Updates or deletes <i>internal</i> routes data according to the provided arguments.
<br>Internal routes are navigation routes.</td>
</tr>
</tbody>
</table>

# Schema description
[block:callout]
{
  "type": "warning",
  "body": "Arguments must be provided by the user. The exclamation mark `!` indicates that a type cannot be nullable."
}
[/block]
## QueryRedirect

<table>
    <thead>
        <tr>
            <th align="left">Field</th>
            <th align="right">(argument)</th>
            <th align="left">Type</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" valign="top"><strong>get</strong></td>
            <td valign="top"><a href="#redirect">Redirect</a></td>
            <td valign="top">Returns information regarding a specific redirect route, given its related <i>path</i> and <i>locator</i>.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">path</td>
            <td valign="top"><strong>String!</strong></td>
            <td>The path of the desired route to fetch data.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locator</td>
            <td valign="top"><a href="#routelocator">RouteLocator</a></td>
            <td>The <i>RouteLocator</i> object, containing information about the store locale and route origin.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>listRedirects</strong></td>
            <td valign="top"><a href="#listredirectsresponse">ListRedirectsResponse</a>!</td>
            <td>Lists all redirect routes.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top" align="right">limit</td>
            <td valign="top">Int</td>
            <td>The number of <i>ListRedirectsResponse</i> objects to be displayed at once.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top" align="right">next</td>
            <td valign="top">String</td>
            <td>The argument used to fetch more internal routes from <i>ListRedirectsResponse</i>.<br>It must be empty in the first query and, in the following, filled in with the string previously obtained from the <i>ListRedirectsResponse</i> object.</td>
        </tr>
    </tbody>
</table>

<div style="text-align: right"><a href="#query">Query</a> 🔼</div>

## QueryInternal
<table>
    <thead>
        <tr>
            <th align="left">Field</th>
            <th align="right">(argument)</th>
            <th align="left">Type</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" valign="top"><strong>get</strong></td>
            <td valign="top"><a href="#internal">Internal</a></td>
            <td>Returns information regarding a specific internal route, given its related <i>path</i> and <i>locator</i></td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">path</td>
            <td valign="top">String!</td>
            <td>The path of the desired route to fetch data.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locator</td>
            <td valign="top"><a href="#routelocator">RouteLocator</a></td>
            <td>The <i>RouteLocator</i> object, containing information about the store locale and route origin.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>listInternals</strong></td>
            <td valign="top"><a href="#listinternalsresponse">ListInternalsResponse</a>!</td>
            <td>Lists all internal routes.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">limit</td>
            <td valign="top">Int</td>
            <td>The number of <i>ListInternalsResponse</i> objects to be displayed at once.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">next</td>
            <td valign="top">String</td>
            <td>The argument used to fetch more internal routes from <i>ListInternalsResponse</i>.<br>It must be empty in the first query and, in the following, filled in with the string previously obtained from the <i>ListInternalsResponse</i> object.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>routes</strong></td>
            <td valign="top">[<a href="#routesbybinding">RoutesByBinding</a>!]</td>
            <td>Lists all internal routes of a specific type (e.g. deparment routes, category routes, etc.) and its related <i>binding</i>, which is an identifier for each store locale.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locator</td>
            <td valign="top"><a href="#entitylocator">EntityLocator</a></td>
            <td>The <i>EntityLocator</i> object, containing information about the entity type of the routes to be listed.</td>
        </tr>
    </tbody>
</table>

<div style="text-align: right"><a href="#query">Query</a> 🔼</div>

## MutateRedirect

<table>
    <thead>
        <tr>
            <th align="left">Field</th>
            <th align="right">(argument)</th>
            <th align="left">Type</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" valign="top"><strong>save</strong></td>
            <td valign="top"><a href="#redirect">Redirect</a></td>
            <td>Creates or updates a redirect route according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">route</td>
            <td valign="top"><a href="#redirectinput">RedirectInput</a>!</td>
            <td>The data regarding the redirect route to be created or updated.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>saveMany</strong></td>
            <td valign="top">Boolean!</td>
            <td>Creates or updates many redirect routes according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">routes</td>
            <td valign="top">[<a href="#redirectinput">RedirectInput</a>!]!</td>
            <td>The data regarding the redirect routes to be created or updated.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>delete</strong></td>
            <td valign="top"><a href="#redirect">Redirect</a></td>
            <td>Deletes a redirect route according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">path</td>
            <td valign="top">String!</td>
            <td>The path of the route to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locator</td>
            <td valign="top"><a href="#routelocator">RouteLocator</a></td>
            <td>The <i>EntityLocator</i> object, containing information about the entity type of the route to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>deleteMany</strong></td>
            <td valign="top">Boolean!</td>
            <td>Deletes many redirect route according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">paths</td>
            <td valign="top">[String!]!</td>
            <td>The paths of the routes to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locators</td>
            <td valign="top">[<a href="#routelocator">RouteLocator</a>!]</td>
            <td>The <i>EntityLocator</i> objects, containing information about the entity type of the routes to be deleted.</td>
        </tr>
    </tbody>
</table>

<div style="text-align: right"><a href="#mutation">Mutation</a> 🔼</div>

## MutateInternal

<table>
    <thead>
        <tr>
            <th align="left">Field</th>
            <th align="right">(argument)</th>
            <th align="left">Type</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" valign="top"><strong>save</strong></td>
            <td valign="top"><a href="#internal">Internal</a></td>
            <td>Creates or updates an internal route according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">route</td>
            <td valign="top"><a href="#internalinput">InternalInput</a>!</td>
            <td>The data regarding the internal route to be created or updated.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>saveMany</strong></td>
            <td valign="top">Boolean!</td>
            <td>Creates or updates many internal routes according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">routes</td>
            <td valign="top">[<a href="#internalinput">InternalInput</a>!]!</td>
            <td>The data regarding the internal routes to be created or updated.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>delete</strong></td>
            <td valign="top"><a href="#internal">Internal</a></td>
            <td>Deletes an internal route according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">path</td>
            <td valign="top">String!</td>
            <td>
                The path of the route to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locator</td>
            <td valign="top"><a href="#routelocator">RouteLocator</a></td>
            <td>The <i>EntityLocator</i> object, containing information about the entity type of the route to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" valign="top"><strong>deleteMany</strong></td>
            <td valign="top">Boolean!</td>
            <td>Deletes many internal routes according to the provided arguments.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">paths</td>
            <td valign="top">[String!]!</td>
            <td>The paths of the routes to be deleted.</td>
        </tr>
        <tr>
            <td colspan="2" align="right" valign="top">locators</td>
            <td valign="top">[<a href="#routelocator">RouteLocator</a>!]</td>
            <td>The <i>EntityLocator</i> objects, containing information about the entity type of the routes to be deleted.</td>
        </tr>
    </tbody>
</table>

<div style="text-align: right"><a href="#mutation">Mutation</a> 🔼</div>



## Internal

<table>
    <thead>
        <tr>
            <th align="left">Field</th>
            <th align="left">Type</th>
            <th align="left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="1" valign="top"><strong>from</strong></td>
            <td valign="top">String!</td>
            <td>The route path.</td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>declarer</strong></td>
            <td valign="top">String!</td>
            <td>The app that originally defined the route in a <code>routes.json</code> file. <br>For VTEX IO pre-defined routes, the <code>declarer</code> value is <code>vtex.store@2.x.</code></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>type</strong></td>
            <td valign="top">String!</td>
            <td>The route entity type defined in the <code>declarer</code> app, which can be: <code>department</code>, <code>category</code>, <code>subcategory</code>, <code>brand</code> , etc.</td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>id</strong></td>
            <td valign="top">String!</td>
            <td>The entity type id. For example, a deparment id.</td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>query</strong></td>
            <td valign="top">JSON</td>
            <td>The query string parameters of a route.</td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>binding</strong></td>
            <td valign="top">String!</td>
            <td>The id of the <i>binding</i> which the route is available.<br><i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>endDate</strong></td>
            <td valign="top">String</td>
            <td>The date a route stops being valid.<br><i>Keep in mind: The <code>endDate</code> value for permanent routes is <code>null</code>.</i></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>imagePath</strong></td>
            <td valign="top">String</td>
            <td></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>imageTitle</strong></td>
            <td valign="top">String</td>
            <td></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>routesVersion</strong></td>
            <td valign="top">Float</td>
            <td>The current routes version.
                <br>
                <i>Keep in mind: If the <code>routesVersion</code> value is <code>null</code> or different from the current version, the route is not currently available in the store.</i>
            </td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>resolveAs</strong></td>
            <td valign="top">String</td>
            <td>Alias paths of a route, meaning that the route will resolve the paths defined in the <code>resolveAs</code> field.<br><i>Keep in mind: The <code>resolveAs</code> parameter must always be defined in the catalog's default language.</i></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>origin</strong></td>
            <td valign="top">String</td>
            <td>A string that defines the origin of the route, for example: <code>user-canonical</code></td>
        </tr>
        <tr>
            <td colspan="1" valign="top"><strong>disableSitemapEntry</strong></td>
            <td valign="top">Boolean</td>
            <td>The boolean value that indicates if a route is included (<code>False</code>) or not (<code>True</code>) in the store's sitemap.</td>
        </tr>
    </tbody>
</table>

<div style="text-align: right"><a href="#queryinternal">QueryInternal</a> 🔼</div>

<div style="text-align: right"><a href="#mutateinternal">MutateInternal</a> 🔼</div>

<div style="text-align: right"><a href="#listinternalsresponse">ListInternalsResponse</a> 🔼</div>

## ListInternalsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" valign="top"><strong>routes</strong></td>
<td valign="top">[<a href="#internal">Internal</a>!]</td>
<td>Returns the demanded information from the <i>Internal</i> object for each route.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>next</strong></td>
<td valign="top">String</td>
<td>Returns a string to be used as the <i>next</i> argument of the succeeding <i>listInternals</i> query to fetch more data.<br>When <i>next</i> returns <i>null</i>, all data have already been fetched.</td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryinternal">QueryInternal</a> 🔼</div>

## RoutesByBinding

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" valign="top"><strong>binding</strong></td>
<td valign="top">String!</td>
<td>The id of the <i>binding</i> which the route is available.
<br>
<i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>route</strong></td>
<td valign="top">String!</td>
<td>Returns the route path.</td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryinternal">QueryInternal</a> 🔼</div>

## Redirect

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" valign="top"><strong>from</strong></td>
<td valign="top">String!</td>
<td>The original route path.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>to</strong></td>
<td valign="top">String!</td>
<td>The route redirect path.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>endDate</strong></td>
<td valign="top">String</td>
<td>The date a redirect route stops being valid.
<br>
<i>Keep in mind: The <code>endDate</code> value for permanent routes is <code>null</code>.</i></td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#redirecttypes">RedirectTypes</a>!</td>
<td>The route type: temporary or permanent.</td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>binding</strong></td>
<td valign="top">String!</td>
<td>The id of the <i>binding</i> which the route is available.
<br>
<i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
</tr>
<tr>
<td colspan="1" valign="top"><strong>origin</strong></td>
<td valign="top">String</td>
<td>A string that defines the origin of the route, for example: <code>user-canonical</code></td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryredirect">QueryRedirect</a> 🔼</div>

<div style="text-align: right"><a href="#mutateredirect">MutateRedirect</a> 🔼</div>

## ListRedirectsResponse

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>routes</strong></td>
<td valign="top">[<a href="#redirect">Redirect</a>!]</td>
<td>Returns the demanded information from the <i>Redirect</i> object for each route.</td>
</tr>
<tr>
<td valign="top"><strong>next</strong></td>
<td valign="top">String</td>
<td>Returns a string to be used as the <i>next</i> argument of the succeeding <i>listInternals</i> query to fetch more data.<br>When <i>next</i> returns <i>null</i>, all data have already been fetched.</td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryredirect">QueryRedirect</a> 🔼</div>

## EntityLocator

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top"><strong>id</strong></td>
<td valign="top">String!</td>
<td>The entity type id. For example, a deparment id.</td>
</tr>
<tr>
<td valign="top"><strong>type</strong></td>
<td valign="top">String!</td>
<td>The route entity type, which can be: <code>department</code>, <code>category</code>, <code>subcategory</code>, <code>brand</code> , etc</td></td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryinternal">QueryInternal</a> 🔼</div>

## InternalInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top">String!</td>
<td>The route path.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>declarer</strong></td>
<td valign="top">String!</td>
<td>The app that originally defined the route in a <code>routes.json</code> file.
<br>For VTEX IO pre-defined routes, the <code>declarer</code> value is <code>vtex.store@2.x.</code></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top">String!</td>
<td>The route entity type, which can be: <code>department</code>, <code>category</code>, <code>subcategory</code>, <code>brand</code> , etc</td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top">String!</td>
<td>The entity type id. For example, a deparment id.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>query</strong></td>
<td valign="top">JSON</td>
<td>The query string parameters of a route.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>binding</strong></td>
<td valign="top">String</td>
<td>The id of the <i>binding</i> which the route is available.
<br>
<i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>endDate</strong></td>
<td valign="top">String</td>
<td>The date a route stops being valid.
<br>
<i>Keep in mind: The <code>endDate</code> value for permanent routes is <code>null</code>.</i></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>imagePath</strong></td>
<td valign="top">String</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>imageTitle</strong></td>
<td valign="top">String</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>resolveAs</strong></td>
<td valign="top">String</td>
<td>Alias paths of a route, meaning that the route will resolve the paths defined in the <code>resolveAs</code> field.
<br>
<i>Keep in mind: The <code>resolveAs</code> parameter must always be defined in the catalog's default language.</i></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>origin</strong></td>
<td valign="top">String</td>
<td>A string that defines the origin of the route, for example: <code>user-canonical</code></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>disableSitemapEntry</strong></td>
<td valign="top">Boolean</td>
<td>The boolean value that indicates if a route is included (<code>False</code>) or not (<code>True</code>) in the store's sitemap.</td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#mutateinternal">MutateInternal</a> 🔼</div>

## RedirectInput

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top">String!</td>
<td>The original route path.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top">String!</td>
<td>The route redirect path.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>endDate</strong></td>
<td valign="top">String</td>
<td>The date a route stops being valid.
<br>
<i>Keep in mind: The <code>endDate</code> value for permanent routes is <code>null</code>.</i></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#redirecttypes">RedirectTypes</a>!</td>
<td>The route type: temporary or permanent.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>binding</strong></td>
<td valign="top">String</td>
<td>The id of the <i>binding</i> which the route is available.
<br>
<i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>origin</strong></td>
<td valign="top">String</td>
<td>A string that defines the origin of the route, for example: <code>user-canonical</code></td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#mutateredirect">MutateRedirect</a> 🔼</div>

## RouteLocator

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top">String!</td>
<td>The original route path.</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>binding</strong></td>
<td valign="top">String!</td>
<td>The id of the <i>binding</i> which the route is available.<br><i>Keep in mind: Every store has a binding id related to its store locale. Hence, cross-border stores always have more than one binding, while accounts with a single storefront have only one binding id.</i></td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#queryredirect">QueryRedirect</a> 🔼</div>

<div style="text-align: right"><a href="#queryinternal">QueryInternal</a> 🔼</div>

<div style="text-align: right"><a href="#mutateredirect">MutateRedirect</a> 🔼</div>

<div style="text-align: right"><a href="#mutateinternal">MutateInternal</a> 🔼</div>

## RedirectTypes

<table>
<thead>
<th align="left">Value</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PERMANENT</strong></td>
</tr>
<tr>
<td valign="top"><strong>TEMPORARY</strong></td>
</tr>
</tbody>
</table>

<div style="text-align: right"><a href="#redirect">Redirect</a> 🔼</div>

<div style="text-align: right"><a href="#redirectinput">RedirectInput</a> 🔼</div>
