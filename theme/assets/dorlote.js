/* Maison Dorlote : comportements de la page (galerie, offres, avant/après, teintes,
   barre d'achat, panier Ajax Shopify, FAQ, formulaire de contact). */
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var root = (window.Shopify && Shopify.routes && Shopify.routes.root) || '/';
  var money = function (cents) {
    return (cents / 100).toFixed(2).replace('.', ',') + ' €';
  };
  var esc = function (s) { var d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; };

  /* Galerie */
  var main = $('#main-img');
  $$('.thumbs button').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!main || window.matchMedia('(max-width:900px)').matches) return;
      $$('.thumbs button').forEach(function (x) { x.setAttribute('aria-current', 'false'); });
      b.setAttribute('aria-current', 'true');
      main.style.opacity = 0;
      setTimeout(function () { main.removeAttribute('srcset'); main.src = b.dataset.src; main.alt = b.dataset.alt; main.style.opacity = 1; }, 180);
    });
  });
  var th = $('.thumbs'), cpt = $('#compteur-galerie');
  if (th && cpt) {
    th.addEventListener('scroll', function () {
      var n = th.children.length, w = th.scrollWidth / n;
      cpt.textContent = Math.min(n, Math.round(th.scrollLeft / w) + 1) + ' / ' + n;
    }, { passive: true });
  }

  /* Prix selon l'offre choisie */
  $$('.offres input[type=radio]').forEach(function (r) {
    r.addEventListener('change', function () {
      var p = r.dataset.prix;
      if ($('#prix-affiche')) $('#prix-affiche').textContent = p;
      var s = $('#sticky-buy strong'); if (s) s.textContent = p;
    });
  });

  /* Avant / après */
  var ba = $('#ba'), range = $('#ba-range');
  if (ba && range) range.addEventListener('input', function () { ba.style.setProperty('--pos', range.value + '%'); });

  /* Teintes */
  $$('.choix button').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('.choix button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      $$('#teinte-img img').forEach(function (i) { i.classList.toggle('on', i.dataset.t === b.dataset.t); });
    });
  });

  /* Date de livraison estimée (jours ouvrés) */
  function ouvres(n) { var d = new Date(); while (n > 0) { d.setDate(d.getDate() + 1); var j = d.getDay(); if (j !== 0 && j !== 6) n--; } return d; }
  var dl = $('#date-livraison');
  if (dl) {
    try {
      var f = new Intl.DateTimeFormat('fr-FR', { weekday: 'short', day: 'numeric', month: 'long' });
      var txt = 'recevez-la entre le ' + f.format(ouvres(+dl.dataset.min || 6)) + ' et le ' + f.format(ouvres(+dl.dataset.max || 9));
      dl.textContent = 'commandez aujourd’hui, ' + txt;
      if ($('#panier-date')) $('#panier-date').textContent = txt;
    } catch (e) {}
  }

  /* Toast */
  var tt;
  function toast(m) { var e = $('#toast'); if (!e) return; e.textContent = m; e.classList.add('show'); clearTimeout(tt); tt = setTimeout(function () { e.classList.remove('show'); }, 2400); }

  /* Panier (API Ajax Shopify) */
  var panier = $('#panier'), voile = $('#voile'), openBtn = $('#open-cart');
  var MOINS = '<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  var PLUS = '<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8M6 2v8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  var cartState = null, msgTimer;

  function api(path, body) {
    return fetch(root + path, {
      method: body ? 'POST' : 'GET',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: body ? JSON.stringify(body) : undefined
    }).then(function (r) { return r.json().then(function (j) { if (!r.ok) throw j; return j; }); });
  }
  function ouvrir() { if (!panier) return; panier.classList.add('show'); voile.classList.add('show'); panier.setAttribute('aria-hidden', 'false'); setTimeout(function () { $('#close-cart').focus(); }, 50); }
  function fermer() { panier.classList.remove('show'); voile.classList.remove('show'); panier.setAttribute('aria-hidden', 'true'); if (openBtn) openBtn.focus(); }

  function rendu(cart) {
    cartState = cart;
    if ($('#cart-count')) $('#cart-count').textContent = cart.item_count;
    var h = '';
    if (!cart.item_count) {
      h = '<div class="vide">Votre panier est vide.</div>';
    } else {
      cart.items.forEach(function (it, i) {
        var img = it.image ? '<img src="' + esc(it.image) + (it.image.indexOf('?') > -1 ? '&' : '?') + 'width=160" alt="">' : '';
        var sous = it.variant_title && it.variant_title !== 'Default Title' ? esc(it.variant_title) : '';
        h += '<div class="ligne-p">' + img + '<div><div class="t">' + esc(it.product_title) + '</div><div class="s">' + sous + '</div>' +
          '<div class="qte"><button type="button" data-l="' + (i + 1) + '" data-q="' + (it.quantity - 1) + '" aria-label="Retirer un">' + MOINS + '</button><span>' + it.quantity + '</span>' +
          '<button type="button" data-l="' + (i + 1) + '" data-q="' + (it.quantity + 1) + '" aria-label="Ajouter un">' + PLUS + '</button></div></div>' +
          '<div class="v">' + money(it.final_line_price) + '</div></div>';
      });
      var cadeau = cart.attributes && cart.attributes['C’est pour offrir'] === 'Oui';
      var msg = (cart.attributes && cart.attributes['Message cadeau']) || '';
      h += '<div class="cadeau-panier"><label class="chk" for="gift"><input type="checkbox" id="gift"' + (cadeau ? ' checked' : '') + '><span><span class="t">C’est pour offrir</span><br><span class="s">Ajoutez un message pour les heureux parents.</span></span></label>' +
        (cadeau ? '<label class="visually-hidden" for="gift-msg">Votre message</label><textarea id="gift-msg" maxlength="200" placeholder="Votre message (200 caractères maximum)">' + esc(msg) + '</textarea><small id="gift-cpt">' + msg.length + ' / 200</small>' : '') + '</div>';
    }
    $('#corps').innerHTML = h;
    $('#total').textContent = money(cart.total_price);
    $$('.qte button', panier).forEach(function (b) {
      b.addEventListener('click', function () {
        api('cart/change.js', { line: +b.dataset.l, quantity: Math.max(0, +b.dataset.q) }).then(rendu).catch(function () { toast('Impossible de modifier le panier.'); });
      });
    });
    var gc = $('#gift');
    if (gc) gc.addEventListener('change', function () {
      api('cart/update.js', { attributes: { 'C’est pour offrir': gc.checked ? 'Oui' : '', 'Message cadeau': gc.checked ? msg : '' } }).then(function (c) { rendu(c); var m = $('#gift-msg'); if (m) m.focus(); });
    });
    var gm = $('#gift-msg');
    if (gm) gm.addEventListener('input', function () {
      $('#gift-cpt').textContent = gm.value.length + ' / 200';
      clearTimeout(msgTimer);
      msgTimer = setTimeout(function () { api('cart/update.js', { attributes: { 'Message cadeau': gm.value } }).then(function (c) { cartState = c; }); }, 600);
    });
  }
  function charger() { return api('cart.js').then(rendu); }

  var form = $('#form-produit');
  function ajouter(e) {
    if (e) e.preventDefault();
    if (!form) return;
    var id = (form.querySelector('[name=id]:checked') || form.querySelector('[name=id]')).value;
    var b = $('#add'); if (b) b.setAttribute('aria-busy', 'true');
    api('cart/add.js', { items: [{ id: +id, quantity: 1 }] })
      .then(charger).then(ouvrir)
      .catch(function (err) { toast((err && err.description) || 'Ajout impossible, réessayez.'); })
      .then(function () { if (b) b.removeAttribute('aria-busy'); });
  }
  if (form) form.addEventListener('submit', ajouter);
  if ($('#sticky-add')) $('#sticky-add').addEventListener('click', ajouter);
  if (openBtn) openBtn.addEventListener('click', function () { charger().then(ouvrir).catch(function () { location.href = root + 'cart'; }); });
  if ($('#close-cart')) $('#close-cart').addEventListener('click', fermer);
  if (voile) voile.addEventListener('click', fermer);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panier && panier.classList.contains('show')) fermer(); });

  /* Barre d'achat fixe (mobile) */
  var sticky = $('#sticky-buy'), add = $('#add');
  if (sticky && add && 'IntersectionObserver' in window) {
    var vu = true;
    var upd = function () { var show = !vu && add.getBoundingClientRect().top < 0; sticky.classList.toggle('show', show); sticky.setAttribute('aria-hidden', String(!show)); $('#sticky-add').tabIndex = show ? 0 : -1; };
    new IntersectionObserver(function (e) { vu = e[0].isIntersecting; upd(); }).observe(add);
    window.addEventListener('scroll', upd, { passive: true });
  }

  /* FAQ : filtres */
  var fb = $$('.faq-filtres button');
  fb.forEach(function (b) {
    b.addEventListener('click', function () {
      fb.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      $$('.faq details').forEach(function (d) { d.hidden = !(b.dataset.f === 'tout' || d.dataset.cat === b.dataset.f); });
    });
  });

  /* Formulaire de contact : aide et vérification avant envoi à Shopify */
  var cf = $('#cf');
  if (cf) {
    var reps = []; try { reps = JSON.parse($('#cf-reponses').textContent).map(function (s) { return s.trim(); }); } catch (e) {}
    var err = function (id, m) { var e = document.getElementById(id + '-err'); if (e) e.textContent = m; var i = document.getElementById(id); if (i) i.setAttribute('aria-invalid', m ? 'true' : 'false'); };
    var canal = function () { var c = cf.querySelector('[data-canal]:checked'); return c ? c.dataset.canal : 'email'; };
    $$('[data-canal]', cf).forEach(function (r) { r.addEventListener('change', function () { $('#cf-tel-champ').hidden = canal() === 'email'; err('cf-tel', ''); }); });
    $$('input[name="contact[Thème]"]', cf).forEach(function (r) {
      r.addEventListener('change', function () {
        var t = reps[+r.dataset.index] || '';
        $('#cf-rapide').hidden = !t; $('#cf-rapide-txt').textContent = t;
        $('#cf-commande-champ').hidden = r.value !== 'Ma commande'; $('#cf-theme-err').textContent = '';
      });
    });
    var msgEl = $('#cf-message');
    if (msgEl) msgEl.addEventListener('input', function () { $('#cf-compteur').textContent = msgEl.value.length + ' / 1000'; });
    cf.addEventListener('submit', function (e) {
      var ok = true, premier = null;
      var ko = function (id, m) { err(id, m); ok = false; if (!premier) premier = document.getElementById(id); };
      if (!$('#cf-prenom').value.trim()) ko('cf-prenom', 'Indiquez votre prénom.'); else err('cf-prenom', '');
      if (!$('#cf-nom').value.trim()) ko('cf-nom', 'Indiquez votre nom.'); else err('cf-nom', '');
      var v = $('#cf-email').value.trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) ko('cf-email', v ? 'Cette adresse email semble incomplète. Exemple : prenom@exemple.fr' : 'Indiquez votre adresse email.'); else err('cf-email', '');
      if (canal() !== 'email') {
        var d = $('#cf-tel').value.replace(/[\s.\-]/g, '').replace(/^\+33/, '0');
        if (!/^0[1-9]\d{8}$/.test(d)) ko('cf-tel', 'Indiquez un numéro valide. Exemple : 06 12 34 56 78'); else err('cf-tel', '');
      }
      if (!cf.querySelector('input[name="contact[Thème]"]:checked')) { $('#cf-theme-err').textContent = 'Choisissez le thème de votre question.'; ok = false; if (!premier) premier = cf.querySelector('input[name="contact[Thème]"]'); }
      if (msgEl.value.trim().length < 5) ko('cf-message', 'Écrivez votre question en quelques mots.'); else err('cf-message', '');
      if (!$('#cf-consent').checked) { $('#cf-consent-err').textContent = 'Cochez cette case pour que nous puissions vous répondre.'; ok = false; if (!premier) premier = $('#cf-consent'); } else $('#cf-consent-err').textContent = '';
      if (!ok) { e.preventDefault(); if (premier) premier.focus(); }
    });
  }
})();
