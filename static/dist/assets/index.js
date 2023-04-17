(function(){const e=document.createElement("link").relList;if(e&&e.supports&&e.supports("modulepreload"))return;for(const s of document.querySelectorAll('link[rel="modulepreload"]'))n(s);new MutationObserver(s=>{for(const r of s)if(r.type==="childList")for(const i of r.addedNodes)i.tagName==="LINK"&&i.rel==="modulepreload"&&n(i)}).observe(document,{childList:!0,subtree:!0});function t(s){const r={};return s.integrity&&(r.integrity=s.integrity),s.referrerPolicy&&(r.referrerPolicy=s.referrerPolicy),s.crossOrigin==="use-credentials"?r.credentials="include":s.crossOrigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function n(s){if(s.ep)return;s.ep=!0;const r=t(s);fetch(s.href,r)}})();const g=`<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.9493 23.6164L21.6168 14.9491C21.8642 14.7017 22 14.372 22 14.0204C22 13.6684 21.864 13.3388 21.6168 13.0914L20.8297 12.3045C20.5826 12.0573 20.2527 11.9211 19.9009 11.9211C19.5493 11.9211 19.2082 12.0573 18.9612 12.3045L13.8937 17.3608L13.8937 1.29657C13.8937 0.572288 13.3267 0 12.6022 0L11.4895 0C10.765 0 10.1408 0.572288 10.1408 1.29657L10.1408 17.4182L5.04502 12.3047C4.79761 12.0575 4.47663 11.9213 4.12483 11.9213C3.77342 11.9213 3.44776 12.0575 3.20055 12.3047L2.41597 13.0916C2.16856 13.339 2.03373 13.6686 2.03373 14.0206C2.03373 14.3722 2.17031 14.7019 2.41772 14.9493L11.085 23.6166C11.3332 23.8646 11.6645 24.001 12.0167 24C12.37 24.0008 12.7015 23.8646 12.9493 23.6164Z" fill="currentColor"/>
</svg>
`,A=Object.freeze(Object.defineProperty({__proto__:null,default:g},Symbol.toStringTag,{value:"Module"})),E=()=>{const o=document.querySelectorAll(".accordion li"),e=t=>{var n;(n=t.parentNode)==null||n.querySelectorAll("[aria-selected]").forEach(s=>s.removeAttribute("aria-selected"))};document.querySelectorAll(".accordion .icon").forEach(t=>{t.insertAdjacentHTML("beforeend",g)}),document.querySelectorAll(".accordion-content").forEach(t=>{const n=`wrapper-${crypto.randomUUID()}`,s=`button-${crypto.randomUUID()}`,r=document.createElement("div"),i=t.parentNode,c=i==null?void 0:i.querySelector("button");r.classList.add("accordion-content-wrapper"),r.setAttribute("id",n),r.setAttribute("role","region"),r.setAttribute("aria-labelledby",s),r==null||r.addEventListener("transitionend",()=>r.setAttribute("style","")),i==null||i.insertBefore(r,t),c==null||c.setAttribute("aria-controls",n),c==null||c.setAttribute("id",s),c==null||c.setAttribute("aria-expanded",new Boolean(c==null?void 0:c.hasAttribute("aria-selected")).toString()),r.appendChild(t)}),o.forEach(t=>{const n=t.querySelector("button"),s=t.querySelector(".accordion-content-wrapper"),r=s==null?void 0:s.querySelector(".accordion-content");n==null||n.addEventListener("click",()=>{const i=n.parentNode;if(i!=null&&i.hasAttribute("aria-selected")){const c=r==null?void 0:r.clientHeight;s==null||s.setAttribute("style",`height:${c}px`),e(t),n.setAttribute("aria-expanded","false")}else{e(t),i.setAttribute("aria-selected","true");const c=r==null?void 0:r.clientHeight;s==null||s.setAttribute("style",`max-height:${c}px`),n.setAttribute("aria-expanded","true")}})})},_=()=>{document.querySelectorAll(".card.with-accordion").forEach(o=>{const e=o.querySelector("header"),t=o.querySelector(".content"),n=crypto.randomUUID(),s=`content-${n}`,r=`button-${n}`,i=e==null?void 0:e.getAttribute("aria-expanded"),c=i==="true"||i===null;!e||!t||(e.setAttribute("role","button"),e.setAttribute("aria-expanded",(!!c).toString()),e.setAttribute("aria-controls",s),e.setAttribute("id",r),t.setAttribute("id",s),t.setAttribute("aria-labelledby",r),t.setAttribute("role","region"),e.addEventListener("click",()=>{const d=e.getAttribute("aria-expanded")==="true";e.setAttribute("aria-expanded",String(!d))}))})},L="modulepreload",w=function(o){return"/"+o},f={},l=function(e,t,n){if(!t||t.length===0)return e();const s=document.getElementsByTagName("link");return Promise.all(t.map(r=>{if(r=w(r),r in f)return;f[r]=!0;const i=r.endsWith(".css"),c=i?'[rel="stylesheet"]':"";if(!!n)for(let u=s.length-1;u>=0;u--){const m=s[u];if(m.href===r&&(!i||m.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${r}"]${c}`))return;const a=document.createElement("link");if(a.rel=i?"stylesheet":L,i||(a.as="script",a.crossOrigin=""),a.href=r,document.head.appendChild(a),i)return new Promise((u,m)=>{a.addEventListener("load",u),a.addEventListener("error",()=>m(new Error(`Unable to preload CSS for ${r}`)))})})).then(()=>e())},S=(o,e)=>{const t=o[e];return t?typeof t=="function"?t():Promise.resolve(t):new Promise((n,s)=>{(typeof queueMicrotask=="function"?queueMicrotask:setTimeout)(s.bind(null,new Error("Unknown variable dynamic import: "+e)))})},x=()=>{const o="icon-";document.querySelectorAll(`i[class^="${o}"]`).forEach(async e=>{const t=e.className.replace(o,""),n=await S(Object.assign({"../svg/add.svg":()=>l(()=>import("./add.js"),[]),"../svg/arrow-down.svg":()=>l(()=>Promise.resolve().then(()=>A),void 0),"../svg/arrow-up.svg":()=>l(()=>import("./arrow-up.js"),[]),"../svg/calendar.svg":()=>l(()=>import("./calendar.js"),[]),"../svg/chevron-down.svg":()=>l(()=>import("./chevron-down.js"),[]),"../svg/crest.svg":()=>l(()=>import("./crest.js"),[]),"../svg/cross.svg":()=>l(()=>import("./cross.js"),[]),"../svg/logo.svg":()=>l(()=>import("./logo.js"),[]),"../svg/menu.svg":()=>l(()=>import("./menu.js"),[]),"../svg/new-tab.svg":()=>l(()=>import("./new-tab.js"),[]),"../svg/pencil.svg":()=>l(()=>import("./pencil.js"),[]),"../svg/search.svg":()=>l(()=>import("./search.js"),[]),"../svg/tick.svg":()=>l(()=>import("./tick.js"),[])}),`../svg/${t}.svg`);e.outerHTML=n.default})},b=o=>{const e=o==null?void 0:o.parentNode,{value:t}=o,n="has-value";return t?e==null?void 0:e.classList.add(n):e==null?void 0:e.classList.remove(n)},C=()=>{document.querySelectorAll(".select select").forEach(o=>{b(o),o.addEventListener("change",e=>b(e.target))})};const h=(o,e)=>{var n;const t=o.closest("form");(n=t.querySelector('input[type="hidden"][name="active_filter"]'))==null||n.setAttribute("value",e||""),t&&t.submit()},q=o=>{o.querySelectorAll('button[type="reset"]').forEach(e=>{e.addEventListener("click",()=>{var n;const t=o.querySelectorAll("input[type=checkbox][name]:checked");t.forEach(s=>{s.removeAttribute("checked"),s.checked=!1}),h(o,(n=t[0])==null?void 0:n.name)})})},O=o=>{o.querySelectorAll("input[data-controls]").forEach(e=>{e.addEventListener("keyup",()=>{const t=e.value.toLowerCase(),{controls:n}=e.dataset;o.querySelectorAll(`input[type=checkbox][name=${n}][value]`).forEach(s=>{var i;const r=s.closest(".row");r&&((i=r==null?void 0:r.textContent)!=null&&i.toLowerCase().includes(t)?r.style.display="block":r.style.display="none")})})})},P=o=>{o.querySelectorAll('input[type="checkbox"]').forEach(e=>{e.addEventListener("change",()=>{const{name:t}=e;h(o,t)})})},D=()=>{document.querySelectorAll(".filter-control").forEach(o=>{q(o),P(o),O(o)})};function k(o,e=!1,t=0,n){const s=o.getBoundingClientRect();if(e&&s.top>=0&&s.bottom<=window.innerHeight){n&&n();return}if(n){let r=window.pageYOffset,i=!1;const c=()=>{window.pageYOffset===r?(i=!1,n()):(r=window.pageYOffset,requestAnimationFrame(c))},d=()=>{i||(i=!0,requestAnimationFrame(c))};window.addEventListener("scroll",d)}window.scrollTo({top:s.top+window.pageYOffset-t,behavior:"smooth"})}const I=()=>{document.querySelectorAll("a.smooth-scroll").forEach(o=>{o.addEventListener("click",e=>{var s;e.preventDefault();const t=(s=e.target)==null?void 0:s.getAttribute("href"),n=t&&document.querySelector(t);n&&(n.classList.remove("scrolled"),n.classList.add("scrolling"),k(n,!0,16,()=>{n.classList.remove("scrolling"),n.classList.add("scrolled")}))})})},v=o=>{var e,t;o?(e=document.querySelector("body"))==null||e.classList.add("darken"):(t=document.querySelector("body"))==null||t.classList.remove("darken"),document.getElementById("main-header-mobile-menu").setAttribute("aria-expanded",(!!o).toString())},T=()=>v(!1),R=()=>{var o;(o=document.getElementById("main-header-mobile-menu"))==null||o.addEventListener("click",e=>v(e.currentTarget.getAttribute("aria-expanded")!=="true"))};class $ extends HTMLDivElement{constructor(){super(),this.setupDom()}setupDom(){const e=crypto.randomUUID(),t=`content_${e}`,n=`button_${e}`,s=this.querySelector(".content");if(!s)return;const r=document.createElement("button");r.setAttribute("id",n),r.classList.add("txt-link"),r.setAttribute("aria-expanded",this.dataset.open||"false"),r.setAttribute("aria-controls",t),r.innerHTML=(this.getAttribute("aria-label")||"Hint")+g,r.addEventListener("click",()=>{const d=r.getAttribute("aria-expanded")==="true";r.setAttribute("aria-expanded",String(!d))}),this.prepend(r);const i=document.createElement("div"),c=s.parentNode;i.classList.add("content-wrapper"),i.setAttribute("id",t),i.setAttribute("aria-labelledby",n),i.setAttribute("role","region"),c==null||c.insertBefore(i,s),i.appendChild(s)}}const B=()=>{customElements.define("hint-box",$,{extends:"div"})};function N(o){return Array.isArray(o)?o.every(e=>typeof e=="object"&&typeof e.color=="string"&&typeof e.percentage=="number"&&e.percentage>=0&&e.percentage<=100):!1}function H(o,e){const t=document.createElementNS("http://www.w3.org/2000/svg","svg");t.setAttribute("viewBox","0 0 100 100"),t.classList.add("progress-bar");const n=document.createElementNS("http://www.w3.org/2000/svg","circle");n.setAttribute("cx","50"),n.setAttribute("cy","50"),n.setAttribute("r","40"),n.classList.add("progress-bar-background"),t.appendChild(n);const s=e.reduce((c,d)=>c+d.percentage,0);let r=0;e.forEach(c=>{let d=-90-s/2*1.5-60;const a=document.createElementNS("http://www.w3.org/2000/svg","circle");a.setAttribute("cx","50"),a.setAttribute("cy","50"),a.setAttribute("r","40"),a.classList.add("progress-bar-foreground"),a.style.stroke=c.color,a.style.strokeDasharray="0",a.style.strokeDashoffset="0",a.style.transformOrigin="50% 50%",a.style.transform=`rotate(${r*360/100+d}deg)`,t.appendChild(a);const u=a.getAttribute("r");if(typeof u=="string"){const m=parseFloat(u),p=2*Math.PI*m,y=p*(1-c.percentage/100);a.style.strokeDasharray=`${p} ${p}`,a.style.strokeDashoffset=y.toString()}else console.error("Failed to retrieve the radius attribute from the progressCircle element");r+=c.percentage});const i=document.createElementNS("http://www.w3.org/2000/svg","rect");i.setAttribute("x","50"),i.setAttribute("y","11"),i.setAttribute("width","2"),i.setAttribute("height","25"),i.style.fill="var(--color-purple)",i.style.transformOrigin="50% 50%",i.style.transform="rotate(160deg) translateY(-14%)",t.appendChild(i),o.appendChild(t)}const V=()=>{document.querySelectorAll(".circular-progress-bar").forEach(e=>{try{const t=JSON.parse(e.getAttribute("data-segments")||"null");N(t)?H(e,t):console.error("Invalid data-segments attribute:",e.getAttribute("data-segments"))}catch(t){t instanceof Error?console.error("Failed to parse data-segments:",t.message):console.error("Failed to parse data-segments:",t)}})};window.addEventListener("load",()=>{globalThis.devMode||(E(),_(),x(),C(),D(),I(),R(),B(),V())});window.addEventListener("DOMContentLoaded",()=>{const o=window.matchMedia("(min-width: 800px)"),e=()=>{o.matches&&T()};o.addEventListener("change",e)});
