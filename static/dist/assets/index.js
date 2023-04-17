;(function () {
  const e = document.createElement('link').relList
  if (e && e.supports && e.supports('modulepreload')) return
  for (const s of document.querySelectorAll('link[rel="modulepreload"]')) n(s)
  new MutationObserver((s) => {
    for (const r of s)
      if (r.type === 'childList')
        for (const i of r.addedNodes)
          i.tagName === 'LINK' && i.rel === 'modulepreload' && n(i)
  }).observe(document, { childList: !0, subtree: !0 })
  function t(s) {
    const r = {}
    return (
      s.integrity && (r.integrity = s.integrity),
      s.referrerPolicy && (r.referrerPolicy = s.referrerPolicy),
      s.crossOrigin === 'use-credentials'
        ? (r.credentials = 'include')
        : s.crossOrigin === 'anonymous'
        ? (r.credentials = 'omit')
        : (r.credentials = 'same-origin'),
      r
    )
  }
  function n(s) {
    if (s.ep) return
    s.ep = !0
    const r = t(s)
    fetch(s.href, r)
  }
})()
const g = `<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.9493 23.6164L21.6168 14.9491C21.8642 14.7017 22 14.372 22 14.0204C22 13.6684 21.864 13.3388 21.6168 13.0914L20.8297 12.3045C20.5826 12.0573 20.2527 11.9211 19.9009 11.9211C19.5493 11.9211 19.2082 12.0573 18.9612 12.3045L13.8937 17.3608L13.8937 1.29657C13.8937 0.572288 13.3267 0 12.6022 0L11.4895 0C10.765 0 10.1408 0.572288 10.1408 1.29657L10.1408 17.4182L5.04502 12.3047C4.79761 12.0575 4.47663 11.9213 4.12483 11.9213C3.77342 11.9213 3.44776 12.0575 3.20055 12.3047L2.41597 13.0916C2.16856 13.339 2.03373 13.6686 2.03373 14.0206C2.03373 14.3722 2.17031 14.7019 2.41772 14.9493L11.085 23.6166C11.3332 23.8646 11.6645 24.001 12.0167 24C12.37 24.0008 12.7015 23.8646 12.9493 23.6164Z" fill="currentColor"/>
</svg>
`,
  b = Object.freeze(
    Object.defineProperty({ __proto__: null, default: f }, Symbol.toStringTag, {
      value: 'Module',
    })
  ),
  _ = () => {
    const r = document.querySelectorAll('.accordion li'),
      e = (n) => {
        var s
        ;(s = n.parentNode) == null ||
          s
            .querySelectorAll('[aria-selected]')
            .forEach((o) => o.removeAttribute('aria-selected'))
      }
    document.querySelectorAll('.accordion .icon').forEach((n) => {
      n.insertAdjacentHTML('beforeend', f)
    }),
      document.querySelectorAll('.accordion-content').forEach((n) => {
        const s = `wrapper-${crypto.randomUUID()}`,
          o = `button-${crypto.randomUUID()}`,
          t = document.createElement('div'),
          i = n.parentNode,
          c = i == null ? void 0 : i.querySelector('button')
        t.classList.add('accordion-content-wrapper'),
          t.setAttribute('id', s),
          t.setAttribute('role', 'region'),
          t.setAttribute('aria-labelledby', o),
          t == null ||
            t.addEventListener('transitionend', () =>
              t.setAttribute('style', '')
            ),
          i == null || i.insertBefore(t, n),
          c == null || c.setAttribute('aria-controls', s),
          c == null || c.setAttribute('id', o),
          c == null ||
            c.setAttribute(
              'aria-expanded',
              new Boolean(
                c == null ? void 0 : c.hasAttribute('aria-selected')
              ).toString()
            ),
          t.appendChild(n)
      }),
      r.forEach((n) => {
        const s = n.querySelector('button'),
          o = n.querySelector('.accordion-content-wrapper'),
          t = o == null ? void 0 : o.querySelector('.accordion-content')
        s == null ||
          s.addEventListener('click', () => {
            const i = s.parentNode
            if (i != null && i.hasAttribute('aria-selected')) {
              const c = t == null ? void 0 : t.clientHeight
              o == null || o.setAttribute('style', `height:${c}px`),
                e(n),
                s.setAttribute('aria-expanded', 'false')
            } else {
              e(n), i.setAttribute('aria-selected', 'true')
              const c = t == null ? void 0 : t.clientHeight
              o == null || o.setAttribute('style', `max-height:${c}px`),
                s.setAttribute('aria-expanded', 'true')
            }
          })
      })
  },
  A = () => {
    document.querySelectorAll('.card.with-accordion').forEach((r) => {
      const e = r.querySelector('header'),
        n = r.querySelector('.content'),
        s = crypto.randomUUID(),
        o = `content-${s}`,
        t = `button-${s}`,
        i = e == null ? void 0 : e.getAttribute('aria-expanded'),
        c = i === 'true' || i === null
      !e ||
        !n ||
        (e.setAttribute('role', 'button'),
        e.setAttribute('aria-expanded', (!!c).toString()),
        e.setAttribute('aria-controls', o),
        e.setAttribute('id', t),
        n.setAttribute('id', o),
        n.setAttribute('aria-labelledby', t),
        n.setAttribute('role', 'region'),
        e.addEventListener('click', () => {
          const d = e.getAttribute('aria-expanded') === 'true'
          e.setAttribute('aria-expanded', String(!d))
        }))
    })
  },
  E = 'modulepreload',
  y = function (r) {
    return '/' + r
  },
  p = {},
  l = function (e, n, s) {
    if (!n || n.length === 0) return e()
    const o = document.getElementsByTagName('link')
    return Promise.all(
      n.map((t) => {
        if (((t = y(t)), t in p)) return
        p[t] = !0
        const i = t.endsWith('.css'),
          c = i ? '[rel="stylesheet"]' : ''
        if (!!s)
          for (let u = o.length - 1; u >= 0; u--) {
            const m = o[u]
            if (m.href === t && (!i || m.rel === 'stylesheet')) return
          }
        else if (document.querySelector(`link[href="${t}"]${c}`)) return
        const a = document.createElement('link')
        if (
          ((a.rel = i ? 'stylesheet' : E),
          i || ((a.as = 'script'), (a.crossOrigin = '')),
          (a.href = t),
          document.head.appendChild(a),
          i)
        )
          return new Promise((u, m) => {
            a.addEventListener('load', u),
              a.addEventListener('error', () =>
                m(new Error(`Unable to preload CSS for ${t}`))
              )
          })
      })
    ).then(() => e())
  },
  L = (r, e) => {
    const n = r[e]
    return n
      ? typeof n == 'function'
        ? n()
        : Promise.resolve(n)
      : new Promise((s, o) => {
          ;(typeof queueMicrotask == 'function' ? queueMicrotask : setTimeout)(
            o.bind(null, new Error('Unknown variable dynamic import: ' + e))
          )
        })
  },
  w = () => {
    const r = 'icon-'
    document.querySelectorAll(`i[class^="${r}"]`).forEach(async (e) => {
      const n = e.className.replace(r, ''),
        s = await L(
          Object.assign({
            '../svg/add.svg': () => l(() => import('./add.js'), []),
            '../svg/arrow-down.svg': () =>
              l(() => Promise.resolve().then(() => b), void 0),
            '../svg/arrow-up.svg': () => l(() => import('./arrow-up.js'), []),
            '../svg/calendar.svg': () => l(() => import('./calendar.js'), []),
            '../svg/chevron-down.svg': () =>
              l(() => import('./chevron-down.js'), []),
            '../svg/crest.svg': () => l(() => import('./crest.js'), []),
            '../svg/cross.svg': () => l(() => import('./cross.js'), []),
            '../svg/logo.svg': () => l(() => import('./logo.js'), []),
            '../svg/menu.svg': () => l(() => import('./menu.js'), []),
            '../svg/new-tab.svg': () => l(() => import('./new-tab.js'), []),
            '../svg/pencil.svg': () => l(() => import('./pencil.js'), []),
            '../svg/search.svg': () => l(() => import('./search.js'), []),
            '../svg/tick.svg': () => l(() => import('./tick.js'), []),
          }),
          `../svg/${n}.svg`
        )
      e.outerHTML = s.default
    })
  },
  v = (r) => {
    const e = r == null ? void 0 : r.parentNode,
      { value: n } = r,
      s = 'has-value'
    return n
      ? e == null
        ? void 0
        : e.classList.add(s)
      : e == null
      ? void 0
      : e.classList.remove(s)
  },
  S = () => {
    document.querySelectorAll('.select select').forEach((r) => {
      v(r), r.addEventListener('change', (e) => v(e.target))
    })
  }
const g = (r, e) => {
    var s
    const n = r.closest('form')
    ;(s = n.querySelector('input[type="hidden"][name="active_filter"]')) ==
      null || s.setAttribute('value', e || ''),
      n && n.submit()
  },
  x = (r) => {
    r.querySelectorAll('button[type="reset"]').forEach((e) => {
      e.addEventListener('click', () => {
        var s
        const n = r.querySelectorAll('input[type=checkbox][name]:checked')
        n.forEach((o) => {
          o.removeAttribute('checked'), (o.checked = !1)
        }),
          g(r, (s = n[0]) == null ? void 0 : s.name)
      })
    })
  },
  q = (r) => {
    r.querySelectorAll('input[data-controls]').forEach((e) => {
      e.addEventListener('keyup', () => {
        const n = e.value.toLowerCase(),
          { controls: s } = e.dataset
        r.querySelectorAll(`input[type=checkbox][name=${s}][value]`).forEach(
          (o) => {
            var i
            const t = o.closest('.row')
            t &&
              ((i = t == null ? void 0 : t.textContent) != null &&
              i.toLowerCase().includes(n)
                ? (t.style.display = 'block')
                : (t.style.display = 'none'))
          }
        )
      })
    })
  },
  O = (r) => {
    r.querySelectorAll('input[type="checkbox"]').forEach((e) => {
      e.addEventListener('change', () => {
        const { name: n } = e
        g(r, n)
      })
    })
  },
  D = () => {
    document.querySelectorAll('.filter-control').forEach((r) => {
      x(r), O(r), q(r)
    })
  }
function I(r, e = !1, n = 0, s) {
  const o = r.getBoundingClientRect()
  if (e && o.top >= 0 && o.bottom <= window.innerHeight) {
    s && s()
    return
  }
  if (s) {
    let t = window.pageYOffset,
      i = !1
    const c = () => {
        window.pageYOffset === t
          ? ((i = !1), s())
          : ((t = window.pageYOffset), requestAnimationFrame(c))
      },
      d = () => {
        i || ((i = !0), requestAnimationFrame(c))
      }
    window.addEventListener('scroll', d)
  }
  window.scrollTo({ top: o.top + window.pageYOffset - n, behavior: 'smooth' })
}
const P = () => {
    document.querySelectorAll('a.smooth-scroll').forEach((r) => {
      r.addEventListener('click', (e) => {
        var o
        e.preventDefault()
        const n = (o = e.target) == null ? void 0 : o.getAttribute('href'),
          s = n && document.querySelector(n)
        s &&
          (s.classList.remove('scrolled'),
          s.classList.add('scrolling'),
          I(s, !0, 16, () => {
            s.classList.remove('scrolling'), s.classList.add('scrolled')
          }))
      })
    })
  },
  h = (r) => {
    var e, n
    r
      ? (e = document.querySelector('body')) == null ||
        e.classList.add('darken')
      : (n = document.querySelector('body')) == null ||
        n.classList.remove('darken'),
      document
        .getElementById('main-header-mobile-menu')
        .setAttribute('aria-expanded', (!!r).toString())
  },
  T = () => h(!1),
  C = () => {
    var r
    ;(r = document.getElementById('main-header-mobile-menu')) == null ||
      r.addEventListener('click', (e) =>
        h(e.currentTarget.getAttribute('aria-expanded') !== 'true')
      )
  }
class k extends HTMLDivElement {
  constructor() {
    super(), this.setupDom()
  }
  setupDom() {
    const e = crypto.randomUUID(),
      n = `content_${e}`,
      s = `button_${e}`,
      o = this.querySelector('.content')
    if (!o) return
    const t = document.createElement('button')
    t.setAttribute('id', s),
      t.classList.add('txt-link'),
      t.setAttribute('aria-expanded', this.dataset.open || 'false'),
      t.setAttribute('aria-controls', n),
      (t.innerHTML = (this.getAttribute('aria-label') || 'Hint') + f),
      t.addEventListener('click', () => {
        const d = t.getAttribute('aria-expanded') === 'true'
        t.setAttribute('aria-expanded', String(!d))
      }),
      this.prepend(t)
    const i = document.createElement('div'),
      c = o.parentNode
    i.classList.add('content-wrapper'),
      i.setAttribute('id', n),
      i.setAttribute('aria-labelledby', s),
      i.setAttribute('role', 'region'),
      c == null || c.insertBefore(i, o),
      i.appendChild(o)
  }
}
const R = () => {
  customElements.define('hint-box', k, { extends: 'div' })
}
window.addEventListener('load', () => {
  globalThis.devMode || (_(), A(), w(), S(), D(), P(), C(), R())
})
window.addEventListener('DOMContentLoaded', () => {
  const r = window.matchMedia('(min-width: 800px)'),
    e = () => {
      r.matches && T()
    }
  r.addEventListener('change', e)
})
