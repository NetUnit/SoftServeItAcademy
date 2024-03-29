
/*@preserve
***Version 1.56.0***
*/

/*@license
 *                       Copyright 2002 - 2018 Qualtrics, LLC.
 *                        CONFIDENTIAL.  All rights reserved.
 *
 * Notice: All code, text, concepts, and other information herein (collectively, the
 * "Materials") are the sole property of Qualtrics, LLC, except to the extent
 * otherwise indicated. The Materials are proprietary to Qualtrics and are protected
 * under all applicable laws, including copyright, patent (as applicable), trade
 * secret, and contract law. Disclosure or reproduction of any Materials is strictly
 * prohibited without the express prior written consent of an authorized signatory
 * of Qualtrics. For disclosure requests, please contact notice@qualtrics.com.
 */

try {
  (window["WAFQualtricsWebpackJsonP-hosted-1.56.0"]=window["WAFQualtricsWebpackJsonP-hosted-1.56.0"]||[]).push([[16],{53:function(e,n,t){"use strict";t.r(n);var i=function(){return function(e,n){this.payload=n,this.type=e}}();t.d(n,"addPopunderEmbeddedDataHandler",function(){return o}),t.d(n,"updatePopunderEDCallback",function(){return a});var o=function(e){var n=window.QSI,t=n.util,i=n.windowHandler,o=n.dbg;t.observe(window,"beforeunload",e,!0);try{i.setupWindowHandles()}catch(e){o.e(e)}},d=function(e,n){if("string"==typeof e&&"string"==typeof n){var t=window.QSI.windowHandler,o=t.getWin(n);if(o){var d=new i("setTargetUrlInPlaceholderWindow",e),r=JSON.stringify(d),a=t.getWindowOrigin(window);o.postMessage(r,a)}}},r=function(e,n,t,o){if(void 0!==e&&void 0!==n&&"string"==typeof t&&"string"==typeof o){var d=window.QSI,r=d.windowHandler,a=d.dbg,w=r.getWin(t);if(w){var s=new i("setEmbeddedData",{key:e,value:n}),c=JSON.stringify(s);if(/targetwindow/.test(t))w.postMessage(c,o);else try{var g=w.document.getElementById("PopUnderTargetFrame");if(g&&g.contentWindow)g.contentWindow.postMessage(c,o)}catch(e){a.e(e)}}}},a=function(){var e=window.QSI.dbg;try{var n=window.QSI.windowHandler;n.removeClosedWindowHandles();var t=n.getOptInIDsAndWindowNames()||{},i=n.getOptInIDsAndTargetOrigins()||{};for(var o in t)if(Object.prototype.hasOwnProperty.call(t,o)){var a=t[o],w=i[o]||"*",s=window.QSI.EmbeddedData.getEmbeddedData(o);if(!s||window.QSI.util.isObjectEmpty(s))continue;if(window.QSI.reg[o]&&/placeholderWindow/.test(a)){var c=window.QSI.reg[o].getTarget();return void d(c,a)}for(var g in s)Object.prototype.hasOwnProperty.call(s,g)&&r(g,s[g],a,w)}}catch(n){e.e(n)}}}}]);
} catch(e) {
  if (typeof QSI !== 'undefined' && QSI.dbg && QSI.dbg.e) {
    QSI.dbg.e(e);
  }
}