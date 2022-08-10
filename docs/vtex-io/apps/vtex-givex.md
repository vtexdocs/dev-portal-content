---
title: "GiveX"
slug: "vtex-givex"
excerpt: "vtex.givex@0.5.3"
hidden: true
createdAt: "2022-07-07T18:27:40.926Z"
updatedAt: "2022-07-14T18:55:16.158Z"
---
How to configure the gateway affiliations
Access the Payments module;
Click on Settings;
Access the Gateway Affiliations tab;
Click on + to add a new affiliation;
Choose the Gift Card option;
Give a name to the affiliation;
Define Type of Refund and Early Security Capture conditions;
Click on Save.

How to configure the payment conditions
Access the Payments module;
Click on Settings;
Click on + symbol to add a new payment condition;
Choose Vale (Gift Card) as the payment condition;
Name the condition, activate it, and select Process with Affiliation (previously created);
Click on Save.

After entering settings on admin page, enter the following url in a browser: `<site>.myvtex.com/givex/giftcards/registration`

## Checkout Integration

To add a field for gift card PINs, custom JS code must be added to checkout in the `checkout6-custom.js` file:

```js
// Giftcard PIN
$(function() {
({
    const GC_NAME = "{{CARD NAME}}"
    init: function() {
        this.events(), this._splitGiftCardInput(), this._orderFormUpdate()
    },
    _orderFormUpdate: function() {
        var a = this;
        $(window).on("orderFormUpdated.vtex", function(t, e) {
            e.paymentData && a._updateGiftCardFormat(e)
        })
    },
    events: function() {
        var i = this;
        $(document).ajaxSuccess(function(r) { r.paymentData && i._updateGiftCardFormat(r)
        }), $(document).on("click", ".orderform-template-holder #show-gift-card-group", function() {
            i._addValueToGiftCardsSelect(), i._addListenerToSelect($(".orderform-template-holder .gift-card-section select#gift-card-provider-selector"))
        }), $(document).on("change", ".orderform-template-holder .gift-card-section select#gift-card-provider-selector", function() {
            i._addListenerToSelect(this), i._updateGiftCardFormat(vtexjs.checkout.orderForm)
        })
    },
    _updateGiftCardFormat: function(t) {
        t.paymentData && t.paymentData.giftCards && (t.paymentData.giftCards.some(function(t) {
            return GC_NAME !== t.provider
        }) && GC_NAME !== $("#gift-card-provider-selector option:selected").text() ? ($(".gift-card-multiple-providers").removeClass("enableBtn")) : ($(".gift-card-multiple-providers").addClass("enableBtn"), setTimeout(function() {
            $(".gift-card-multiple-providers").addClass("enableBtn")
        }, 2500), setTimeout(function() {
            $(".gift-card-multiple-providers").addClass("enableBtn")
        }, 6e3))), t.paymentData.giftCards.some(function(t) {
            return t && GC_NAME == t.provider
        }) && $("#show-gift-card-group").trigger("click")
    },
    _addValueToGiftCardsSelect: function() {
        $(".orderform-template-holder .gift-card-section select#gift-card-provider-selector option").each(function() {
            $(this).attr("value", $(this).text())
        })
    },
    _addListenerToSelect: function(t) {
        $(".orderform-template-holder .gift-card-section input#payment-discounts-code").val("").text("").removeClass("success"), this._addMaskToGiftCard($(t).attr("value")), this._splitGiftCardInput($(t).attr("value"))
    },
    _addMaskToGiftCard: function(t) {
        GC_NAME === t && $(".gift-card-multiple-providers").addClass(GC_NAME), GC_NAME == t ? ($(".orderform-template-holder .gift-card-section input#payment-discounts-code").attr("maxlength", "24").addClass("givexMask"), $(".orderform-template-holder .link-gift-card").addClass("pinText"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !0), $(".orderform-template-holder .gift-card-section input.givexMask").on("keyup.maskK change.maskC", function() {
            24 == $(this).val().length ? ($(".orderform-template-holder .gift-card-section input:last-of-type").addClass("success"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !1)) : ($(".orderform-template-holder .gift-card-section input:last-of-type").removeClass("success"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !0))
        })) : ($(".orderform-template-holder .gift-card-section input#payment-discounts-code").removeAttr("maxlength").removeClass("givexMask").off("keyup.maskK change.maskC"), $(".orderform-template-holder .link-gift-card").removeClass("pinText"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !0), $(".orderform-template-holder .gift-card-section input#payment-discounts-code").on("keyup change", function() {
            $(this).val().length ? $(this).addClass("success") : $(this).removeClass("success"), 0 < $(this).val().length ? ($(this).addClass("success"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !1)) : ($(this).removeClass("success"), $(".gift-card-section #btn-add-gift-card").prop("disabled", !0))
        }))
    },
    _splitGiftCardInput: function(t) {
        var e = $(".orderform-template-holder .gift-card-section .payment-discounts-options input#payment-discounts-code"),
            a = $(".orderform-template-holder .gift-card-section .payment-discounts-options .in");
        GC_NAME == t ? (e.hide(), a.length || $('<input class="in" placeholder="Code" type="text" maxlength="19" id="i1"/><input class="in pin" placeholder="Pin" type="text" maxlength="4" id="i2"/>').insertAfter(e)) : (e.show(), a.remove()), $(document).on("input", ".orderform-template-holder .gift-card-section .payment-discounts-options .in", function() {
            var t = $(".orderform-template-holder .gift-card-section .payment-discounts-options .in").map(function() {
                return this.value
            }).get().join("|");
            this.value.length == this.maxLength && $(this).next(".in").select(), 0 == this.value.length && $(this).prev(".in").focus(), e.val(t).trigger("change")
        })
    }
}).init()
});
// end Giftcard PIN
```