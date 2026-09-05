<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
  <meta name="theme-color" content="#08090d">
  <meta name="mobile-web-app-capable" content="yes">
  <title>NOVA NFT</title>

  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <script src="https://unpkg.com/@tonconnect/ui@2.0.9/dist/tonconnect-ui.min.js"></script>

  <style>
    :root {
      --bg:#08090d;
      --card:#151821;
      --card2:#1b1f29;
      --text:#f5f7fb;
      --muted:#8d95a6;
      --blue:#3390ec;
      --blue2:#62b0ff;
      --gold:#ffc94a;
      --green:#35d47a;
      --red:#ff5d70;
      --line:rgba(255,255,255,.07);
      --safe:env(safe-area-inset-bottom,0px);
    }

    * {
      box-sizing:border-box;
      -webkit-tap-highlight-color:transparent;
    }

    html,body {
      margin:0;
      min-height:100%;
      background:var(--bg);
      color:var(--text);
      font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI",Roboto,Arial,sans-serif;
    }

    body {
      overflow-x:hidden;
      background:
        radial-gradient(circle at 50% -10%,rgba(51,144,236,.14),transparent 34%),
        var(--bg);
    }

    button,input {
      font:inherit;
    }

    button {
      border:0;
      color:inherit;
      cursor:pointer;
    }

    .app {
      width:100%;
      max-width:720px;
      min-height:100vh;
      margin:auto;
      padding-bottom:calc(90px + var(--safe));
    }

    /* TOP */

    .topbar {
      position:sticky;
      top:0;
      z-index:20;
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:13px 15px;
      background:rgba(8,9,13,.88);
      backdrop-filter:blur(22px);
      -webkit-backdrop-filter:blur(22px);
      border-bottom:1px solid rgba(255,255,255,.045);
    }

    .brand {
      display:flex;
      align-items:center;
      gap:10px;
    }

    .logo {
      width:39px;
      height:39px;
      display:grid;
      place-items:center;
      border-radius:13px;
      background:linear-gradient(145deg,#5db0ff,#2476d1);
      box-shadow:0 8px 28px rgba(51,144,236,.25);
      font-weight:900;
      font-size:19px;
    }

    .brand-name {
      font-size:16px;
      font-weight:850;
    }

    .brand-sub {
      margin-top:2px;
      color:var(--muted);
      font-size:10px;
    }

    .sell-top {
      padding:10px 12px;
      border-radius:13px;
      background:rgba(51,144,236,.14);
      color:#73baff;
      font-size:12px;
      font-weight:800;
    }

    /* PAGES */

    .page {
      display:none;
      padding:17px 15px;
      animation:pageIn .18s ease;
    }

    .page.active {
      display:block;
    }

    @keyframes pageIn {
      from {opacity:0;transform:translateY(5px)}
      to {opacity:1;transform:none}
    }

    /* MARKET */

    .hero {
      padding:23px;
      border:1px solid var(--line);
      border-radius:24px;
      background:
        radial-gradient(circle at 90% 10%,rgba(51,144,236,.2),transparent 35%),
        linear-gradient(145deg,#171d28,#10131a);
    }

    .hero-label {
      color:#75baff;
      font-size:10px;
      font-weight:850;
      letter-spacing:.8px;
      text-transform:uppercase;
    }

    .hero h1 {
      margin:8px 0 7px;
      font-size:28px;
      line-height:1.04;
      letter-spacing:-1.2px;
    }

    .hero p {
      margin:0;
      color:var(--muted);
      font-size:12px;
      line-height:1.5;
    }

    .section-head {
      display:flex;
      justify-content:space-between;
      align-items:center;
      margin:21px 3px 12px;
    }

    .section-title {
      font-size:18px;
      font-weight:850;
    }

    .section-count {
      color:var(--muted);
      font-size:11px;
    }

    .market-grid {
      display:grid;
      grid-template-columns:repeat(2,minmax(0,1fr));
      gap:11px;
    }

    .nft-card {
      overflow:hidden;
      border:1px solid var(--line);
      border-radius:19px;
      background:var(--card);
    }

    .nft-image,
    .nft-empty-image {
      display:block;
      width:100%;
      aspect-ratio:1;
      object-fit:cover;
      background:#101218;
    }

    .nft-empty-image {
      display:grid;
      place-items:center;
      color:#5d6676;
      font-size:31px;
    }

    .nft-info {
      padding:11px;
    }

    .nft-name {
      overflow:hidden;
      text-overflow:ellipsis;
      white-space:nowrap;
      font-size:13px;
      font-weight:800;
    }

    .nft-seller {
      margin-top:4px;
      overflow:hidden;
      text-overflow:ellipsis;
      white-space:nowrap;
      color:var(--muted);
      font-size:10px;
    }

    .nft-bottom {
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:6px;
      margin-top:10px;
    }

    .price {
      font-size:12px;
      font-weight:850;
    }

    .star {
      color:var(--gold);
    }

    .buy {
      padding:8px 10px;
      border-radius:10px;
      background:var(--blue);
      font-size:10px;
      font-weight:850;
    }

    .empty {
      padding:55px 20px;
      text-align:center;
      border:1px dashed rgba(255,255,255,.09);
      border-radius:22px;
      background:rgba(255,255,255,.018);
    }

    .empty-icon {
      width:59px;
      height:59px;
      margin:auto;
      display:grid;
      place-items:center;
      border-radius:19px;
      background:#151821;
      color:#697384;
      font-size:27px;
    }

    .empty-title {
      margin-top:15px;
      font-size:17px;
      font-weight:850;
    }

    .empty-text {
      max-width:300px;
      margin:7px auto 0;
      color:var(--muted);
      font-size:11px;
      line-height:1.55;
    }

    .empty-button {
      margin-top:17px;
      padding:11px 16px;
      border-radius:13px;
      background:var(--blue);
      font-size:12px;
      font-weight:850;
    }

    .loading {
      display:flex;
      justify-content:center;
      align-items:center;
      gap:8px;
      padding:45px 0;
      color:var(--muted);
      font-size:11px;
    }

    .spinner {
      width:15px;
      height:15px;
      border:2px solid rgba(255,255,255,.13);
      border-top-color:var(--blue);
      border-radius:50%;
      animation:spin .7s linear infinite;
    }

    @keyframes spin {
      to {transform:rotate(360deg)}
    }

    /* BALANCE */

    .balance {
      padding:23px;
      border-radius:24px;
      border:1px solid rgba(102,175,255,.12);
      background:
        radial-gradient(circle at 90% 10%,rgba(72,158,255,.23),transparent 34%),
        linear-gradient(145deg,#182334,#111722);
    }

    .balance-label {
      color:#96a1b2;
      font-size:11px;
    }

    .balance-number {
      margin-top:7px;
      font-size:34px;
      font-weight:900;
      letter-spacing:-1.5px;
    }

    .balance-unit {
      color:#82c0ff;
      font-size:13px;
      letter-spacing:0;
    }

    .balance-grid {
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:9px;
      margin-top:20px;
    }

    .primary,
    .secondary {
      padding:13px;
      border-radius:14px;
      font-size:12px;
      font-weight:850;
    }

    .primary {
      background:var(--blue);
    }

    .secondary {
      background:rgba(255,255,255,.07);
    }

    /* PROFILE */

    .profile {
      display:flex;
      align-items:center;
      gap:13px;
      padding:18px;
      border-radius:22px;
      background:var(--card);
      border:1px solid var(--line);
    }

    .avatar {
      width:62px;
      height:62px;
      flex:0 0 62px;
      object-fit:cover;
      border-radius:19px;
      background:#202530;
    }

    .avatar-placeholder {
      display:grid;
      place-items:center;
      color:#a0a9b9;
      font-size:22px;
      font-weight:850;
    }

    .profile-name {
      font-size:17px;
      font-weight:850;
    }

    .profile-username {
      margin-top:4px;
      color:var(--muted);
      font-size:11px;
    }

    .profile-balance {
      margin-top:5px;
      color:#72b9ff;
      font-size:11px;
      font-weight:750;
    }

    /* WALLET */

    .wallet {
      margin-top:12px;
      padding:17px;
      border:1px solid var(--line);
      border-radius:20px;
      background:var(--card);
    }

    .wallet-title {
      font-size:14px;
      font-weight:850;
    }

    .wallet-desc {
      margin-top:5px;
      color:var(--muted);
      font-size:10px;
      line-height:1.5;
    }

    #ton-connect {
      margin-top:14px;
      min-height:42px;
    }

    .wallet-address {
      display:none;
      margin-top:10px;
      padding:10px;
      border-radius:11px;
      background:#0d1015;
      color:#83bcfa;
      font-family:monospace;
      font-size:10px;
      word-break:break-all;
    }

    /* FORM */

    .form {
      padding:17px;
      border-radius:20px;
      background:var(--card);
      border:1px solid var(--line);
    }

    .field {
      margin-bottom:13px;
    }

    .field label {
      display:block;
      margin-bottom:7px;
      color:#a4adbd;
      font-size:10px;
      font-weight:750;
    }

    .field input {
      width:100%;
      padding:13px;
      outline:none;
      border:1px solid var(--line);
      border-radius:13px;
      background:#0f1218;
      color:white;
      font-size:13px;
    }

    .field input:focus {
      border-color:rgba(51,144,236,.55);
    }

    /* BONUS */

    .bonus {
      padding:23px;
      border-radius:23px;
      border:1px solid rgba(255,201,74,.1);
      background:
        radial-gradient(circle at 100% 0,rgba(255,201,74,.16),transparent 36%),
        linear-gradient(145deg,#211e16,#15140f);
    }

    .bonus-icon {
      font-size:34px;
    }

    .bonus h2 {
      margin:9px 0 6px;
      font-size:22px;
    }

    .bonus p {
      margin:0;
      color:var(--muted);
      font-size:11px;
      line-height:1.5;
    }

    .bonus-list {
      display:grid;
      gap:9px;
      margin-top:15px;
    }

    .bonus-item {
      padding:14px;
      border:1px solid var(--line);
      border-radius:15px;
      background:rgba(255,255,255,.035);
    }

    .bonus-item strong {
      font-size:12px;
    }

    .bonus-item span {
      display:block;
      margin-top:4px;
      color:var(--muted);
      font-size:10px;
    }

    /* MENU */

    .menu {
      margin-top:12px;
      overflow:hidden;
      border:1px solid var(--line);
      border-radius:20px;
      background:var(--card);
    }

    .menu button {
      width:100%;
      display:flex;
      align-items:center;
      gap:12px;
      padding:15px;
      background:transparent;
      text-align:left;
      border-bottom:1px solid var(--line);
    }

    .menu button:last-child {
      border-bottom:0;
    }

    .menu-icon {
      width:36px;
      height:36px;
      display:grid;
      place-items:center;
      border-radius:11px;
      background:#202530;
    }

    .menu-text {
      flex:1;
    }

    .menu-name {
      font-size:12px;
      font-weight:800;
    }

    .menu-sub {
      margin-top:3px;
      color:var(--muted);
      font-size:9px;
    }

    .arrow {
      color:#606878;
      font-size:18px;
    }

    /* NAV */

    .nav {
      position:fixed;
      left:50%;
      bottom:0;
      z-index:100;
      transform:translateX(-50%);
      width:min(720px,100%);
      display:grid;
      grid-template-columns:repeat(4,1fr);
      padding:7px 9px calc(7px + var(--safe));
      background:rgba(9,10,14,.95);
      backdrop-filter:blur(23px);
      -webkit-backdrop-filter:blur(23px);
      border-top:1px solid var(--line);
    }

    .nav-btn {
      padding:6px 2px;
      background:transparent;
      color:#70798a;
    }

    .nav-btn.active {
      color:#69b4ff;
    }

    .nav-icon {
      height:21px;
      font-size:17px;
      line-height:19px;
    }

    .nav-label {
      margin-top:3px;
      font-size:9px;
      font-weight:750;
    }

    /* TOAST */

    .toast {
      position:fixed;
      left:50%;
      bottom:calc(78px + var(--safe));
      z-index:200;
      width:max-content;
      max-width:calc(100% - 30px);
      padding:11px 15px;
      transform:translate(-50%,15px);
      opacity:0;
      pointer-events:none;
      border-radius:13px;
      background:#222630;
      box-shadow:0 12px 35px rgba(0,0,0,.45);
      font-size:11px;
      transition:.2s;
    }

    .toast.show {
      opacity:1;
      transform:translate(-50%,0);
    }

    @media(min-width:600px) {
      .market-grid {
        grid-template-columns:repeat(3,minmax(0,1fr));
      }
    }
  </style>
</head>

<body>

<div class="app">

  <header class="topbar">
    <div class="brand">
      <div class="logo">N</div>
      <div>
        <div class="brand-name">NOVA</div>
        <div class="brand-sub">NFT Marketplace</div>
      </div>
    </div>

    <button class="sell-top" onclick="openSell()">
      ＋ Выставить NFT
    </button>
  </header>


  <!-- MARKET -->

  <main id="market" class="page active">

    <section class="hero">
      <div class="hero-label">Telegram NFT Marketplace</div>

      <h1>
        Реальные NFT.<br>
        Без фейковых карточек.
      </h1>

      <p>
        Маркет показывает только активные объявления,
        полученные с твоего backend.
      </p>
    </section>

    <div class="section-head">
      <div class="section-title">Маркет</div>
      <div id="count" class="section-count">0 NFT</div>
    </div>

    <div id="marketContent">
      <div class="loading">
        <div class="spinner"></div>
        Загрузка...
      </div>
    </div>

  </main>


  <!-- TOP UP -->

  <main id="topup" class="page">

    <div class="section-title" style="margin:5px 3px 15px">
      Пополнить
    </div>

    <section class="balance">

      <div class="balance-label">
        Баланс NOVA
      </div>

      <div class="balance-number">
        <span id="balance">0</span>
        <span class="balance-unit">⭐ Stars</span>
      </div>

      <div class="balance-grid">
        <button class="primary" onclick="createInvoice(100)">
          +100 ⭐
        </button>

        <button class="secondary" onclick="createInvoice(500)">
          +500 ⭐
        </button>
      </div>

    </section>

    <section class="form" style="margin-top:12px">

      <div class="field">
        <label>СВОЯ СУММА</label>
        <input
          id="customAmount"
          type="number"
          min="1"
          max="10000000"
          placeholder="Количество Stars"
        >
      </div>

      <button
        class="primary"
        style="width:100%"
        onclick="customTopup()"
      >
        Пополнить
      </button>

    </section>

  </main>


  <!-- BONUS -->

  <main id="bonus" class="page">

    <section class="bonus">

      <div class="bonus-icon">🎁</div>

      <h2>Бонусы NOVA</h2>

      <p>
        Бонусная система будет подключена отдельно.
        Никаких выдуманных начислений.
      </p>

      <div class="bonus-list">

        <div class="bonus-item">
          <strong>⭐ Бонус за активность</strong>
          <span>Скоро</span>
        </div>

        <div class="bonus-item">
          <strong>🎨 Бонус продавцам</strong>
          <span>Скоро</span>
        </div>

        <div class="bonus-item">
          <strong>🚀 Реферальная система</strong>
          <span>Скоро</span>
        </div>

      </div>

    </section>

  </main>


  <!-- PROFILE -->

  <main id="profile" class="page">

    <div class="section-title" style="margin:5px 3px 15px">
      Профиль
    </div>

    <section class="profile">

      <div id="avatar" class="avatar avatar-placeholder">
        N
      </div>

      <div style="min-width:0">

        <div id="profileName" class="profile-name">
          Пользователь Telegram
        </div>

        <div id="profileUsername" class="profile-username">
          Telegram
        </div>

        <div class="profile-balance">
          Баланс:
          <span id="profileBalance">0</span>
          ⭐
        </div>

      </div>

    </section>


    <!-- TON CONNECT -->

    <section class="wallet">

      <div class="wallet-title">
        TON-кошелёк
      </div>

      <div class="wallet-desc">
        Подключение через TON Connect.
        Можно выбрать Tonkeeper или другой совместимый кошелёк,
        включая Telegram Wallet.
      </div>

      <div id="ton-connect"></div>

      <div id="walletAddress" class="wallet-address"></div>

    </section>


    <section class="menu">

      <button onclick="openMyListings()">
        <div class="menu-icon">🖼</div>

        <div class="menu-text">
          <div class="menu-name">Мои NFT</div>
          <div class="menu-sub">
            Твои объявления
          </div>
        </div>

        <div class="arrow">›</div>
      </button>


      <button onclick="loadListings();showToast('Маркет обновлён')">
        <div class="menu-icon">↻</div>

        <div class="menu-text">
          <div class="menu-name">Обновить маркет</div>
          <div class="menu-sub">
            Получить актуальные данные
          </div>
        </div>

        <div class="arrow">›</div>
      </button>


      <button onclick="showToast('Комиссия NOVA: 0%')">
        <div class="menu-icon">✦</div>

        <div class="menu-text">
          <div class="menu-name">NOVA Marketplace</div>
          <div class="menu-sub">
            Комиссия платформы — 0%
          </div>
        </div>

        <div class="arrow">›</div>
      </button>

    </section>

  </main>


  <!-- SELL -->

  <main id="sell" class="page">

    <div class="section-title" style="margin:5px 3px 15px">
      Выставить NFT
    </div>

    <section class="form">

      <div class="field">
        <label>НАЗВАНИЕ NFT</label>

        <input
          id="sellTitle"
          maxlength="100"
          placeholder="Название подарка"
        >
      </div>


      <div class="field">
        <label>ЦЕНА В STARS</label>

        <input
          id="sellPrice"
          type="number"
          min="1"
          placeholder="Например, 500"
        >
      </div>


      <div class="field">
        <label>TELEGRAM GIFT ID</label>

        <input
          id="sellGiftId"
          placeholder="ID настоящего Telegram Gift"
        >
      </div>


      <div class="field">
        <label>URL ИЗОБРАЖЕНИЯ</label>

        <input
          id="sellImage"
          type="url"
          placeholder="https://..."
        >
      </div>


      <button
        class="primary"
        style="width:100%"
        onclick="submitListing()"
      >
        Выставить NFT
      </button>


      <div style="
        margin-top:12px;
        color:#727b8c;
        font-size:9px;
        line-height:1.5;
      ">
        Используй только настоящий Telegram Gift.
        Seed-фраза и приватный ключ кошелька никогда не нужны.
      </div>

    </section>

  </main>

</div>


<!-- NAV -->

<nav class="nav">

  <button
    class="nav-btn active"
    data-page="market"
    onclick="switchPage('market',this)"
  >
    <div class="nav-icon">⌂</div>
    <div class="nav-label">Маркет</div>
  </button>


  <button
    class="nav-btn"
    data-page="topup"
    onclick="switchPage('topup',this)"
  >
    <div class="nav-icon">⭐</div>
    <div class="nav-label">Пополнить</div>
  </button>


  <button
    class="nav-btn"
    data-page="bonus"
    onclick="switchPage('bonus',this)"
  >
    <div class="nav-icon">🎁</div>
    <div class="nav-label">Бонусы</div>
  </button>


  <button
    class="nav-btn"
    data-page="profile"
    onclick="switchPage('profile',this)"
  >
    <div class="nav-icon">●</div>
    <div class="nav-label">Профиль</div>
  </button>

</nav>


<div id="toast" class="toast"></div>


<script>

  /* =========================================================
     NOVA CONFIG
     ========================================================= */

  const API =
    "https://houses-nato-answers-sword.trycloudflare.com";

  const TON_MANIFEST =
    "https://alexsali593-droid.github.io/Zalupa/tonconnect-manifest.json";


  /* =========================================================
     TELEGRAM
     ========================================================= */

  const tg =
    window.Telegram &&
    window.Telegram.WebApp
      ? window.Telegram.WebApp
      : null;

  let tgUser = null;

  if (tg) {

    try {

      tg.ready();
      tg.expand();

      if (tg.setHeaderColor)
        tg.setHeaderColor("#08090d");

      if (tg.setBackgroundColor)
        tg.setBackgroundColor("#08090d");

      tgUser =
        tg.initDataUnsafe &&
        tg.initDataUnsafe.user
          ? tg.initDataUnsafe.user
          : null;

    } catch (e) {
      console.warn(e);
    }

  }


  /* =========================================================
     STATE
     ========================================================= */

  let nfts = [];
  let tonUI = null;
  let currentWallet = null;


  /* =========================================================
     PROFILE
     ========================================================= */

  function updateProfile() {

    if (!tgUser)
      return;

    const name =
      [
        tgUser.first_name || "",
        tgUser.last_name || ""
      ]
      .join(" ")
      .trim() ||
      "Пользователь Telegram";


    document.getElementById("profileName").textContent =
      name;


    document.getElementById("profileUsername").textContent =
      tgUser.username
        ? "@" + tgUser.username
        : "Telegram";


    const avatar =
      document.getElementById("avatar");


    if (tgUser.photo_url) {

      avatar.className = "avatar";
      avatar.src = tgUser.photo_url;
      avatar.alt = name;

    } else {

      avatar.className =
        "avatar avatar-placeholder";

      avatar.textContent =
        name.charAt(0).toUpperCase();

    }

  }

  updateProfile();


  /* =========================================================
     NAVIGATION
     ========================================================= */

  function switchPage(pageId, button) {

    document
      .querySelectorAll(".page")
      .forEach(page => {
        page.classList.remove("active");
      });


    const page =
      document.getElementById(pageId);

    if (page)
      page.classList.add("active");


    document
      .querySelectorAll(".nav-btn")
      .forEach(btn => {
        btn.classList.remove("active");
      });


    if (button)
      button.classList.add("active");


    window.scrollTo({
      top:0,
      behavior:"smooth"
    });

  }


  function openSell() {

    document
      .querySelectorAll(".page")
      .forEach(page =>
        page.classList.remove("active")
      );

    document
      .getElementById("sell")
      .classList.add("active");

    document
      .querySelectorAll(".nav-btn")
      .forEach(btn =>
        btn.classList.remove("active")
      );

    window.scrollTo(0,0);

  }


  /* =========================================================
     TOAST
     ========================================================= */

  function showToast(message) {

    const toast =
      document.getElementById("toast");

    toast.textContent = message;

    toast.classList.add("show");

    clearTimeout(window.__toast);

    window.__toast =
      setTimeout(() => {
        toast.classList.remove("show");
      },2600);

  }


  /* =========================================================
     ESCAPE
     ========================================================= */

  function escapeHTML(value) {

    return String(value ?? "")
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;")
      .replaceAll("'","&#039;");

  }


  /* =========================================================
     MARKET
     ========================================================= */

  async function loadListings() {

    const content =
      document.getElementById("marketContent");


    content.innerHTML = `
      <div class="loading">
        <div class="spinner"></div>
        Загрузка NFT...
      </div>
    `;


    try {

      const response =
        await fetch(
          API + "/api/listings",
          {
            method:"GET",
            cache:"no-store"
          }
        );


      if (!response.ok)
        throw new Error(
          "Backend HTTP " +
          response.status
        );


      const data =
        await response.json();


      /*
        КРИТИЧЕСКИ ВАЖНО:

        Здесь НЕТ demoNFT.
        Здесь НЕТ fallback.
        Здесь НЕТ выдуманных карточек.

        Если backend вернул [] —
        на экране будет "NFT пока нет".
      */

      nfts =
        Array.isArray(data.items)
          ? data.items.filter(item =>
              item &&
              item.status === "active" &&
              item.telegram_gift_id
            )
          : [];


      renderMarket();

    } catch (error) {

      console.error(
        "NOVA marketplace:",
        error
      );


      nfts = [];

      document.getElementById("count")
        .textContent = "0 NFT";


      content.innerHTML = `
        <div class="empty">

          <div class="empty-icon">
            ◇
          </div>

          <div class="empty-title">
            NFT пока нет
          </div>

          <div class="empty-text">
            Активных объявлений сейчас нет.
            Фейковые NFT не показываются.
          </div>

          <button
            class="empty-button"
            onclick="loadListings()"
          >
            Обновить
          </button>

        </div>
      `;

    }

  }


  function renderMarket() {

    const content =
      document.getElementById("marketContent");


    const count =
      document.getElementById("count");


    count.textContent =
      nfts.length + " NFT";


    if (!nfts.length) {

      content.innerHTML = `
        <div class="empty">

          <div class="empty-icon">
            ◇
          </div>

          <div class="empty-title">
            NFT пока нет
          </div>

          <div class="empty-text">
            Сейчас на маркетплейсе нет
            активных объявлений.
            Когда появится настоящее NFT,
            оно автоматически появится здесь.
          </div>

          <button
            class="empty-button"
            onclick="openSell()"
          >
            Выставить NFT
          </button>

        </div>
      `;

      return;
    }


    content.innerHTML = `
      <div class="market-grid">
        ${nfts.map(renderNFT).join("")}
      </div>
    `;

  }


  function renderNFT(item) {

    const id =
      escapeHTML(item.id);

    const title =
      escapeHTML(
        item.title ||
        "Telegram Gift"
      );


    const seller =
      escapeHTML(
        item.seller_username
          ? "@" + item.seller_username
          : "Продавец"
      );


    const image =
      escapeHTML(
        item.image_url || ""
      );


    const price =
      Number(
        item.price_stars || 0
      );


    const imageHTML =
      image

        ? `
          <img
            class="nft-image"
            src="${image}"
            alt="${title}"
            loading="lazy"
            onerror="
              this.outerHTML=
              '<div class=&quot;nft-empty-image&quot;>◇</div>'
            "
          >
        `

        : `
          <div class="nft-empty-image">
            ◇
          </div>
        `;


    return `
      <article
        class="nft-card"
        data-id="${id}"
      >

        ${imageHTML}

        <div class="nft-info">

          <div class="nft-name">
            ${title}
          </div>

          <div class="nft-seller">
            ${seller}
          </div>

          <div class="nft-bottom">

            <div class="price">
              <span class="star">★</span>
              ${price.toLocaleString("ru-RU")}
            </div>

            <button
              class="buy"
              onclick="buyNFT('${id}')"
            >
              Купить
            </button>

          </div>

        </div>

      </article>
    `;

  }


  function buyNFT(id) {

    const item =
      nfts.find(
        x => String(x.id) === String(id)
      );


    if (!item) {

      showToast(
        "NFT больше недоступна"
      );

      return;
    }


    showToast(
      "Оплата NFT будет подключена через backend"
    );

  }


  /* =========================================================
     STARS
     ========================================================= */

  async function createInvoice(amount) {

    if (!tg || !tg.initData) {

      showToast(
        "Открой приложение внутри Telegram"
      );

      return;
    }


    try {

      showToast(
        "Создаём счёт..."
      );


      const response =
        await fetch(
          API + "/api/invoice",
          {
            method:"POST",
            headers:{
              "Content-Type":
                "application/json",

              "Authorization":
                "tma " + tg.initData
            },

            body:JSON.stringify({
              amount_stars:Number(amount)
            })
          }
        );


      const data =
        await response.json();


      if (!response.ok || !data.ok)
        throw new Error(
          data.error ||
          "Ошибка создания счёта"
        );


      if (
        tg.openInvoice
      ) {

        tg.openInvoice(
          data.invoice_url,
          status => {

            if (status === "paid") {

              showToast(
                "Оплата прошла успешно ⭐"
              );

              loadBalance();

            }

            else if (
              status === "cancelled"
            ) {

              showToast(
                "Оплата отменена"
              );

            }

            else if (
              status === "failed"
            ) {

              showToast(
                "Оплата не прошла"
              );

            }

          }
        );

      } else {

        window.location.href =
          data.invoice_url;

      }


    } catch (error) {

      console.error(error);

      showToast(
        error.message ||
        "Ошибка оплаты"
      );

    }

  }


  function customTopup() {

    const amount =
      Number(
        document.getElementById(
          "customAmount"
        ).value
      );


    if (
      !Number.isInteger(amount) ||
      amount <= 0
    ) {

      showToast(
        "Введите корректную сумму"
      );

      return;
    }


    if (amount > 10000000) {

      showToast(
        "Слишком большая сумма"
      );

      return;
    }


    createInvoice(amount);

  }


  /*
    Пока backend не имеет /api/balance,
    баланс НЕ выдумывается.
  */

  async function loadBalance() {

    document.getElementById(
      "balance"
    ).textContent = "0";


    document.getElementById(
      "profileBalance"
    ).textContent = "0";

  }


  /* =========================================================
     SELL
     ========================================================= */

  async function submitListing() {

    const title =
      document.getElementById(
        "sellTitle"
      ).value.trim();


    const price =
      Number(
        document.getElementById(
          "sellPrice"
        ).value
      );


    const giftId =
      document.getElementById(
        "sellGiftId"
      ).value.trim();


    const image =
      document.getElementById(
        "sellImage"
      ).value.trim();


    if (!title) {

      showToast(
        "Введите название NFT"
      );

      return;
    }


    if (
      !Number.isInteger(price) ||
      price <= 0
    ) {

      showToast(
        "Введите корректную цену"
      );

      return;
    }


    if (!giftId) {

      showToast(
        "Укажи настоящий Telegram Gift ID"
      );

      return;
    }


    if (!tg || !tg.initData) {

      showToast(
        "Открой приложение внутри Telegram"
      );

      return;
    }


    try {

      const response =
        await fetch(
          API + "/api/listings",
          {
            method:"POST",

            headers:{
              "Content-Type":
                "application/json",

              "Authorization":
                "tma " + tg.initData
            },

            body:JSON.stringify({

              title:title,

              price_stars:price,

              telegram_gift_id:
                giftId,

              image_url:
                image

            })
          }
        );


      const data =
        await response.json();


      if (!response.ok || !data.ok)
        throw new Error(
          data.error ||
          "Ошибка создания объявления"
        );


      document.getElementById(
        "sellTitle"
      ).value = "";


      document.getElementById(
        "sellPrice"
      ).value = "";


      document.getElementById(
        "sellGiftId"
      ).value = "";


      document.getElementById(
        "sellImage"
      ).value = "";


      showToast(
        data.status === "active"
          ? "NFT выставлена"
          : "NFT отправлена на проверку"
      );


      await loadListings();


      switchPage(
        "market",
        document.querySelector(
          '[data-page="market"]'
        )
      );


    } catch (error) {

      console.error(error);

      showToast(
        error.message ||
        "Ошибка"
      );

    }

  }


  /* =========================================================
     MY LISTINGS
     ========================================================= */

  async function openMyListings() {

    if (!tg || !tg.initData) {

      showToast(
        "Открой приложение внутри Telegram"
      );

      return;
    }


    try {

      const response =
        await fetch(
          API + "/api/my-listings",
          {
            method:"GET",
            headers:{
              "Authorization":
                "tma " + tg.initData
            },
            cache:"no-store"
          }
        );


      const data =
        await response.json();


      if (!response.ok || !data.ok)
        throw new Error(
          data.error ||
          "Ошибка"
        );


      const count =
        Array.isArray(data.items)
          ? data.items.length
          : 0;


      showToast(
        count
          ? `У тебя ${count} NFT`
          : "У тебя пока нет NFT"
      );


    } catch (error) {

      console.error(error);

      showToast(
        error.message ||
        "Ошибка"
      );

    }

  }


  /* =========================================================
     TON CONNECT
     ========================================================= */

  function initTonConnect() {

    if (
      !window.TON_CONNECT_UI ||
      !window.TON_CONNECT_UI.TonConnectUI
    ) {

      console.error(
        "TON Connect UI не загрузился"
      );

      showToast(
        "TON Connect не загрузился"
      );

      return;
    }


    try {

      tonUI =
        new TON_CONNECT_UI.TonConnectUI({

          manifestUrl:
            TON_MANIFEST,

          buttonRootId:
            "ton-connect"

        });


      tonUI.onStatusChange(
        wallet => {

          currentWallet =
            wallet || null;

          renderWallet();

        }
      );


      if (
        tonUI.account
      ) {

        currentWallet =
          tonUI.account;

      }


      renderWallet();


    } catch (error) {

      console.error(
        "TON Connect error:",
        error
      );


      document.getElementById(
        "ton-connect"
      ).innerHTML = `
        <button
          class="secondary"
          style="width:100%"
          onclick="initTonConnect()"
        >
          Подключить TON-кошелёк
        </button>
      `;

    }

  }


  function renderWallet() {

    const box =
      document.getElementById(
        "walletAddress"
      );


    if (
      !currentWallet ||
      !currentWallet.account
    ) {

      box.style.display =
        "none";

      box.textContent =
        "";

      return;
    }


    const address =
      currentWallet.account.address ||
      "";


    if (!address)
      return;


    box.style.display =
      "block";


    box.textContent =
      address;

  }


  /* =========================================================
     START
     ========================================================= */

  document.addEventListener(
    "DOMContentLoaded",
    () => {

      /*
        Ждём загрузку TON UI.
      */

      setTimeout(
        initTonConnect,
        500
      );


      loadListings();

      loadBalance();

    }
  );

</script>

</body>
</html>