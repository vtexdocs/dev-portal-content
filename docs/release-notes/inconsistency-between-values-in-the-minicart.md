---
slug: "inconsistency-between-values-in-the-minicart"
title: "Inconsistency between values in the Minicart"
createdAt: 2020-11-26T18:37:06.076Z
hidden: false
type: "fixed"
---

<div class="badge" id="store-framework">Store Framework</div>
[block:html]
{
  "html": "<br/>"
}
[/block]
The total value displayed in the Minicart was ignoring the value passed to the `totalizersToShow` prop, generating a mismatch between the values listed and their final sum. [This crazy math was adjusted by our team](https://github.com/vtex-apps/checkout-summary/pull/38) and the total value now respects the value passed to the prop!