define("templates\/content\/invoice\/seo\/seoItemRow.dust",["dust.core"],function(dust){dust.register("templates\/content\/invoice\/seo\/seoItemRow.dust",body_0);function body_0(chk,ctx){return chk.h("useContent",ctx,{"block":body_1},{"bundle":"content/invoice/seo/seoinvoiceform.properties"},"h");}body_0.__dustBody=!0;function body_1(chk,ctx){return chk.w("<tr><td><div class=\"col-lg-12 col-md-12 col-xs-12 no-padding\"><div class=\"vx_form-group no-padding\"><textarea class=\"vx_form-control item-desc\" id=\"itemName\" rows=\"1\" maxlength=\"200\" placeholder=\"").h("pre",ctx,{},{"type":"content","key":"content.itemName"},"h").w("\" aria-labelledBy=\"row_item\"></textarea></div></div></td><td><div class=\"no-padding\"><div class=\"vx_form-group no-padding\"><div><input class=\"vx_form-control input-form-field right-align item-field\" autocomplete=\"off\" type=\"number\" pattern=\"[0-9]*\" name=\"itemQuantity\" placeholder=\"0\" data-value=\"1\" value=\"1\" aria-labelledBy=\"row_quantity\"></div><div class=\"error-box invalid\" name=\"error\">").h("pre",ctx,{},{"type":"content","key":"alert.error.invalidQuantity"},"h").w("</div><div class=\"error-box\" name=\"error\">").h("pre",ctx,{},{"type":"content","key":"alert.error.invalidQuantityRange"},"h").w("</div></div></td><td><div class=\"no-padding\"><div class=\"vx_form-group no-padding\"><input class=\"vx_form-control input-form-field right-align item-field\" autocomplete=\"off\" type=\"number\" pattern=\"[0-9]*\" name=\"itemPrice\" placeholder=\"0.00\" aria-labelledBy=\"row_price\"></div><div class=\"error-box invalid\" name=\"error\">").h("pre",ctx,{},{"type":"content","key":"alert.error.invalidPrice"},"h").w("</div><div class=\"error-box\" name=\"error\">").h("pre",ctx,{},{"type":"content","key":"alert.error.invalidPriceRange"},"h").w("</div></div></td><td style=\"padding-left: 0px !important; padding-right:0px !important;\"><div class=\"line-item-amount no-padding\"><span name=\"negativeAmount\" class=\"hidden\">-</span><span name=\"currencySymbol\">").x(ctx.get(["currencySymbol"], false),ctx,{"else":body_2,"block":body_3},{}).w("</span><span name=\"lineItemTotal\">0.00</span></div></td><td style=\"padding-left: 0px !important; padding-right:0px !important;\" ><div class=\"line-item-amount no-padding\"><button id=\"closeIcon\" class=\"remove-item-icon\" aria-labelledBy=\"remove_item_btn\"/}\"><span class=\"vx_icon vx_icon-small vx_icon-close-small\"></span></button></div></td></tr>");}body_1.__dustBody=!0;function body_2(chk,ctx){return chk.w("$");}body_2.__dustBody=!0;function body_3(chk,ctx){return chk.f(ctx.get(["currencySymbol"], false),ctx,"h");}body_3.__dustBody=!0;return body_0});