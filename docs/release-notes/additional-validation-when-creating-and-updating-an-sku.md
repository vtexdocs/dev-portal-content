---
slug: "additional-validation-when-creating-and-updating-an-sku"
title: "Additional validation when creating and updating an SKU"
createdAt: 2020-11-18T17:10:40.176Z
hidden: false
type: "fixed"
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

Before, [Catalog API](ref:catalog-api-overview) did not apply the same validation rules seen in Admin, which had unintended side effects for our users when they attempted to activate an SKU they created or updated. Now we have corrected this behavior and the following restrictions apply.

- post [Create SKU](ref:catalog-api-post-sku)
SKU should never be created as active.

- put [Update SKU](ref:catalog-api-put-sku)
SKU should not be saved as active if:

- It does not have files added and associated to it.
- It is a kit and does not have components created and associated with it.
- It is a kit and one of its components is not set as active.

From now on, if you violate these conditions when attempting to create or update an SKU, you will receive a `400 Bad Request` error.

These constraints were created to guide developers into following the recommended SKU creation sequence:

1. [Create the SKU](ref:catalog-api-post-sku).
2. If the SKU is a kit, [create and associate SKU components](ref:catalog-api-post-sku-kit).
3. [Create and associate SKU files](ref:catalog-api-post-sku-file).
4. [Update the SKU](ref:catalog-api-put-sku) as active.
