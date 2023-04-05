(function(){const o=document.createElement("link").relList;if(o&&o.supports&&o.supports("modulepreload"))return;for(const n of document.querySelectorAll('link[rel="modulepreload"]'))r(n);new MutationObserver(n=>{for(const s of n)if(s.type==="childList")for(const c of s.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&r(c)}).observe(document,{childList:!0,subtree:!0});function t(n){const s={};return n.integrity&&(s.integrity=n.integrity),n.referrerPolicy&&(s.referrerPolicy=n.referrerPolicy),n.crossOrigin==="use-credentials"?s.credentials="include":n.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function r(n){if(n.ep)return;n.ep=!0;const s=t(n);fetch(n.href,s)}})();const Z=`<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.9493 23.6164L21.6168 14.9491C21.8642 14.7017 22 14.372 22 14.0204C22 13.6684 21.864 13.3388 21.6168 13.0914L20.8297 12.3045C20.5826 12.0573 20.2527 11.9211 19.9009 11.9211C19.5493 11.9211 19.2082 12.0573 18.9612 12.3045L13.8937 17.3608L13.8937 1.29657C13.8937 0.572288 13.3267 0 12.6022 0L11.4895 0C10.765 0 10.1408 0.572288 10.1408 1.29657L10.1408 17.4182L5.04502 12.3047C4.79761 12.0575 4.47663 11.9213 4.12483 11.9213C3.77342 11.9213 3.44776 12.0575 3.20055 12.3047L2.41597 13.0916C2.16856 13.339 2.03373 13.6686 2.03373 14.0206C2.03373 14.3722 2.17031 14.7019 2.41772 14.9493L11.085 23.6166C11.3332 23.8646 11.6645 24.001 12.0167 24C12.37 24.0008 12.7015 23.8646 12.9493 23.6164Z" fill="currentColor"/>
</svg>
`,ne=Object.freeze(Object.defineProperty({__proto__:null,default:Z},Symbol.toStringTag,{value:"Module"}));function oe(e){if(e.__esModule)return e;var o=e.default;if(typeof o=="function"){var t=function r(){if(this instanceof r){var n=[null];n.push.apply(n,arguments);var s=Function.bind.apply(o,n);return new s}return o.apply(this,arguments)};t.prototype=o.prototype}else t={};return Object.defineProperty(t,"__esModule",{value:!0}),Object.keys(e).forEach(function(r){var n=Object.getOwnPropertyDescriptor(e,r);Object.defineProperty(t,r,n.get?n:{enumerable:!0,get:function(){return e[r]}})}),t}var O,se=new Uint8Array(16);function J(){if(!O&&(O=typeof crypto<"u"&&crypto.getRandomValues&&crypto.getRandomValues.bind(crypto)||typeof msCrypto<"u"&&typeof msCrypto.getRandomValues=="function"&&msCrypto.getRandomValues.bind(msCrypto),!O))throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported");return O(se)}const ce=/^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i;function q(e){return typeof e=="string"&&ce.test(e)}var d=[];for(var k=0;k<256;++k)d.push((k+256).toString(16).substr(1));function T(e){var o=arguments.length>1&&arguments[1]!==void 0?arguments[1]:0,t=(d[e[o+0]]+d[e[o+1]]+d[e[o+2]]+d[e[o+3]]+"-"+d[e[o+4]]+d[e[o+5]]+"-"+d[e[o+6]]+d[e[o+7]]+"-"+d[e[o+8]]+d[e[o+9]]+"-"+d[e[o+10]]+d[e[o+11]]+d[e[o+12]]+d[e[o+13]]+d[e[o+14]]+d[e[o+15]]).toLowerCase();if(!q(t))throw TypeError("Stringified UUID is invalid");return t}var X,D,M=0,P=0;function ae(e,o,t){var r=o&&t||0,n=o||new Array(16);e=e||{};var s=e.node||X,c=e.clockseq!==void 0?e.clockseq:D;if(s==null||c==null){var a=e.random||(e.rng||J)();s==null&&(s=X=[a[0]|1,a[1],a[2],a[3],a[4],a[5]]),c==null&&(c=D=(a[6]<<8|a[7])&16383)}var i=e.msecs!==void 0?e.msecs:Date.now(),f=e.nsecs!==void 0?e.nsecs:P+1,l=i-M+(f-P)/1e4;if(l<0&&e.clockseq===void 0&&(c=c+1&16383),(l<0||i>M)&&e.nsecs===void 0&&(f=0),f>=1e4)throw new Error("uuid.v1(): Can't create more than 10M uuids/sec");M=i,P=f,D=c,i+=122192928e5;var u=((i&268435455)*1e4+f)%4294967296;n[r++]=u>>>24&255,n[r++]=u>>>16&255,n[r++]=u>>>8&255,n[r++]=u&255;var p=i/4294967296*1e4&268435455;n[r++]=p>>>8&255,n[r++]=p&255,n[r++]=p>>>24&15|16,n[r++]=p>>>16&255,n[r++]=c>>>8|128,n[r++]=c&255;for(var w=0;w<6;++w)n[r+w]=s[w];return o||T(n)}function Q(e){if(!q(e))throw TypeError("Invalid UUID");var o,t=new Uint8Array(16);return t[0]=(o=parseInt(e.slice(0,8),16))>>>24,t[1]=o>>>16&255,t[2]=o>>>8&255,t[3]=o&255,t[4]=(o=parseInt(e.slice(9,13),16))>>>8,t[5]=o&255,t[6]=(o=parseInt(e.slice(14,18),16))>>>8,t[7]=o&255,t[8]=(o=parseInt(e.slice(19,23),16))>>>8,t[9]=o&255,t[10]=(o=parseInt(e.slice(24,36),16))/1099511627776&255,t[11]=o/4294967296&255,t[12]=o>>>24&255,t[13]=o>>>16&255,t[14]=o>>>8&255,t[15]=o&255,t}function ie(e){e=unescape(encodeURIComponent(e));for(var o=[],t=0;t<e.length;++t)o.push(e.charCodeAt(t));return o}var fe="6ba7b810-9dad-11d1-80b4-00c04fd430c8",le="6ba7b811-9dad-11d1-80b4-00c04fd430c8";function z(e,o,t){function r(n,s,c,a){if(typeof n=="string"&&(n=ie(n)),typeof s=="string"&&(s=Q(s)),s.length!==16)throw TypeError("Namespace must be array-like (16 iterable integer values, 0-255)");var i=new Uint8Array(16+n.length);if(i.set(s),i.set(n,s.length),i=t(i),i[6]=i[6]&15|o,i[8]=i[8]&63|128,c){a=a||0;for(var f=0;f<16;++f)c[a+f]=i[f];return c}return T(i)}try{r.name=e}catch{}return r.DNS=fe,r.URL=le,r}function ue(e){if(typeof e=="string"){var o=unescape(encodeURIComponent(e));e=new Uint8Array(o.length);for(var t=0;t<o.length;++t)e[t]=o.charCodeAt(t)}return de(ve(he(e),e.length*8))}function de(e){for(var o=[],t=e.length*32,r="0123456789abcdef",n=0;n<t;n+=8){var s=e[n>>5]>>>n%32&255,c=parseInt(r.charAt(s>>>4&15)+r.charAt(s&15),16);o.push(c)}return o}function W(e){return(e+64>>>9<<4)+14+1}function ve(e,o){e[o>>5]|=128<<o%32,e[W(o)-1]=o;for(var t=1732584193,r=-271733879,n=-1732584194,s=271733878,c=0;c<e.length;c+=16){var a=t,i=r,f=n,l=s;t=v(t,r,n,s,e[c],7,-680876936),s=v(s,t,r,n,e[c+1],12,-389564586),n=v(n,s,t,r,e[c+2],17,606105819),r=v(r,n,s,t,e[c+3],22,-1044525330),t=v(t,r,n,s,e[c+4],7,-176418897),s=v(s,t,r,n,e[c+5],12,1200080426),n=v(n,s,t,r,e[c+6],17,-1473231341),r=v(r,n,s,t,e[c+7],22,-45705983),t=v(t,r,n,s,e[c+8],7,1770035416),s=v(s,t,r,n,e[c+9],12,-1958414417),n=v(n,s,t,r,e[c+10],17,-42063),r=v(r,n,s,t,e[c+11],22,-1990404162),t=v(t,r,n,s,e[c+12],7,1804603682),s=v(s,t,r,n,e[c+13],12,-40341101),n=v(n,s,t,r,e[c+14],17,-1502002290),r=v(r,n,s,t,e[c+15],22,1236535329),t=h(t,r,n,s,e[c+1],5,-165796510),s=h(s,t,r,n,e[c+6],9,-1069501632),n=h(n,s,t,r,e[c+11],14,643717713),r=h(r,n,s,t,e[c],20,-373897302),t=h(t,r,n,s,e[c+5],5,-701558691),s=h(s,t,r,n,e[c+10],9,38016083),n=h(n,s,t,r,e[c+15],14,-660478335),r=h(r,n,s,t,e[c+4],20,-405537848),t=h(t,r,n,s,e[c+9],5,568446438),s=h(s,t,r,n,e[c+14],9,-1019803690),n=h(n,s,t,r,e[c+3],14,-187363961),r=h(r,n,s,t,e[c+8],20,1163531501),t=h(t,r,n,s,e[c+13],5,-1444681467),s=h(s,t,r,n,e[c+2],9,-51403784),n=h(n,s,t,r,e[c+7],14,1735328473),r=h(r,n,s,t,e[c+12],20,-1926607734),t=g(t,r,n,s,e[c+5],4,-378558),s=g(s,t,r,n,e[c+8],11,-2022574463),n=g(n,s,t,r,e[c+11],16,1839030562),r=g(r,n,s,t,e[c+14],23,-35309556),t=g(t,r,n,s,e[c+1],4,-1530992060),s=g(s,t,r,n,e[c+4],11,1272893353),n=g(n,s,t,r,e[c+7],16,-155497632),r=g(r,n,s,t,e[c+10],23,-1094730640),t=g(t,r,n,s,e[c+13],4,681279174),s=g(s,t,r,n,e[c],11,-358537222),n=g(n,s,t,r,e[c+3],16,-722521979),r=g(r,n,s,t,e[c+6],23,76029189),t=g(t,r,n,s,e[c+9],4,-640364487),s=g(s,t,r,n,e[c+12],11,-421815835),n=g(n,s,t,r,e[c+15],16,530742520),r=g(r,n,s,t,e[c+2],23,-995338651),t=m(t,r,n,s,e[c],6,-198630844),s=m(s,t,r,n,e[c+7],10,1126891415),n=m(n,s,t,r,e[c+14],15,-1416354905),r=m(r,n,s,t,e[c+5],21,-57434055),t=m(t,r,n,s,e[c+12],6,1700485571),s=m(s,t,r,n,e[c+3],10,-1894986606),n=m(n,s,t,r,e[c+10],15,-1051523),r=m(r,n,s,t,e[c+1],21,-2054922799),t=m(t,r,n,s,e[c+8],6,1873313359),s=m(s,t,r,n,e[c+15],10,-30611744),n=m(n,s,t,r,e[c+6],15,-1560198380),r=m(r,n,s,t,e[c+13],21,1309151649),t=m(t,r,n,s,e[c+4],6,-145523070),s=m(s,t,r,n,e[c+11],10,-1120210379),n=m(n,s,t,r,e[c+2],15,718787259),r=m(r,n,s,t,e[c+9],21,-343485551),t=A(t,a),r=A(r,i),n=A(n,f),s=A(s,l)}return[t,r,n,s]}function he(e){if(e.length===0)return[];for(var o=e.length*8,t=new Uint32Array(W(o)),r=0;r<o;r+=8)t[r>>5]|=(e[r/8]&255)<<r%32;return t}function A(e,o){var t=(e&65535)+(o&65535),r=(e>>16)+(o>>16)+(t>>16);return r<<16|t&65535}function ge(e,o){return e<<o|e>>>32-o}function R(e,o,t,r,n,s){return A(ge(A(A(o,e),A(r,s)),n),t)}function v(e,o,t,r,n,s,c){return R(o&t|~o&r,e,o,n,s,c)}function h(e,o,t,r,n,s,c){return R(o&r|t&~r,e,o,n,s,c)}function g(e,o,t,r,n,s,c){return R(o^t^r,e,o,n,s,c)}function m(e,o,t,r,n,s,c){return R(t^(o|~r),e,o,n,s,c)}var me=z("v3",48,ue);const pe=me;function ye(e,o,t){e=e||{};var r=e.random||(e.rng||J)();if(r[6]=r[6]&15|64,r[8]=r[8]&63|128,o){t=t||0;for(var n=0;n<16;++n)o[t+n]=r[n];return o}return T(r)}function we(e,o,t,r){switch(e){case 0:return o&t^~o&r;case 1:return o^t^r;case 2:return o&t^o&r^t&r;case 3:return o^t^r}}function V(e,o){return e<<o|e>>>32-o}function Ae(e){var o=[1518500249,1859775393,2400959708,3395469782],t=[1732584193,4023233417,2562383102,271733878,3285377520];if(typeof e=="string"){var r=unescape(encodeURIComponent(e));e=[];for(var n=0;n<r.length;++n)e.push(r.charCodeAt(n))}else Array.isArray(e)||(e=Array.prototype.slice.call(e));e.push(128);for(var s=e.length/4+2,c=Math.ceil(s/16),a=new Array(c),i=0;i<c;++i){for(var f=new Uint32Array(16),l=0;l<16;++l)f[l]=e[i*64+l*4]<<24|e[i*64+l*4+1]<<16|e[i*64+l*4+2]<<8|e[i*64+l*4+3];a[i]=f}a[c-1][14]=(e.length-1)*8/Math.pow(2,32),a[c-1][14]=Math.floor(a[c-1][14]),a[c-1][15]=(e.length-1)*8&4294967295;for(var u=0;u<c;++u){for(var p=new Uint32Array(80),w=0;w<16;++w)p[w]=a[u][w];for(var E=16;E<80;++E)p[E]=V(p[E-3]^p[E-8]^p[E-14]^p[E-16],1);for(var L=t[0],_=t[1],S=t[2],I=t[3],U=t[4],C=0;C<80;++C){var F=Math.floor(C/20),re=V(L,5)+we(F,_,S,I)+U+o[F]+p[C]>>>0;U=I,I=S,S=V(_,30)>>>0,_=L,L=re}t[0]=t[0]+L>>>0,t[1]=t[1]+_>>>0,t[2]=t[2]+S>>>0,t[3]=t[3]+I>>>0,t[4]=t[4]+U>>>0}return[t[0]>>24&255,t[0]>>16&255,t[0]>>8&255,t[0]&255,t[1]>>24&255,t[1]>>16&255,t[1]>>8&255,t[1]&255,t[2]>>24&255,t[2]>>16&255,t[2]>>8&255,t[2]&255,t[3]>>24&255,t[3]>>16&255,t[3]>>8&255,t[3]&255,t[4]>>24&255,t[4]>>16&255,t[4]>>8&255,t[4]&255]}var Ee=z("v5",80,Ae);const be=Ee,Le="00000000-0000-0000-0000-000000000000";function _e(e){if(!q(e))throw TypeError("Invalid UUID");return parseInt(e.substr(14,1),16)}const Se=Object.freeze(Object.defineProperty({__proto__:null,NIL:Le,parse:Q,stringify:T,v1:ae,v3:pe,v4:ye,v5:be,validate:q,version:_e},Symbol.toStringTag,{value:"Module"})),Ie=oe(Se);function j(e,o){if(!e||!o||!e.length||!o.length)throw new Error("Bad alphabet");this.srcAlphabet=e,this.dstAlphabet=o}j.prototype.convert=function(e){var o,t,r,n={},s=this.srcAlphabet.length,c=this.dstAlphabet.length,a=e.length,i=typeof e=="string"?"":[];if(!this.isValid(e))throw new Error('Number "'+e+'" contains of non-alphabetic digits ('+this.srcAlphabet+")");if(this.srcAlphabet===this.dstAlphabet)return e;for(o=0;o<a;o++)n[o]=this.srcAlphabet.indexOf(e[o]);do{for(t=0,r=0,o=0;o<a;o++)t=t*s+n[o],t>=c?(n[r++]=parseInt(t/c,10),t=t%c):r>0&&(n[r++]=0);a=r,i=this.dstAlphabet.slice(t,t+1).concat(i)}while(r!==0);return i};j.prototype.isValid=function(e){for(var o=0;o<e.length;++o)if(this.srcAlphabet.indexOf(e[o])===-1)return!1;return!0};var Ce=j,Oe=Ce;function b(e,o){var t=new Oe(e,o);return function(r){return t.convert(r)}}b.BIN="01";b.OCT="01234567";b.DEC="0123456789";b.HEX="0123456789abcdef";var xe=b;const{v4:$}=Ie,x=xe,N="123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ",qe="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+-./:<=>?@[]^_`{|}~",Te={consistentLength:!0};let H;const Y=(e,o,t)=>{const r=o(e.toLowerCase().replace(/-/g,""));return!t||!t.consistentLength?r:r.padStart(t.shortIdLength,t.paddingChar)},Re=(e,o)=>{const r=o(e).padStart(32,"0").match(/(\w{8})(\w{4})(\w{4})(\w{4})(\w{12})/);return[r[1],r[2],r[3],r[4],r[5]].join("-")},Ue=e=>Math.ceil(Math.log(2**128)/Math.log(e));var B=(()=>{const e=(o,t)=>{const r=o||N,n={...Te,...t};if([...new Set(Array.from(r))].length!==r.length)throw new Error("The provided Alphabet has duplicate characters resulting in unreliable results");const s=Ue(r.length),c={shortIdLength:s,consistentLength:n.consistentLength,paddingChar:r[0]},a=x(x.HEX,r),i=x(r,x.HEX),f=()=>Y($(),a,c),l={new:f,generate:f,uuid:$,fromUUID:u=>Y(u,a,c),toUUID:u=>Re(u,i),alphabet:r,maxLength:s};return Object.freeze(l),l};return e.constants={flickrBase58:N,cookieBase90:qe},e.uuid=$,e.generate=()=>(H||(H=e(N).generate),H()),e})();const ke=()=>{const e=document.querySelectorAll(".accordion li"),o=t=>{var r;(r=t.parentNode)==null||r.querySelectorAll(".active").forEach(n=>n.classList.remove("active"))};document.querySelectorAll(".accordion .icon").forEach(t=>{t.insertAdjacentHTML("beforeend",Z)}),document.querySelectorAll(".accordion-content").forEach(t=>{const r=`wrapper-${B.generate()}`,n=`button-${B.generate()}`,s=document.createElement("div"),c=t.parentNode,a=c==null?void 0:c.querySelector("button");s.classList.add("accordion-content-wrapper"),s.setAttribute("id",r),s.setAttribute("role","region"),s.setAttribute("aria-labelledby",n),s==null||s.addEventListener("transitionend",()=>s.setAttribute("style","")),c==null||c.insertBefore(s,t),a==null||a.setAttribute("aria-controls",r),a==null||a.setAttribute("id",n),a==null||a.setAttribute("aria-expanded",new Boolean(a==null?void 0:a.classList.contains("active")).toString()),s.appendChild(t)}),e.forEach(t=>{const r=t.querySelector("button"),n=t.querySelector(".accordion-content-wrapper"),s=n==null?void 0:n.querySelector(".accordion-content");r==null||r.addEventListener("click",()=>{const c=r.parentNode;if(c!=null&&c.classList.contains("active")){const a=s==null?void 0:s.clientHeight;n==null||n.setAttribute("style",`height:${a}px`),o(t),r.setAttribute("aria-expanded","false")}else{o(t),c.classList.add("active");const a=s==null?void 0:s.clientHeight;n==null||n.setAttribute("style",`max-height:${a}px`),r.setAttribute("aria-expanded","true")}})})},De=()=>{document.querySelectorAll(".card.with-accordion").forEach(e=>{const o=e.querySelector("header"),t=e.querySelector(".content"),r=B.generate(),n=`content-${r}`,s=`button-${r}`,c=o==null?void 0:o.getAttribute("aria-expanded"),a=c==="true"||c===null;!o||!t||(o.setAttribute("role","button"),o.setAttribute("aria-expanded",(!!a).toString()),o.setAttribute("aria-controls",n),o.setAttribute("id",s),t.setAttribute("id",n),t.setAttribute("aria-labelledby",s),t.setAttribute("role","region"),o.addEventListener("click",()=>{const i=o.getAttribute("aria-expanded")==="true";o.setAttribute("aria-expanded",String(!i))}))})},Me="modulepreload",Pe=function(e){return"/"+e},K={},y=function(o,t,r){if(!t||t.length===0)return o();const n=document.getElementsByTagName("link");return Promise.all(t.map(s=>{if(s=Pe(s),s in K)return;K[s]=!0;const c=s.endsWith(".css"),a=c?'[rel="stylesheet"]':"";if(!!r)for(let l=n.length-1;l>=0;l--){const u=n[l];if(u.href===s&&(!c||u.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${s}"]${a}`))return;const f=document.createElement("link");if(f.rel=c?"stylesheet":Me,c||(f.as="script",f.crossOrigin=""),f.href=s,document.head.appendChild(f),c)return new Promise((l,u)=>{f.addEventListener("load",l),f.addEventListener("error",()=>u(new Error(`Unable to preload CSS for ${s}`)))})})).then(()=>o())},Ve=(e,o)=>{const t=e[o];return t?typeof t=="function"?t():Promise.resolve(t):new Promise((r,n)=>{(typeof queueMicrotask=="function"?queueMicrotask:setTimeout)(n.bind(null,new Error("Unknown variable dynamic import: "+o)))})},$e=()=>{const e="icon-";document.querySelectorAll(`i[class^="${e}"]`).forEach(async o=>{const t=o.className.replace(e,""),r=await Ve(Object.assign({"../svg/add.svg":()=>y(()=>import("./add.js"),[]),"../svg/arrow-down.svg":()=>y(()=>Promise.resolve().then(()=>ne),void 0),"../svg/arrow-up.svg":()=>y(()=>import("./arrow-up.js"),[]),"../svg/chevron-down.svg":()=>y(()=>import("./chevron-down.js"),[]),"../svg/crest.svg":()=>y(()=>import("./crest.js"),[]),"../svg/cross.svg":()=>y(()=>import("./cross.js"),[]),"../svg/logo.svg":()=>y(()=>import("./logo.js"),[]),"../svg/menu.svg":()=>y(()=>import("./menu.js"),[]),"../svg/new-tab.svg":()=>y(()=>import("./new-tab.js"),[]),"../svg/search.svg":()=>y(()=>import("./search.js"),[]),"../svg/tick.svg":()=>y(()=>import("./tick.js"),[])}),`../svg/${t}.svg`);o.outerHTML=r.default})},G=e=>{const o=e==null?void 0:e.parentNode,{value:t}=e,r="has-value";return t?o==null?void 0:o.classList.add(r):o==null?void 0:o.classList.remove(r)},Ne=()=>{document.querySelectorAll(".select select").forEach(e=>{G(e),e.addEventListener("change",o=>G(o.target))})};const ee=(e,o)=>{var r;const t=e.closest("form");(r=t.querySelector('input[type="hidden"][name="active_filter"]'))==null||r.setAttribute("value",o||""),t&&t.submit()},He=e=>{e.querySelectorAll('button[type="reset"]').forEach(o=>{o.addEventListener("click",()=>{var r;const t=e.querySelectorAll("input[type=checkbox][name]:checked");t.forEach(n=>{n.removeAttribute("checked"),n.checked=!1}),ee(e,(r=t[0])==null?void 0:r.name)})})},Be=e=>{e.querySelectorAll("input[data-controls]").forEach(o=>{o.addEventListener("keyup",()=>{const t=o.value.toLowerCase(),{controls:r}=o.dataset;e.querySelectorAll(`input[type=checkbox][name=${r}][value]`).forEach(n=>{var c;const s=n.closest(".row");s&&((c=s==null?void 0:s.textContent)!=null&&c.toLowerCase().includes(t)?s.style.display="block":s.style.display="none")})})})},je=e=>{e.querySelectorAll('input[type="checkbox"]').forEach(o=>{o.addEventListener("change",()=>{const{name:t}=o;ee(e,t)})})},Fe=()=>{document.querySelectorAll(".filter-control").forEach(e=>{He(e),je(e),Be(e)})};function Xe(e,o=!1,t=0,r){const n=e.getBoundingClientRect();if(o&&n.top>=0&&n.bottom<=window.innerHeight){r&&r();return}if(r){let s=window.pageYOffset,c=!1;const a=()=>{window.pageYOffset===s?(c=!1,r()):(s=window.pageYOffset,requestAnimationFrame(a))},i=()=>{c||(c=!0,requestAnimationFrame(a))};window.addEventListener("scroll",i)}window.scrollTo({top:n.top+window.pageYOffset-t,behavior:"smooth"})}const Ye=()=>{document.querySelectorAll("a.smooth-scroll").forEach(e=>{e.addEventListener("click",o=>{var n;o.preventDefault();const t=(n=o.target)==null?void 0:n.getAttribute("href"),r=t&&document.querySelector(t);r&&(r.classList.remove("scrolled"),r.classList.add("scrolling"),Xe(r,!0,16,()=>{r.classList.remove("scrolling"),r.classList.add("scrolled")}))})})},te=e=>{var o,t;e?(o=document.querySelector("body"))==null||o.classList.add("darken"):(t=document.querySelector("body"))==null||t.classList.remove("darken"),document.getElementById("main-header-mobile-menu").setAttribute("aria-expanded",(!!e).toString())},Ke=()=>te(!1),Ge=()=>{var e;(e=document.getElementById("main-header-mobile-menu"))==null||e.addEventListener("click",o=>te(o.currentTarget.getAttribute("aria-expanded")==="false"))};window.addEventListener("load",()=>{globalThis.devMode||(ke(),De(),$e(),Ne(),Fe(),Ye(),Ge())});window.addEventListener("DOMContentLoaded",()=>{const e=window.matchMedia("(min-width: 800px)"),o=()=>{e.matches&&Ke()};e.addEventListener("change",o)});
